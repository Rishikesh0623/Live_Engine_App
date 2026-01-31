# 🚗 Live Engine App

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Stable-green)
![Architecture](https://img.shields.io/badge/Architecture-Modular-brightgreen)
![Learning](https://img.shields.io/badge/Purpose-System%20Design-informational)

**Live Engine App** is a modular Python application that simulates a real-world vehicle control system.  
It models how independent subsystems (engine, AC, locks, radio) interact through shared state and enforced rules.

This project focuses on **system design**, **clean architecture**, and **separation of concerns**, rather than UI or frameworks.

---

## 🎯 Purpose

The goal of this project is to:

- Learn how to design **modular systems**
- Model **real-world dependencies** (e.g. AC requires engine ON)
- Separate **UI logic**, **business logic**, and **state**
- Build a foundation suitable for:
  - IoT systems
  - Embedded controllers
  - Mobile / web applications
  - Game engines (turn-based or state-driven)

This is a **logic-first** project.

---

## 🧠 Conceptual Overview

Think of this app as a **vehicle control console**:

- Each car feature is its own module
- All modules share a single source of truth (`state.py`)
- The main app only coordinates user actions
- Rules are enforced at the module level, not globally

This mirrors how real production systems are designed.

---
## 📁 Project Structure
```tree
live_engine_app/
├── main.py        # App coordinator (UI → logic)
├── engine.py      # Car engine control
├── ac.py          # AC control (depends on engine state)
├── lock.py        # Door lock control (independent)
├── radio.py       # Radio control (depends on engine state)
└── state.py       # Shared system state (single source of truth)
```


---

## 🧩 Module Responsibilities

### `main.py`
- Entry point of the application
- Handles user input and command routing
- Does **not** contain business logic

### `engine.py`
- Starts and stops the engine
- Acts as the primary dependency for other modules

### `ac.py`
- Controls air conditioning
- Can only operate when engine is running

### `lock.py`
- Locks and unlocks the car
- Operates independently of engine state

### `radio.py`
- Controls radio system
- Requires engine to be running

### `state.py`
- Centralized application state
- Tracks:
  - Engine status
  - AC status
  - Lock status
  - Radio status
  - Runtime information

---

## 🕹️ How to Run

### Requirements
- Python **3.10+**

### Start the app
- python main.py

---

🚀 Version History
v0.1

Basic system info

Single runtime loop

v0.2

Multi-user session control

Engine lifecycle management

v0.3 (Current)

Feature-based modular architecture

Independent subsystems

Shared state management

Application-level control model

---

🔮 Future Extensions (Optional)

Hardware integration (Arduino / Raspberry Pi)

REST API or WebSocket control

Mobile UI (Android / Kotlin)

Persistent state storage

Game engine reuse (e.g. Monopoly simulation)

----
👤 Author

Rishikesh (Rishi)
Learning by building systems, not copying code.
