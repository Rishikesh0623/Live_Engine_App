"""
radio.py
Controls the car radio system.

Rules:
- Radio can only be turned ON if the engine is running
- Radio turns OFF automatically when the engine stops

Uses shared state to check engine availability.
"""

import state

def toggle_radio():
    if not state.ENGINE_ON:
        print("Cannot turn radio on. Engine is OFF.")
        return

    state.RADIO_ON = not state.RADIO_ON
    status = "ON" if state.RADIO_ON else "OFF"
    print(f"Radio turned {status}")