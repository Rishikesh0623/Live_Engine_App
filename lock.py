import state

def toggle_lock():
    state.LOCKED = not state.LOCKED
    status = "LOCKED" if state.LOCKED else "UNLOCKED"
    print(f"Car is now {status}")
