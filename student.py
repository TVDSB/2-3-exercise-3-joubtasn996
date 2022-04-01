def main():
    #your code goes here
    number = int(input("Enter a Number:"))
    if (number % 2) == 0:
      print("2")
    elif (number % 3) == 0:
      print("Fizz")
    elif (number % 4) == 0:
      print("4")
    elif (number % 5) == 0:
      print("Buzz")
    elif (number % 5 and number % 3) == 0:
      print("BuzzFizz")
    else:
      print(number)

if __name__ =='__main__':
    main()
