class Coffee {
    constructor() {
        this.data = 'Coffee';
    }

    static toCode() {
        this.data = 'Code';
        return this.data;
    }
}

console.log(Coffee.toCode());
