from file_operations import FileOperations
from system_operations import SystemOperations
from time_operations import TimeOperations

class UnixShell:
    def __init__(self):
        self.commands = {
            "list": FileOperations.list_files,
            "dirs": FileOperations.list_dirs,
            "date": TimeOperations.display_date,
            "ipconfig": SystemOperations.display_ipconfig,
            "pwd": SystemOperations.display_pwd,
            "clear": SystemOperations.clear_screen,
            "exit": exit
        }

    def run(self): #loop created to continuously run and execute commands
        while True:
            try:
                command = input("shell> ").strip().split() # to split input into command and arguments
                if not command:
                    continue # to skip if input is empty

                cmd = command[0]
                args = command[1:]

                if cmd in self.commands:
                    self.commands[cmd]()
                elif cmd == "cat" and len(args) == 1:
                    FileOperations.cat_file(args[0])
                elif cmd == "head" and len(args) == 2 and args[0] == "-5":
                    FileOperations.head_file(args[1])
                elif cmd == "tail" and len(args) == 2 and args[0] == "-5":
                    FileOperations.tail_file(args[1])
                elif cmd == "copy_file" and len(args) == 2:
                    FileOperations.copy_file(args[0], args[1])
                elif cmd == "remove_file" and len(args) == 1:
                    FileOperations.remove_file(args[0])
                elif cmd == "empty_file" and len(args) == 1:
                    FileOperations.empty_file(args[0])
                elif cmd == "time":
                    if len(args) == 1:
                        if args[0] == "-hours":
                            TimeOperations.display_time_hours()
                        elif args[0] == "-mins":
                            TimeOperations.display_time_minutes()
                        elif args[0] == "-secs":
                            TimeOperations.display_time_seconds()
                        else:
                            print(f"Invalid argument for time: {args[0]}")
                    else:
                        TimeOperations.display_time()
                else:
                    print(f"Invalid command: {cmd}")
            except Exception as e:
                print(f"Error: {e}")