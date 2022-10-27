import sys
import datetime


def print_usage():
    info = '\nCommand Line Todo application\n=============================\nCommand line arguments:\n-l   Lists all ' \
           'the tasks\n-a   Adds a new task\n-r   Removes a task\n-c   Completer a task '

    sys.stdout.write(info)


def list_tasks():
    with open("list_of_tasks.txt", 'r') as fobj:
        fobj_content = fobj.readlines()
        if len(fobj_content) == 0:
            sys.stdout.write('No todos for today! :)')

        else:
            task_num = 1
            for line in fobj_content:
                sys.stdout.write(f'{task_num} - {line}')
                task_num += 1


def add_new_task(task=''):
    if task == '':
        sys.stderr.write('Unable to add: no task provided')
    else:
        with open("list_of_tasks.txt", "a") as fobj:
            fobj.write('\n' + str(task))
            sys.stdout.write(f'New task: {task} has been added')


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print_usage()

    elif args[1] == '-l':
        list_tasks()

    elif args[1] == '-a':
        try:
            add_new_task(args[2])

        except IndexError:
            add_new_task()

