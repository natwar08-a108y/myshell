import shlex
def main():
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
  print("Command:", command)
  print("Arguments:", args)
  

if __name__=="__main__":
 main()