CREATE TABLE public.drink_types (
    name            text PRIMARY KEY,
    created_at      timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated_at      timestamp with time zone DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE public.drink_entities (
    id              BIGSERIAL PRIMARY KEY,
    name            text NOT NULL,
    kind            text NOT NULL REFERENCES public.drink_types (name),
    brewed_at       timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    consumed_at     timestamp with time zone NULL
);

CREATE TABLE public.codes (
    id              BIGSERIAL PRIMARY KEY,
    consumed_drink  BIGINT NOT NULL REFERENCES public.drink_entities (id),
    created_at      timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- define trigger as coffee consumer
CREATE OR REPLACE FUNCTION consume_coffee_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.kind = 'coffee' THEN
        RAISE NOTICE 'can i haz % gulp gulp', NEW.name;
        NEW.consumed_at = CURRENT_TIMESTAMP;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- define trigger as coder to execute after drink
CREATE OR REPLACE FUNCTION write_code_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.kind = 'coffee' THEN
        RAISE NOTICE 'coding from drinked %', NEW.name;
        INSERT INTO public.codes (consumed_drink) VALUES (NEW.id);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- attach drinker and coder
CREATE TRIGGER consume_coffee
    BEFORE INSERT OR UPDATE
    ON public.drink_entities
    FOR EACH ROW EXECUTE FUNCTION consume_coffee_trigger();

CREATE TRIGGER write_code
    AFTER INSERT OR UPDATE
    ON public.drink_entities
    FOR EACH ROW EXECUTE FUNCTION write_code_trigger();

-- init drink_kinds
INSERT INTO public.drink_types (name) VALUES ('coffee');
INSERT INTO public.drink_types (name) VALUES ('tea');
