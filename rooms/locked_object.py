class LockedObject:
    def __init__(self, name, required_item, success_msg, result_item, description=None):
        self.name = name
        self.description = description
        self.required_item = required_item
        self.success_msg = success_msg
        self.result_item = result_item
        self.unlocked = False

    def describe(self):
        print(f"This is a {self.name}, Description: {self.description}")
    
    def get_required_item(self):
        return self.required_item
        

    