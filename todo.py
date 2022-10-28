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


# saves the tasks in the list_of_tasks.txt file into a list variable
def task_list():
    with open("list_of_tasks.txt", 'r') as fobj:
        task_list = fobj.readlines()
        return task_list


def remove_task(index=0):
    task_ls = task_list()
    sys.stdout.write(f'Task: {task_ls[index - 1]} has been deleted.')
    del task_ls[index - 1]
    with open("list_of_tasks.txt", "w") as fobj:
        for task in task_ls:
            fobj.write(task)


if __name__ == '__main__':
    args = sys.argv
    valid_args = ['-l', '-a', '-r', 'c']

    if len(args) == 1:
        print_usage()

    elif args[1] not in valid_args:
        sys.stderr.write('\nUnsupported argument\n')
        print_usage()

    elif args[1] == '-l':
        list_tasks()

    elif args[1] == '-a':
        try:
            add_new_task(args[2])

        except IndexError:
            add_new_task()

    elif args[1] == '-r':
        try:
            remove_task(int(args[2]))
        except ValueError:
            sys.stderr.write("Unable to remove: index is not a number")
        except IndexError:
            if len(args) < 3:
                sys.stderr.write('Unable to remove: no index provided')
            elif int(args[2]) - 1 > len(task_list()):
                sys.stderr.write('Unable to remove: index is out of bound')
