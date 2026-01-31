import state

def toggle_engine():
    state.ENGINE_ON = not state.ENGINE_ON
    status = "ON" if state.ENGINE_ON else "OFF"
    print(f"Engine turned {status}")