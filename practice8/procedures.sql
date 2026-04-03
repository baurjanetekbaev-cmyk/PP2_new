CREATE OR REPLACE PROCEDURE upsert(pname TEXT, pphone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = pname) THEN
        UPDATE phonebook SET phone = pphone WHERE name = pname;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES(pname, pphone);
    END IF;
END;
$$;

CREATE TABLE IF NOT EXISTS invalcon(
    name TEXT,
    phone TEXT
);

CREATE OR REPLACE PROCEDURE insertm(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE 
    i INT;
BEGIN
    FOR i IN 1..array_length(names,1) LOOP
        IF phones[i] ~ '^[0-9]{10,15}$' THEN
            CALL upsert(names[i], phones[i]);
        ELSE
            INSERT INTO invalcon(name, phone)
            VALUES(names[i], phones[i]);
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE deletec(key TEXT)
LANGUAGE plpgsql AS $$
BEGIN 
    DELETE FROM phonebook
    WHERE name = key OR phone = key;
END;
$$;