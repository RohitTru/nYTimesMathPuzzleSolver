
numbers = []
target = 0
validation = 'a'
userVal = True

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


def getCheck():
    global userVal

    print(f'Are your values:  {numbers} and target value: {target} correct? (Enter "y" or "n")')
    
    while True:
        userVal = input()        
        if userVal == 'y':
            userVal = True
            break

        if userVal == 'n':
            userVal = False
            break

    return(userVal)




            
    




def main():
    #introduction()
    getNumbers()
    getCheck()
    print(userVal)



if __name__ == "__main__":
    main()