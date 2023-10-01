class StateManager:

    def __init__(self):
        self.state = None

    def set_state(self, new_state):
        self.state = new_state

    def get_state(self):
        return self.state