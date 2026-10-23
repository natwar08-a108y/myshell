import shlex
import sys
import shlex
import sys
import os
import subprocess

def main():
    prev_dir = None
    last_status = 0
    while True:
        try:
            cwd = os.getcwd()
        except FileNotFoundError:
            print("myshell: current directory has been deleted; defaulting to /")
            os.chdir("/")
            cwd = "/"

        home = os.path.expanduser("~")
        if cwd == home:
            cwd = "~"
        elif cwd.startswith(home + os.sep):
            cwd = "~" + cwd[len(home):]
        prompt = "myshell:" + cwd + "$ "

        try:
            user_input = input(prompt)
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            last_status = 130
            continue

        user_input = user_input.strip()
        if not user_input:
            continue

        try:
            tokens = shlex.split(user_input)
        except ValueError:
            print("myshell: syntax error: unmatched quote")
            last_status = 2
            continue

        if not tokens:
            continue

        command = tokens[0]
        args = tokens[1:]

        if command == "exit":
            exit_code = 0  
            if len(args) >= 1:
                try:
                    exit_code = int(args[0])
                except ValueError:
                    print("myshell: exit: numeric argument required")
                    exit_code = 2  
            sys.exit(exit_code)

        elif command == "cd":
            if len(args) > 1:
                print("myshell: cd: too many arguments")
                last_status = 1
                continue

            if len(args) == 0:
                target = "~"
            else:
                target = args[0]

            if target == "-":
                if prev_dir is None:
                    print("myshell: cd: OLDPWD not set")
                    last_status = 1
                    continue
                target = prev_dir
                print(target)

            target = os.path.expanduser(target)
            current_dir = os.getcwd()

            try:
                os.chdir(target)
                prev_dir = current_dir
                last_status = 0
            except FileNotFoundError:
                print("myshell: cd: no such file or directory: " + target)
                last_status = 1
            except NotADirectoryError:
                print("myshell: cd: not a directory: " + target)
                last_status = 1
            except PermissionError:
                print("myshell: cd: permission denied: " + target)
                last_status = 1

        else:
            try:
                result = subprocess.run(tokens)
                last_status = result.returncode
            except FileNotFoundError:
                print("myshell: command not found: " + command)
                last_status = 127
            except PermissionError:
                print("myshell: permission denied: " + command)
                last_status = 126
            except KeyboardInterrupt:
                print()  
                last_status = 130

if __name__ == "__main__":
    main()