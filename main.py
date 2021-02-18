import commandHandler
import time

if __name__ == '__main__':
    while True:
        command = commandHandler.listen_command()
        commandHandler.do_this_command(command)
