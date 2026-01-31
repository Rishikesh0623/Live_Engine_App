import state

def toggle_ac():
    if not state.ENGINE_ON:
        print("Cannot turn AC on. Engine is OFF.")
        return

    state.AC_ON = not state.AC_ON
    status = "ON" if state.AC_ON else "OFF"
    print(f"AC turned {status}")