import sys
import datetime


def print_usage():
    info = '\nCommand Line Todo application\n' \
           '=============================\n' \
           'Command line arguments:\n' \
           '-l   Lists all the tasks\n' \
           '-a   Adds a new task\n' \
           '-r   Removes a task\n' \
           '-c   Completer a task'

    sys.stdout.write(info.encode('utf8'))


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 0:
        print_usage()
