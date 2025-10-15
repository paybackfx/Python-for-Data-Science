import sys
import string 

def count_chars(text: str) -> None:

    upper = lower =  digits = space = punct = 0
    for char in text:
        if(char.isupper()):
            upper += 1
        elif(char.islower()):
            lower += 1
        elif(char.isdigit()):
            digits += 1
        elif(char.isspace()):
            space += 1
        elif(char in string.punctuation):
            punct += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")

def main():
    try :
      if len(sys.argv) > 2 :
           raise AssertionError("more than one argument is provided")
      elif len(sys.argv) == 2 :
          count_chars(sys.argv[1])
      else :
          text = input("What is the text to analyze? ")
          count_chars(text)
    except AssertionError as e :
        print("AssertionError:", e)

if __name__ == "__main__":
    main()