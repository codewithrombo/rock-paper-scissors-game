import random

def game():
    score = 0
    computer_score = 0
    winning_score = 5
    while True:
        rps = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(rps)
        if score != 0 or computer_score != 0:
            print("\nYou have", score, "wins and computer has", computer_score, "wins.")
        if score == winning_score:
            print("GAME OVER. You win!\n")
            break
        if computer_score == winning_score:
            print("GAME OVER. You lose!\n")
            break

        user_action = input("\nChoose rock, paper or scissors: ")

        if user_action.lower() == "rock" and computer_action.lower() == "scissors":
            print("\nRock... Paper... Scissors!\n\nYou chose ROCK and computer chose SCISSORS. Rock crushes scissors, you win!")
            score += 1 
            continue
        
        elif user_action.lower() == "paper" and computer_action.lower() == "rock":
            print("\nRock... Paper... Scissors!\n\nYou chose PAPER and computer chose ROCK. Paper covers rock, you win!")
            score += 1
            continue

        elif user_action.lower() == "scissors" and computer_action.lower() == "paper":
            print("\nRock... Paper... Scissors!\n\nYou chose SCISSORS and computer chose PAPER. Scissors cuts paper, you win!")
            score += 1
            continue

        elif user_action.lower() == computer_action.lower():
            print("\nRock... Paper... Scissors!\n\nYou chose", computer_action.upper(), "and computer chose", computer_action.upper() + ". It is a tie!")
            continue

        else:
            if computer_action.lower() == "scissors" and user_action.lower() == "paper":
                print("\nRock... Paper... Scissors!\n\nYou chose", user_action.upper(), "and computer chose", computer_action.upper() + ". Scissors cuts paper, you lose!")
                computer_score += 1
            elif computer_action.lower() == "paper" and user_action.lower() == "rock":
                print("\nRock... Paper... Scissors!\n\nYou chose", user_action.upper(), "and computer chose", computer_action.upper() + ". Paper covers rock, you lose!")
                computer_score += 1
            elif computer_action.lower() == "rock" and user_action.lower() == "scissors":
                print("\nRock... Paper... Scissors!\n\nYou chose", user_action.upper(), "and computer chose", computer_action.upper() +". Rock crushes scissors, you lose!")
                computer_score += 1
            else:
                print("\nInvalid input. Please try again!\n")

def game_3():
    score = 0
    computer_score = 0
    max_score = 2
    while True:

        rps = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(rps)
        if score != 0 or computer_score != 0:
            print("\n\tYou have", score, "wins and computer has", computer_score, "wins.")
        if score == max_score:
            print("\nGAME OVER. You win!\n")
            break
        if computer_score == max_score:
            print("\nGAME OVER. You lose!\n")
            break

        user_action = input("\nChoose rock, paper or scissors: ")

        if user_action.lower() == "rock" and computer_action.lower() == "scissors":
            print("\nRock...\nPaper...\nScissors...\n\n[You chose ROCK and computer chose SCISSORS. Rock crushes scissors, you win!]")
            score += 1 
            continue
        
        elif user_action.lower() == "paper" and computer_action.lower() == "rock":
            print("\nRock...\nPaper...\nScissors...\n\n[You chose PAPER and computer chose ROCK. Paper covers rock, you win!]")
            score += 1
            continue

        elif user_action.lower() == "scissors" and computer_action.lower() == "paper":
            print("\nRock...\nPaper...\nScissors...\n\n[You chose SCISSORS and computer chose PAPER. Scissors cuts paper, you win!]")
            score += 1
            continue

        elif user_action.lower() == computer_action.lower():
            print("\nRock...\nPaper...\nScissors...\n\n[You chose", computer_action.upper(), "and computer chose", computer_action.upper() + ". It is a tie!]")
            continue

        else:
            if computer_action.lower() == "scissors" and user_action.lower() == "paper":
                print("\nRock...\nPaper...\nScissors...\n\n[You chose", user_action.upper(), "and computer chose", computer_action.upper() + ". Scissors cuts paper, you lose!]")
                computer_score += 1
            elif computer_action.lower() == "paper" and user_action.lower() == "rock":
                print("\nRock...\nPaper...\nScissors...\n\n[You chose", user_action.upper(), "and computer chose", computer_action.upper() + ". Paper covers rock, you lose!]")
                computer_score += 1
            elif computer_action.lower() == "rock" and user_action.lower() == "scissors":
                print("\nRock...\nPaper...\nScissors...\n\n[You chose", user_action.upper(), "and computer chose", computer_action.upper() +". Rock crushes scissors, you lose!]")
                computer_score += 1
            else:
                print("\nInvalid input. Please try again!")

