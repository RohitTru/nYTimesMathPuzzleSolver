
numbers = []
target = 0
validation = 'a'
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
    userResponse = True
    
    print(f'Are your values:  {numbers} and target value: {target} correct? (Enter "y" or "n")')
    
    while True:
        userResponse = input()

        if userResponse == 'y':
            userResponse = True
            break

        if userResponse == 'n':
            userResponse = False
            break
    
    if userResponse == True:
        pass
    if userResponse == False:
        getNumbers() # This doesnt work




def main():
    #introduction()
    getNumbers()
    checkValues()



if __name__ == "__main__":
    main()