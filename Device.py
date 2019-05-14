class Device:
    def __init__(self, name, number, state, citizen):
        self.__name = name
        self.__number = number
        self.__state = state
        self.__owner = citizen

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_state(self):
        return self.__state
