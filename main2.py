from rooms.room import Room

room1 = Room('001', "The mysterious study", "You are in a dimly lit room, with an ancient wooden desk and a large metal safe attached against the wall.")

room1.add_item("desk key", "A rusty old brass key lying on the floor.")
#room1.add_item("note", f"A piece of paper with the code: {room1.PIN}")
#room1.add_item("key", "A shiny metal key hidden in the safe.")

room1.add_locked_object("desk drawer", "desk key", "Desk drawer unlocked.", "note")
room1.add_locked_object("safe", "note", "Safe unlocked.", "key")
room1.add_locked_object("main door", "key", "Unlocked main door.", "")

inventory = []


while not room1.unlocked:
    room1.describe()
    action = input("What would you like to do? (pick/use/quit): ").strip().lower()
    
    if action == 'pick':
        item = input("Which item would you like to pick up? ").strip().lower()
        if item in inventory:
            print(f"You already picked up {item}.")
        elif item in room1.items:
            inventory.append(item)
            print(f"You picked up {item}.")
            del room1.items[item]
        else:
            print(f"That item isn't here.")
                 
        
    if action == 'use':
        item = input("Which item would you like to use? ").strip().lower()
        if item in inventory:
            print("Which object would you like to interact with?")
            for locked_object in room1.locked_objects:
                print(f"- {locked_object.name}")
            target = input("Choose your object: ").strip().lower()           
            room1.interact(target, item)
        else:
            print(f"You don't have that item.")
    

    if action == 'quit':
        print("Game over!")
        break


    if room1.check_unlocked():
        print("Congratulations!! You have unlocked all the objects and escaped the room! 🎉")
#