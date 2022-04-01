def main():
    #your code goes here
    number = int(input("Enter a Number:"))
    if (number % 2) == 0:
      print("2")
    elif (number % 3) == 0:
      print("fizz")
    elif (number % 4) == 0:
      print("4")
    elif (number % 5) == 0:
      print("buzz")
    elif (number % 3 and number % 5) == 0:
      print("fizzbuzz")
    else:
      print(number)
if __name__ =='__main__':
    main()
