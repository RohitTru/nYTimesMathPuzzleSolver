
def introduction():
    print("Hi and welcome to the NYTIMES' Math Puzzle Solver")


numbers = []

def getNumbers():
    i = 0
    
    print("Please enter your 6 integers: ")
    while i < 6:
        i += 1
        numbers.append(int(input()))
    
    print("Please enter the Target value: ")
    global target 
    target = input()
    
    return(numbers, target)

        









def main():
    introduction()
    getNumbers()

    print(numbers)
    print(target)










if __name__ == "__main__":
    main()