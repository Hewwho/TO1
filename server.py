from Notifier import Notifier
from State import States
from Notification import Notification

notifier = Notifier()


def main():
    notification = Notification()
    command = input()

    while command.split(' ')[0] != 'EXIT':

        if command.split(' ')[0] == 'SEND':
            notification.set_message(command.split(' ', 2)[2])
            notification.set_state(States[command.split(' ')[1]])
            notifier.send_message(notification, States[command.split(' ')[1]])

        command = input()

    notification.set_message(command)
    notifier.send_message(notification, 0)
    open("legitnetwork.txt", "w").close()


main()
