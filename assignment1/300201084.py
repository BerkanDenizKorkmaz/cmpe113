from random import randint

print("\nWelcome to the game!")

turn = 0
user_point = 1000
dealer_point = 1000
isOver_User = True
isOver_Dealer = True
isOverTurn = True
isOver_input = True
isOver_input1 = True
isOver_bet = True
press = ""

while dealer_point > 0 and user_point > 0 and press != "q" and press != "Q":  # Main while loop that controls whether any player win the game or not
    ace_user = 0        #
    ace_dealer = 0      # Reset the values
    user_record = ""    # that must be reset
    dealer_record = ""  # for each round
    user_sum = 0        #
    dealer_sum = 0      #
    isOver_bet = True   #

    press = input("\nPress anything to continue. If you want to quit press 'Q' ")
    if press == "q" or press == "Q":
        print("\n----------------------------")
        print("          Good Bye")
        print("----------------------------")

    else:
        print("\n----------------------------")               #
        print("Round " + str(turn))                           #
        print("Current User Points:   " + str(user_point))    # Turner information
        print("Current Dealer Points: " + str(dealer_point))  #
        print("----------------------------\n")               #

        bet = int(input("Please place a maximum of " + str(user_point) + " bet: "))  # Bet claimer

        while isOver_bet == True:  # Break checker for bet
            if 0 < bet <= user_point:  # If that control for valid inputs for bet
                for user_draw in (0, 2):  # For loop that draws 2 cards and controls the aces
                    user_card = min(10, randint(1, 13))  # and records the cards and sum for user
                    user_sum = user_sum + user_card
                    if user_card == 1:
                        user_sum = user_sum + 10
                        ace_user = ace_user + 1
                    if user_sum > 21:
                        if ace_user > 0:
                            user_sum = user_sum - 10
                            ace_user = ace_user - 1
                    user_record = user_record + " " + str(user_card)

                print("\nUser has:  " + user_record + " (Total: " + str(user_sum) + ")")

                for dealer_draw in (0, 2):  # For loop that draws 2 cards, controls the aces
                    dealer_card = min(10, randint(1, 13))  # and records the cards and sum for dealer
                    dealer_sum = dealer_sum + dealer_card
                    if dealer_card == 1:
                        dealer_sum = dealer_sum + 10
                        ace_dealer = ace_dealer + 1
                    if dealer_sum > 21:
                        if ace_dealer > 0:
                            dealer_sum = dealer_sum - 10
                            ace_dealer = ace_dealer - 1
                    dealer_record = dealer_record + " " + str(dealer_card)
                    if dealer_draw == 0:
                        print("Dealer has: " + str(dealer_card) + " ?")

                answer1 = input("\nDo you want to draw just one more card and double the bet? (y,n)\n")

                while isOverTurn == True:  # While loop that checks the answers and compute the results
                    if answer1 == "y" or answer1 == "Y":
                        bet = bet * 2

                        user_card = min(10, randint(1, 13))  # 1 draw for user
                        user_sum = user_sum + user_card            #
                        if user_card == 1:                         #
                            user_sum = user_sum + 10               #
                            ace_user = ace_user + 1                #
                        if user_sum > 21:                          #
                            if ace_user > 0:                       #
                                user_sum = user_sum - 10           #
                                ace_user = ace_user - 1            #

                        user_record = user_record + " " + str(user_card)
                        print("\nNew card: " + str(user_card))
                        print("User has: " + user_record + "(Total: " + str(user_sum) + ")\n")

                        if user_sum > 21:  # Check the 21 over cond. to skip dealer's turn
                            print("Dealer has: " + dealer_record + "(Total: " + str(dealer_sum) + ")")

                            print("\nDealer Won The Round")
                            user_point = user_point - bet
                            dealer_point = dealer_point + bet
                        else:
                            while user_sum > dealer_sum and dealer_sum <= 21:  # Condition that user didn't lose due to over 21
                                dealer_card = min(10, randint(1, 13))   # Dealer draws till win or tie condition
                                dealer_sum = dealer_sum + dealer_card
                                if dealer_card == 1:
                                    dealer_sum = dealer_sum + 10
                                    ace_dealer = ace_dealer + 1
                                if dealer_sum > 21:
                                    if ace_dealer > 0:
                                        dealer_sum = dealer_sum - 10
                                        ace_dealer = ace_dealer - 1
                                dealer_record = dealer_record + " " + str(dealer_card)
                                print("\nDealer draws a new card: " + str(dealer_card))

                            print("Dealer has: " + dealer_record + "(Total: " + str(dealer_sum) + ")")

                            if dealer_sum > 21:
                                print("\nUser Won The Round")            # All the conditions
                                user_point = user_point + bet            # that may happen
                                dealer_point = dealer_point - bet        # at the end
                            else:                                        #
                                if user_sum > dealer_sum:                #
                                    print("\nUser Won The Round")        #
                                    user_point = user_point + bet        #
                                    dealer_point = dealer_point - bet    #
                                elif dealer_sum > user_sum:              #
                                    print("\nDealer Won The Round")      #
                                    user_point = user_point - bet        #
                                    dealer_point = dealer_point + bet    #
                                else:                                    #
                                    print("\nTie break")                 #

                        isOverTurn = False  # Break

                    elif answer1 == "n" or answer1 == "N":
                        while isOver_input == True:
                            isOver_y = True
                            answer2 = input("\nDo you want another card? (y,n)\n")
                            if answer2 == "y" or answer2 == "Y":
                                while isOver_input1 == True:
                                    while isOver_User:  # User draws and check the conditions
                                        while answer2 == "y" or answer2 == "Y":
                                            user_card = min(10, randint(1, 13))
                                            user_sum = user_sum + user_card
                                            if user_card == 1:
                                                user_sum = user_sum + 10
                                                ace_user = ace_user + 1
                                            if user_sum > 21:
                                                if ace_user > 0:
                                                    user_sum = user_sum - 10
                                                    ace_user = ace_user - 1
                                            user_record = user_record + " " + str(user_card)
                                            print("\nNew card: " + str(user_card))
                                            print("User has: " + user_record + "(Total: " + str(user_sum) + ")")
                                            if user_sum > 21:
                                                print("\nDealer has: " + dealer_record + "(Total: " + str(
                                                    dealer_sum) + ")")

                                                print("\nDealer Won The Round")
                                                user_point = user_point - bet
                                                dealer_point = dealer_point + bet
                                                answer2 = "n"
                                                isOver_Dealer = False
                                            else:  # Controls the case that if the user gives us an invalid answer
                                                while isOver_y:
                                                    print("Your answer was not valid.")
                                                    answer2 = input("\nDo you want another card? (y,n)\n")
                                                    if answer2 == "y" or answer2 == "Y":
                                                        isOver_y = False
                                                    elif answer2 == "n" or answer2 == "N":
                                                        isOver_y = False
                                            isOver_User = False
                                        isOver_input = False

                                    while isOver_Dealer == True:  # Dealer draws and check the conditions

                                        while user_sum > dealer_sum and dealer_sum <= 21:
                                            dealer_card = min(10, randint(1, 13))
                                            dealer_sum = dealer_sum + dealer_card
                                            if dealer_card == 1:
                                                dealer_sum = dealer_sum + 10
                                                ace_dealer = ace_dealer + 1
                                            if dealer_sum > 21:
                                                if ace_dealer > 0:
                                                    dealer_sum = dealer_sum - 10
                                                    ace_dealer = ace_dealer - 1
                                            dealer_record = dealer_record + " " + str(dealer_card)
                                            print("\nDealer draws a new card: " + str(dealer_card))
                                        print("Dealer has: " + dealer_record + "(Total: " + str(dealer_sum) + ")")

                                        if dealer_sum > 21:
                                            print("\nUser Won The Round")          # All the conditions
                                            user_point = user_point + bet          # that may happen
                                            dealer_point = dealer_point - bet      # at the end
                                        else:                                      #
                                            if user_sum > dealer_sum:              #
                                                print("\nUser Won The Round")      #
                                                user_point = user_point + bet      #
                                                dealer_point = dealer_point - bet  #
                                            elif dealer_sum > user_sum:            #
                                                print("\nDealer Won The Round")    #
                                                user_point = user_point - bet      #
                                                dealer_point = dealer_point + bet  #
                                            else:                                  #
                                                print("\nTie break")               #
                                        isOver_Dealer = False

                                    isOver_input1 = False

                            elif answer2 == "n" or answer2 == "N":
                                while isOver_Dealer == True:  # Dealer Draws and check the conditions
                                    while user_sum > dealer_sum and dealer_sum <= 21:
                                        dealer_card = min(10, randint(1, 13))
                                        dealer_sum = dealer_sum + dealer_card
                                        if dealer_card == 1:
                                            dealer_sum = dealer_sum + 10
                                            ace_dealer = ace_dealer + 1
                                        if dealer_sum > 21:
                                            if ace_dealer > 0:
                                                dealer_sum = dealer_sum - 10
                                                ace_dealer = ace_dealer - 1
                                        dealer_record = dealer_record + " " + str(dealer_card)
                                        print("\nDealer draws a new card: " + str(dealer_card))
                                    print("Dealer has: " + dealer_record + "(Total: " + str(dealer_sum) + ")")

                                    if dealer_sum > 21:
                                        print("\nUser Won The Round")          # All the conditions
                                        user_point = user_point + bet          # that may happen
                                        dealer_point = dealer_point - bet      # at the end
                                    else:                                      #
                                        if user_sum > dealer_sum:              #
                                            print("\nUser Won The Round")      #
                                            user_point = user_point + bet      #
                                            dealer_point = dealer_point - bet  #
                                        elif dealer_sum > user_sum:            #
                                            print("\nDealer Won The Round")    #
                                            user_point = user_point - bet      #
                                            dealer_point = dealer_point + bet  #
                                        else:                                  #
                                            print("\nTie break")               #
                                    isOver_Dealer = False  # "Break"s for all
                                    isOver_input = False   # loops that contains this part
                                    isOverTurn = False     #

                            else:
                                print("\nYour answer was not valid.")
                            isOverTurn = False  # Break for ending the turn
                    else:
                        print("\nYour answer was not valid.")
                        answer1 = input("\nDo you want to draw just one more card and double the bet? (y,n)\n")
                turn = turn + 1

                isOverTurn = True     # Reset all the values
                isOver_User = True    # and end bet loop
                isOver_Dealer = True  #
                isOver_input = True   #
                isOver_input1 = True  #
                isOver_bet = False    #
            else:
                print("\nYour answer was not valid.")
                bet = int(input("Please place a maximum of " + str(user_point) + " bet: "))  # Bet claimer
if user_point > 0 and press != "q" and press != "Q":
    print("\n----------------------------")
    print('''      Congragulations! 
          You Won!''')
    print("----------------------------")
elif dealer_point > 0 and press != "q" and press != "Q":
    print("\n----------------------------")
    print("          Game Over")
    print("-----------------------------")