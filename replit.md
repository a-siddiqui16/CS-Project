# Satellite Tracking System

## Overview

A real-time 3D satellite visualization platform that combines interactive Earth rendering with satellite tracking capabilities. The system provides user authentication, live satellite positional data from Celestrak, filtering options, and favorites management. Built using VPython for 3D visualization, Tkinter for UI components, and SQLite for data persistence.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**UI Framework: Tkinter**
- Chosen for its native Python integration and simplicity for desktop applications
- Handles login/registration forms with built-in validation
- Lightweight solution suitable for the system's requirements without web framework overhead

**3D Visualization: VPython**
- Selected for real-time 3D satellite tracking and Earth rendering
- Provides built-in physics simulation and interactive 3D canvas
- Native support for textures (Earth texture) and space backgrounds
- Handles user interaction (rotation, zoom) through mouse and keyboard controls
- Runs at 60 FPS for smooth visualization

**Design Decision**: Desktop application rather than web-based
- Pros: Better 3D performance, simpler deployment, no browser compatibility issues
- Cons: Platform-specific builds required, limited accessibility compared to web

### Backend Architecture

**Database: SQLite**
- Lightweight, serverless database embedded directly in the application
- No separate database server required - suitable for single-user or small-scale deployments
- Schema includes:
  - Users table: Authentication credentials with unique usernames
  - Sessions table: Token-based session management with timestamps
  - Satellites table: Core satellite metadata (NORAD ID, name, type)
  - TLE_Data table: Two-Line Element sets with orbital parameters
  - Positional_Data table: (Implementation pending) Real-time position calculations

**Security: Bcrypt Password Hashing**
- Industry-standard password hashing with automatic salt generation
- Passwords hashed before storage, never stored in plaintext
- Verification uses constant-time comparison to prevent timing attacks

**Session Management**
- Token-based authentication system
- 30-minute automatic expiration enforced at database level
- Manual logout capability with session deletion
- Foreign key constraints ensure data integrity between users and sessions

**Password Validation**
- Minimum 8 characters required
- Enforces complexity: uppercase, lowercase, numbers, special characters
- Client-side validation with clear error messaging

### Data Flow

**Satellite Data Retrieval**
- External API integration with Celestrak (celestrak.org)
- Fetches TLE (Two-Line Element) data by NORAD ID
- Parses response into three components: name, line 1, line 2
- Stores orbital parameters: inclination, eccentricity, mean motion, epoch date
- Architecture allows for periodic updates (implementation pending)

**Authentication Flow**
1. User submits credentials via Tkinter form
2. Username lookup in SQLite database
3. Bcrypt verification against stored hash
4. Session token generation and storage with expiration timestamp
5. Token validation for subsequent requests

## External Dependencies

### Third-Party Services

**Celestrak Satellite Database**
- Purpose: Real-time TLE data provider for satellite tracking
- API Endpoint: `https://celestrak.org/NORAD/elements/gp.php`
- Query Parameter: NORAD catalog number (CATNR)
- Response Format: Plain text TLE format (3 lines)
- No authentication required for basic queries

### Python Libraries

**bcrypt**
- Purpose: Cryptographic password hashing
- Used for: Secure password storage and verification
- Provides: Salt generation, hash computation, constant-time comparison

**requests**
- Purpose: HTTP client for API communication
- Used for: Fetching TLE data from Celestrak
- Handles: GET requests, status code validation, response parsing

**VPython (vpython)**
- Purpose: 3D graphics and physics simulation
- Used for: Earth model rendering, satellite visualization, user interaction
- Provides: Canvas, sphere objects, textures, animation loop

**tkinter**
- Purpose: GUI framework (Python standard library)
- Used for: Login/registration forms, message boxes, input validation
- Native Python library - no external installation required

**sqlite3**
- Purpose: Database interface (Python standard library)
- Used for: User data, session management, satellite information storage
- Native Python library - embedded database solution

### Database Schema Relationships

- Foreign key enforcement enabled (`PRAGMA foreign_keys = ON`)
- Sessions linked to Users via `user_id` foreign key
- TLE_Data linked to Satellites via `norad_id` foreign key
- Automatic timestamps for session creation and TLE retrieval
- Cascade behavior to be defined for user/session deletions