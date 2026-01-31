"""
engine.py
Controls the car engine.

Responsibilities:
- Start the engine
- Stop the engine
- Update shared state when engine status changes

Other modules (AC, Radio) depend on engine state.
"""

import state

def toggle_engine():
    state.ENGINE_ON = not state.ENGINE_ON
    status = "ON" if state.ENGINE_ON else "OFF"
    print(f"Engine turned {status}")