import random
def play_human_turn(n):
    # 1. prompt user for their move
    user_move = int(input("Enter a number of coins to remove (1-3 coins): "))
    
    while (user_move < 1 or user_move > 3):
        user_move = int(input("Enter a valid number of coins to remove (1-3 coins): "))
    n -= user_move

    # 2. output number of coins after user's move
    print("There are " + str(n) + " coins on the table.")

    # 3. If the human wins, indicate that and return 0
    if (n == 0):
        print("You win!")
    return n 

    # You must implement this function
    pass

def play_computer_turn(n):
    # 1. Make computer move
    if (n % 4 == 0):
        computer_move = random.randint(1,3)
        n -= computer_move
    else: 
        while (n % 4 != 0):
            n -= 1    
 
    # 2. If computer wins, indicate that and return 0
    if (n == 0):
        print("computer wins!")

    # 3. return number of coins remaining    
    return n   
                         
    # You must implement this function 
    pass
