
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
        while True:
            numberInput = input(f'Enter #{str(i)}\n')

            if numberInput.isdigit():
                numberInput = int(numberInput)
                numbers.append(numberInput)
                break
            else:
                print('NOT A DIGIT')
    
    print("Please enter the Target value: ")

    while True:     
        targetInput = input("Enter Target #\n")
        
        if targetInput.isdigit():
            target = int(targetInput)
            break
    
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
        




def main():
    #introduction()
    getNumbers()
    checkValues()



if __name__ == "__main__":
    main()