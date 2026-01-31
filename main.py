import engine
import ac
import lock
import radio

def main():
    print("Life Engine v0.3 — Application Control")
    print("1. Engine")
    print("2. AC")
    print("3. Lock")
    print("4. Radio")
    print("q. Quit\n")

    while True:
        choice = input("Select option: ").strip().lower()

        if choice == "1":
            engine.toggle_engine()

        elif choice == "2":
            ac.toggle_ac()

        elif choice == "3":
            lock.toggle_lock()

        elif choice == "4":
            radio.toggle_radio()

        elif choice == "q":
            print("Exiting Life Engine App.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
