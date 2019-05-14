from Notification import Notification
from Device import Device

class StateDeviceManager:
    def __init__(self, State):
        self.__devices = []
        self.__state = State

    def add_device(self, device: Device):
        self.__devices.append(device)

    def delete_device(self, number):
        del self.__devices[number]

    def send_to_devices(self, notification: Notification):
        f = open("legitnetwork.txt", "w")
        f.write(self.__state.name + ' ' + notification.get_message())
        f.close()
