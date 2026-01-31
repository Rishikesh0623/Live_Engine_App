"""
lock.py
Controls door locking and unlocking.

Rules:
- Lock and unlock can work independently of engine state
- Can be used even when the engine is OFF

Represents security-related functionality.
"""

import state

def toggle_lock():
    state.LOCKED = not state.LOCKED
    status = "LOCKED" if state.LOCKED else "UNLOCKED"
    print(f"Car is now {status}")