# Satellite Tracking System

## Overview
This is a Python-based satellite tracking system with user authentication and a SQLite database for managing satellite data, user accounts, and tracking information. The application features password validation, bcrypt hashing for security, and a comprehensive database schema for satellite orbital data.

**Current State**: Console-based application with login functionality and database initialization. The application is functional and ready for further development.

## Recent Changes (October 15, 2025)
- Fixed circular import issues between UI.py, hashing.py, and database.py
- Refactored hashing.py to use function-based approach instead of module-level execution
- Updated database.py to use "CREATE TABLE IF NOT EXISTS" for better reusability
- Installed Python 3.11 and bcrypt package
- Added .gitignore for Python projects
- Configured workflow for console application

## Project Architecture

### File Structure
- `UI.py` - Main entry point with login interface and password validation
- `hashing.py` - Password hashing utilities using bcrypt
- `database.py` - Database initialization script
- `satellite_system.db` - SQLite database for satellite tracking data
- `system.db` - Legacy database file (exists but not actively used)

### Database Schema
The application uses SQLite with the following tables:
- **Users**: User authentication (user_id, username, password_hash)
- **Sessions**: User session management with tokens
- **Satellites**: Satellite information (NORAD ID, name, type)
- **TLE_Data**: Two-Line Element orbital data
- **Positional_Data**: Real-time satellite position tracking
- **User_Favourites**: User's favorite satellites

### Key Features
- Password validation (min 8 chars, uppercase, lowercase, digit, special character)
- Bcrypt password hashing for security
- SQLite database with foreign key constraints
- User authentication system (planned)

### Dependencies
- Python 3.11
- bcrypt (for password hashing)
- sqlite3 (built-in)

### Running the Application
The application runs via the "Satellite System" workflow which executes `python UI.py`. Users can interact through the console to:
1. Enter username and password
2. Password is validated against security requirements
3. Valid passwords are hashed using bcrypt

## Development Notes
- The application is a console-based TUI (Text User Interface)
- Database schema supports future features like satellite tracking, TLE data storage, and user favorites
- Password hashing uses bcrypt with automatic salt generation
- The codebase was refactored to eliminate circular imports between modules
