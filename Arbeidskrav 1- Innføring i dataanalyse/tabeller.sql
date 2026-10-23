PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS bestillinger;
DROP TABLE IF EXISTS kunder;

CREATE TABLE kunder (
    kunde_id INTEGER PRIMARY KEY,
    navn TEXT NOT NULL,
    by TEXT NOT NULL,
    registrert_dato TEXT NOT NULL
);

CREATE TABLE bestillinger (
    bestilling_id INTEGER PRIMARY KEY,
    kunde_id INTEGER NOT NULL,
    dato TEXT NOT NULL,
    belop REAL NOT NULL CHECK (belop >= 0),
    status TEXT NOT NULL,
    FOREIGN KEY (kunde_id) REFERENCES kunder(kunde_id)
);
