import random
from rooms.locked_object import LockedObject

class Room():
    def __init__(self, room_no, name, description):
        self.room_no = room_no
        self.name = name
        self.description = description
        self.main_door_locked = True
        self.PIN = f"{random.randint(0, 9999):04d}"
        self.items = {}
        self.locked_objects = []
        self.unlocked = []

    def describe(self):
        print(f"\nRoom Number {self.room_no}: {self.name}")
        print(self.description)
        if self.items:
            print("\nYou see the following items:")
            for item in self.items:
                print(f"- {item}")
        if not self.unlocked:
            print("\nThe main door is locked. You must solve puzzles to escape.\n")

    def add_item(self, name, description):
        self.items[name] = description

    def add_locked_object(self, name, required_item, success_msg, result_item):
        new_locked_object = LockedObject(name, required_item, success_msg, result_item)
        self.locked_objects.append(new_locked_object)

    def select_locked_object(self, object_name):
        for obj in self.locked_objects:
            if obj.name == object_name:
                return obj

    def interact(self, object_name, item_used):
        if object_name in [obj.name for obj in self.locked_objects]:
            lock = self.select_locked_object(object_name)
            if (lock.required_item == item_used) and not (lock.unlocked):
                lock.unlocked = True
                print(lock.success_msg)
                self.add_item(lock.result_item, "")  
                self.unlocked.append(lock)
                print(f"Now you have the {lock.result_item}")
                if lock.result_item == 'main_key':
                    self.main_door_locked = False
                    print("The main door is now unlocked!")
            elif lock.unlocked:
                 print(f"{object_name.capitalize()} has already been unlocked") 
            else:
                print(f"Item {item_used} doesn't seem to work on {object_name}.")
        else:
            print(f"There is no {object_name} to interact with.")

    def check_unlocked(self):
        self.main_door_locked = not all(obj.unlocked for obj in self.locked_objects)
        return not self.main_door_locked

