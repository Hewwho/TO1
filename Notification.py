from State import States


class Notification:
    def __init__(self, message='', state=0):
        self.__message = message
        self.__to_state = state

    def set_message(self, message):
        self.__message = message

    def set_state(self, state: States):
        self.__to_state = state

    def get_message(self):
        return self.__message
