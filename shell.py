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
  else:
    print("You Typed:", user_input)
  

if (__name__=="__main__"):
 main()