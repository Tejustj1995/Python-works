while True:
    print("\n 1. Rock \n 2. paper \n 3. scissor \n")

    choice = int(input("User 1: "))
    if choice == 1:
        name = 'Rock'
    elif choice == 2:
        name = 'paper'
    elif choice == 3:
        name = 'scissor'
    else:
        print("invalid choice")
        break
    print("user 1 choice is: " + name)
    choice1 = int(input("User 2: "))
    if choice1 == 1:
        name1 = 'Rock'
    elif choice1 == 2:
        name1 = 'paper'
    elif choice1 == 3:
        name1 = 'scissor'
    else:
        print("invalid choice")
        break
    print("user 2 choice is: " + name1)

    print(name + " Versus " + name1)

    if (choice == 1 and choice1 == 2) or (choice == 2 and choice1 == 1):
        print("paper wins ", end="")
        winner = "paper"
    elif (choice == 1 and choice1 == 3) or (choice == 3 and choice1 == 1):
        print("Rock wins ", end="")
        winner = "Rock"
    elif (choice == 2 and choice1 == 3) or (choice == 3 and choice1 == 2):
        print("scissor wins ", end="")
        winner = "scissor"
    elif (choice == 1 and choice1 == 1) or (choice == 2 and choice1 == 2) or (choice == 3 and choice1 == 3):
        print("***************DRAW**************", end="")
        winner = ""
    else:
        print('invalid')

    if winner == name:
        print("\n User 1 wins\n")
    elif winner == name1:
        print("\nUser 2 wins\n")
    else:
        print("\n****its a tie****")
    ans = input("do u want to continue(Y/N)")
    if ans == "N" or ans == "n":
        break
