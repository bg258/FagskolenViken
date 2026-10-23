""" We create the SQLite database and read all the .csv data that we have created."""

import csv
import sqlite3
from pathlib import Path

MAPPE = Path(__file__).resolve().parent
DATABASE = MAPPE / "arbeidskrav1.db"


def les_csv(filnavn):
    with (MAPPE / filnavn).open(encoding="utf-8-sig", newline="") as fil:
        return list(csv.DictReader(fil))


with sqlite3.connect(DATABASE) as db:
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript((MAPPE / "tabeller.sql").read_text(encoding="utf-8"))

    kunder = les_csv("kunder.csv")
    db.executemany(
        "INSERT INTO kunder (kunde_id, navn, by, registrert_dato) VALUES (?, ?, ?, ?)",
        [(int(r["kunde_id"]), r["navn"], r["by"], r["registrert_dato"]) for r in kunder],
    )

    bestillinger = les_csv("bestillinger.csv")
    db.executemany(
        "INSERT INTO bestillinger (bestilling_id, kunde_id, dato, belop, status) "
        "VALUES (?, ?, ?, ?, ?)",
        [
            (int(r["bestilling_id"]), int(r["kunde_id"]), r["dato"], float(r["belop"]), r["status"])
            for r in bestillinger
        ],
    )
print("Ferdig. Du kan nå åpne databasen din og jobbe med den!.")
