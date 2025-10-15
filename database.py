# Imports
import sqlite3

# Satellite System Database
conn = sqlite3.connect('satellite_system.db')

# Create a cursor
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")  # Enables foreign keys to enforce relationships between tables

# Create Users table
c.execute("""CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,             
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )""")

# Create Sessions table
c.execute("""CREATE TABLE IF NOT EXISTS Sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        token TEXT NOT NULL UNIQUE,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        expires_at TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    )""")

# Create Satellites table
c.execute("""CREATE TABLE IF NOT EXISTS Satellites (
        norad_id INTEGER PRIMARY KEY,
        satellite_name TEXT NOT NULL,
        satellite_type TEXT
    )""")

# Create TLE_Data table
c.execute("""CREATE TABLE IF NOT EXISTS TLE_Data (
        tle_id INTEGER PRIMARY KEY AUTOINCREMENT,
        norad_id INTEGER NOT NULL,
        tle_line1 TEXT NOT NULL,
        tle_line2 TEXT NOT NULL,
        orbit_type TEXT,
        inclination REAL,
        eccentricity REAL,
        mean_motion REAL,
        epoch_date TEXT NOT NULL,
        retrieved_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (norad_id) REFERENCES Satellites(norad_id)
    )""")

# Create Positional_Data table
c.execute("""CREATE TABLE IF NOT EXISTS Positional_Data (
        position_id INTEGER PRIMARY KEY AUTOINCREMENT,
        norad_id INTEGER NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        altitude REAL NOT NULL,
        velocity REAL NOT NULL,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (norad_id) REFERENCES Satellites(norad_id)
    )""")

# Create User_Favourites table
c.execute("""CREATE TABLE IF NOT EXISTS User_Favourites (
        favourite_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        norad_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (norad_id) REFERENCES Satellites(norad_id),
        UNIQUE(user_id, norad_id)
    )""")

# Commit our commands
conn.commit()

# Close connection
conn.close()

print("Database initialized successfully!")
