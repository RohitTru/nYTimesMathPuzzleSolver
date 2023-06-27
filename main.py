
def Introduction():
    print("Hi and welcome to the NYTIMES' Math Puzzle Solver")

numbers = []

def getNumbers():
    i = 0
    
    print("Please enter your 6 integers: ")

    while i < 6:
        i += 1
        numbers.append(int(input()))
    
    return(numbers)




















if __name__ == "__main__":
    Introduction()
    getNumbers()