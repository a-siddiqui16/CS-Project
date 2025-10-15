# 🌍 Satellite Tracking System — Functional Requirements

A real-time **3D satellite visualization platform** with user authentication, live positional data, filtering, and favourites management.

---

## 🔐 1. Login & Authentication

<details>
<summary><b>📥 Login Page</b></summary>

- [ ] The system must allow users to **log in** using a username and password.  
- [ ] The system must allow users to **register** if they don’t have an account, and store credentials securely in a database.  

**Password Requirements:**
- [ ] Passwords must be **at least 8 characters long**.  
- [ ] Passwords must include a **mix of symbols, numbers, and letters**.  

</details>

<details>
<summary><b>🧩 Session Management</b></summary>

- [ ] The system must create a **unique, securely generated session token** for each login.  
- [ ] The system must store:
  - Token **creation time**
  - Token **expiry time**
- [ ] Sessions must **automatically expire after 30 minutes**.  
- [ ] Once expired, users must **log in again** to regain access.  
- [ ] The system must allow users to **log out manually**, deleting their active session.  

</details>

---

## 🌐 2. 3D Earth Representation

<details>
<summary><b>🌎 3D Earth Model</b></summary>

- [ ] The system must render a **3D Earth** model accurately showing all **seven continents** and **surrounding oceans**.  
- [ ] The background must be **black**, representing space.  

**User Interaction:**
- [ ] Users can **rotate** the Earth in any direction.  
- [ ] Users can **zoom in/out** using **mouse** or **keyboard** controls.  

</details>

---

## 🛰️ 3. Satellite Representation & Tracking

<details>
<summary><b>📡 Satellite Display</b></summary>

- [ ] The system must display satellites in orbit around the 3D Earth.  
- [ ] Users can **interact** with satellite markers.  

**Tracking:**
- [ ] Satellites must be tracked using **positional data**.  
- [ ] The system must update positions **at least once every 3 seconds** for near real-time tracking.  
- [ ] The system must display:
  - **NORAD ID**
  - **Velocity**
  - **Altitude**
  - **Latitude**
  - **Longitude**

</details>

---

## 🌀 4. Orbit Trajectory Visualization

<details>
<summary><b>🧭 Orbit Paths</b></summary>

- [ ] The system must display the **orbit trajectory** of each satellite.  
- [ ] When a satellite is selected, a **trail** should appear showing its orbital path on the 3D Earth.  

</details>

---

## 🔍 5. Satellite Filtering

<details>
<summary><b>🎯 Search & Filter</b></summary>

- [ ] The system must allow users to **filter satellites by type**.  
- [ ] A **search box** must be available, returning results within **2 seconds**.  
- [ ] The user must be able to search by **satellite name** or **NORAD ID**.  

</details>

---

## ⭐ 6. Favourite Satellites

<details>
<summary><b>💫 Favourites Management</b></summary>

- [ ] Users must be able to **mark satellites as favourites**.  
- [ ] Favourite satellites must be **stored in the database**.  
- [ ] The system must **automatically display favourites** on the 3D Earth model.  
- [ ] Users can **add or remove** satellites from their favourites list at any time.  

</details>

---

### ✅ Example README Header
```markdown
# Satellite Tracking System
A real-time 3D satellite visualization platform with user authentication, filtering, and custom satellite tracking features.
