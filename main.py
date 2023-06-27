
numbers = []
target = 0

def introduction():
    print("Hi and welcome to the NYTIMES' Math Puzzle Solver")

def getNumbers():
    i = 0
    global target

    print("Please enter your 6 integers: ")
    while i < 6:
        i += 1
        numbers.append(int(input()))
    
    print("Please enter the Target value: ")
     
    target = int(input())
    
    return(numbers, target)

def checkValues():
    print(f'Are your values:  {numbers} and target value: {target} correct? (Enter "y" or "n")')
    userResponse = input()













def main():
    #introduction()
    getNumbers()
    checkValues()










if __name__ == "__main__":
    main()