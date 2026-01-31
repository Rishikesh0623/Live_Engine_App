import state

def toggle_radio():
    if not state.ENGINE_ON:
        print("Cannot turn radio on. Engine is OFF.")
        return

    state.RADIO_ON = not state.RADIO_ON
    status = "ON" if state.RADIO_ON else "OFF"
    print(f"Radio turned {status}")