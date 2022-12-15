import sys

from command import docs, createCommand


if __name__ == '__main__':
    args = sys.argv[1:]
    len_args = len(args)

    if len_args == 0:
        print(docs())
        sys.exit()

    cmd_name = args[0]
    cmd = createCommand(cmd_name)

    cmd.execute(*args[1:])
