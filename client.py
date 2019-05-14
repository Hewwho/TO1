from Citizen import Citizen
from Device import Device
from State import States
from Notifier import Notifier


def main():

    citizen = Citizen(13, "Jan", "Kowalski")

    device_data = input("name, number, state: ")

    device = Device(device_data.split(' ')[0], device_data.split(' ')[1], States[device_data.split(' ')[2]], citizen)
    notifier = Notifier()
    notifier.add_device(device, device.get_state())

    f = open("legitnetwork.txt", "r")

    message = f.read()

    last_message = None

    while not message or message.split(' ')[1] != 'EXIT':
        if message and message.split(' ')[0] == device.get_state().name and last_message != message.split(' ', 1)[1]:
            print(message.split(' ', 1)[1])
            last_message = message.split(' ', 1)[1]

        f.seek(0)
        message = f.read()

    f.close()


main()
