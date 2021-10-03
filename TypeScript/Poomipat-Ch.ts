//Observer
type Listener<EventType> = (ev: EventType) => void;
function createObserver<EventType>(): {
  subscribe: (listener: Listener<EventType>) => () => void;
  publish: (event: EventType) => void;
} {
  let listeners: Listener<EventType>[] = [];
  return {
    subscribe: (listener: Listener<EventType>): (() => void) => {
      listeners.push(listener);
      return () => {
        listeners = listeners.filter((l) => l !== listener);
      };
    },
    publish: (event: EventType) => {
      listeners.forEach((l) => l(event));
    },
  };
}

interface BeforeAddDataBase<T> {
  value: T;
  newValue: T;
}

interface AfterAddDataBase<T> {
  value: T;
}

interface Coffee {
  id: string;
  text: string;
}

interface BaseRecord {
  id: string;
}

interface DataBase<T extends BaseRecord> {
  set(newValue: T): void;
  get(id: string): T | undefined;

  onBeforeAdd(listener: Listener<BeforeAddDataBase<T>>): () => void;
  onAfterAdd(listener: Listener<AfterAddDataBase<T>>): () => void;
}

class InmemoryDataBase<T extends BaseRecord> implements DataBase<T> {
  private db: Record<string, T> = {};

  private beforeAddListener = createObserver<BeforeAddDataBase<T>>();
  private afterAddListener = createObserver<AfterAddDataBase<T>>();

  public set(newValue: T): void {
    this.beforeAddListener.publish({
      newValue,
      value: this.db[newValue.id],
    });

    this.db[newValue.id] = newValue;

    this.afterAddListener.publish({
      value: this.db[newValue.id],
    });
  }

  public get(id: string): T | undefined {
    return this.db[id];
  }

  onBeforeAdd(listener: Listener<BeforeAddDataBase<T>>): () => void {
    return this.beforeAddListener.subscribe(listener);
  }
  onAfterAdd(listener: Listener<AfterAddDataBase<T>>): () => void {
    return this.afterAddListener.subscribe(listener);
  }
}

const coffee = new InmemoryDataBase<Coffee>();

coffee.onAfterAdd(({ value }) => {
  console.log(value.text);
});

coffee.set({
  id: "1",
  text: [...new Set("coffee")].join("").replace(/[f]/, "d"),
});