def game_7():
    score = 0
    computer_score = 0
    max_score = 4
    while True:

        rps = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(rps)
        if score != 0 or computer_score != 0:
            print("\n\tYou have", score, "wins and computer has", computer_score, "wins.")
        if score == max_score:
            print("\nGAME OVER. You win!\n")
            break
        if computer_score == max_score:
            print("\nGAME OVER. You lose!\n")
            break

        user_action = input("\nChoose rock, paper or scissors: ")

        if user_action.lower() == "rock" and computer_action.lower() == "scissors":
            print("\nRock...\nPaper...\nScissors...\n\n[You chose ROCK and computer chose SCISSORS. Rock crushes scissors, you win!]")
            score += 1 
            continue
        
        elif user_action.lower() == "paper" and computer_action.lower() == "rock":
            print("\nRock...\nPaper...\nScissors...\n\n[You chose PAPER and computer chose ROCK. Paper covers rock, you win!]")
            score += 1
            continue

        elif user_action.lower() == "scissors" and computer_action.lower() == "paper":
            print("\nRock...\nPaper...\nScissors...\n\n[You chose SCISSORS and computer chose PAPER. Scissors cuts paper, you win!]")
            score += 1
            continue

        elif user_action.lower() == computer_action.lower():
            print("\nRock...\nPaper...\nScissors...\n[You chose", computer_action.upper(), "and computer chose", computer_action.upper() + ". It is a tie!")
            continue

        else:
            if computer_action.lower() == "scissors" and user_action.lower() == "paper":
                print("\nRock...\nPaper...\nScissors...\n\n[You chose", user_action.upper(), "and computer chose", computer_action.upper() + ". Scissors cuts paper, you lose!]")
                computer_score += 1
            elif computer_action.lower() == "paper" and user_action.lower() == "rock":
                print("\nRock...\nPaper...\nScissors...\n\n[You chose", user_action.upper(), "and computer chose", computer_action.upper() + ". Paper covers rock, you lose!]")
                computer_score += 1
            elif computer_action.lower() == "rock" and user_action.lower() == "scissors":
                print("\nRock...\nPaper...\nScissors...\n\n[You chose", user_action.upper(), "and computer chose", computer_action.upper() +". Rock crushes scissors, you lose!]")
                computer_score += 1
            else:
                print("\nInvalid input. Please try again!")

print("\n********************************************************")
print("*                                                      *")
print("*\tWELCOME TO ROCK, PAPER AND SCISSORS GAME       *") 
print("*                                                      *")
print("********************************************************\n")


while True:
    play = input("Would you like to play best-of-three or best-of-seven: (Choose either: 3/7 or type exit): ")
    if play.lower() == "3":
        print("\nWelcome to best-of-three game. You have to win two games to win the game! Good luck. ")
        game_3()
        while True:
            play_again = input("Would you like to play again or switch over to best-of-seven? (y/n/7): ")
            if play_again == "y":
                game_3()
            elif play_again =="n":
                quit("\nThank you for playing! Good bye! :)\n")
            elif play_again =="7":
                print("\nStarting best-of-seven...")
                game_7()
                while True:
                    play_again = input("Would you like to play again or switch over to best-of-three? (y/n/3): ")
                    if play_again == "y":
                        game_7()
                        continue
                    elif play_again == "n":
                        quit("\nThank you for playing! Good bye! :)\n")
                    else:
                        print("\nStarting best-of-three...")
                        game_3()
                        break
            elif play_again =="n":
                quit("\nThank you for playing! Good bye! :)\n")
            else:
                print("Invalid input. Please try again!")
    elif play.lower() == "7":
        print("\nWelcome to best-of-seven game. You have to win four games to win the game! Good luck. ")
        game_7()
        while True:
            play_again = input("Would you like to play again or switch over to best-of-three? (y/n/3): ")
            if play_again == "y":
                game_7()
            elif play_again =="n":
                quit("\nThank you for playing! Good bye! :)\n")
            elif play_again =="3":
                print("\nStarting best-of-three...")
                game_3()
                while True:
                    play_again = input("Would you like to play again or switch over to best-of-seven? (y/n/7): ")
                    if play_again == "y":
                        game_3()
                        continue
                    elif play_again == "n":
                        quit("\nThank you for playing! Good bye! :)\n")
                    else:
                        print("\nStarting best-of-seven...")
                        game_7()
                        break
            else:
                print("Invalid input. Please try again!")
    elif play.lower() == "exit":
        quit("\nGood bye :)\n")
    else:
        print("\nInvalid input. Please try again!\n")