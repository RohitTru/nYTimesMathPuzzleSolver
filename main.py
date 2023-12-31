
from itertools import permutations, product

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
    thePermutations = list(permutations(numbers))

    # Our final variable
    result = None

    for perm in thePermutations:
        for ops in product(operators, repeat=(len(numbers)-1)):
            expression = str(perm[0])
            for i in range(1, len(numbers)):
                expression+= ops[i-1] + str(perm[i])
            
            try:
                if eval(expression) == target:
                    result = expression
                    print(result)
                    break
            except ZeroDivisionError:
                pass
    if result:
        print("This is the answer " + result + " = " + str(int(eval(expression))))
    else:
        print("No expression found.")
   
def main():
    introduction()
    getInput()
    solvePuzzle()
    

if __name__ == "__main__":
    main()