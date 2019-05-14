from StateDeviceManager import StateDeviceManager
from State import States
from Notification import Notification


class Notifier:
    __device_state_list = []

    def __init__(self):
        for state in States:
            self.__device_state_list.append(StateDeviceManager(state))

    def send_message(self, notification: Notification, state: States):
        if notification.get_message() == 'EXIT':
            for state_device_manager in self.__device_state_list:
                state_device_manager.send_to_devices(notification)
        else:
            self.__device_state_list[state.value].send_to_devices(notification)

    def add_device(self, device, state):
        self.__device_state_list[state.value].add_device(device)

    def delete_device(self, device, state):
        self.__device_state_list[state.value].delete_device(device)



