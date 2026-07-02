import subprocess
import pgconnect

conn = pgconnect.connect_db("escape_room_db")
cur = conn.cursor()

TOTAL_ROOMS = 100  

def start_room(room):
    try:
        room_script_path = f'rooms/room{room}.py'
        with open(room_script_path, 'r') as file:
            room_script_content = file.read()
            exec(room_script_content)
        print(f"Room {room} completed!")
    except FileNotFoundError:
        print(f"ERROR: Room {room} not found!")
    except Exception as e:
        print(f"ERROR: Room {room} failed to execute. Error: {e}")



def start_game():
    print("\nWelcome to Escape Room Beta!!\n")

    room_sequence = [str(i) for i in range(1, TOTAL_ROOMS + 1)]

    start_map = input(f"Start Map with {TOTAL_ROOMS} rooms? (y/n): ").lower() == 'y'
    if start_map:
        cur.execute("UPDATE rooms SET is_completed=false")
        for index, room in enumerate(room_sequence, start=1):
            start_room(room)
            if index < len(room_sequence):
                move_next = input("Move to the next room? (y/n): ").lower() == 'y'
                if not move_next:
                    print("Goodbye!")
                    break
            else:
                print("Congratulations! You've completed the entire story!")
                break
    else:
        print("Goodbye!")

if __name__ == "__main__":
    start_game()
