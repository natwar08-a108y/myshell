import shlex
import sys
import os

def main():
    prev_dir = None
    while True:
        try:
            user_input = input("myshell> ")
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue
            
        user_input = user_input.strip()
        if not user_input:
            continue
            
        try:
            tokens = shlex.split(user_input)
        except ValueError:
            print("myshell: syntax error: unmatched quote")
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
                print("cd: too many arguments")
                continue
                
            if len(args) == 0:
                target = "~"
            else:
                target = args[0]
                
            if target == "-":
                if prev_dir is None:
                    print("cd: OLDPWD not set")
                    continue
                target = prev_dir
                print(target)
                
            target = os.path.expanduser(target)
            current_dir = os.getcwd()
            
            try:
                os.chdir(target)
                prev_dir = current_dir
                print("Current working directory:", os.getcwd())
            except FileNotFoundError:
                print("cd: no such file or directory: " + target)
            except NotADirectoryError:
                print("cd: not a directory: " + target)
            except PermissionError:
                print("cd: permission denied: " + target)
                
        print("Command:", command)
        print("Arguments:", args)
        

if __name__ == "__main__":
    main()
