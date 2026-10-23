# **Arbeidskrav 1 – Innføring i dataanalyse**

For denne arbeidskravet har jeg brukt SQLite og to tabeller: `kunder` og `bestillinger`.
Alle kundene, bestillingene og beløpene er **fiktive**. Dette er data jeg har funnet på nett og funnet på selv. 

I tillegg har jeg valgt å lagre alt i README filen, blant annet beskrivelse av SQL spørringer og litt bevis. 

## How to Run the Project

1. Install Python 3. SQLite is included with Python through the `sqlite3` module.
2. Open the Terminal/PowerShell in the project folder.
3. Check the SQLite version:

   ```bash
   python -c "import sqlite3; print(sqlite3.sqlite_version)"
   ```

4. Create the database and import the CSV files:

   ```bash
   python3 database.py
   ```

   On some Windows computers, you may need to use `py` instead of `python`.

## Files

- `kunder.csv`: customer data containing 7 customers in total.
- `bestillinger.csv`: purchase data containing 9 orders in total.
- `tabeller.sql`: SQL statements for creating tables with primary keys and data types.
- `sporringer.sql`: SQL queries using INNER JOIN and LEFT JOIN.
- `database.py`: Python script that imports the CSV files into an SQLite database.
- `arbeidskrav1.db`: The completed SQLite database.

## **Screenshots**
### SQLite Installation
The screenshot below shows that SQLite is installed and working.

![SQLite Installation](screenshots/database1.png)
![SQLite Installation](screenshots/database2.png)

### One-to-Many Relationship (1:N)

The database that I have created uses a **one-to-many relationship** between the `kunder` (customers) and `bestillinger` (orders) tables.

This means that one customer can in theory have multiple orders but each order will belong only to one customer.

The tables are connected through `kunde_id` which is the **primary key (PK)** in `kunder` and the **foreign key (FK)** in `bestillinger`.
![SQLite Installation](screenshots/relasjonsdiagram.png)


