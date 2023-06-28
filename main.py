
from itertools import permutations

numbers = []
target = 0
validation = 'a'
userVal = False

def introduction():
    print("Hi and welcome to the NYTIMES' Math Puzzle Solver")

def getNumbers():
    i = 0
    global target
    global numbers

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

def getInput():
    while userVal == False:
        getNumbers()
        getCheck()
        if userVal == True:
            break   


def solvePuzzle():
    operators = ['+', '-', '*', '/']
    perms = list(permutations(numbers))
    print(perms) 




            
    




def main():
    introduction()
    getInput()
    solvePuzzle()
    
    



if __name__ == "__main__":
    main()