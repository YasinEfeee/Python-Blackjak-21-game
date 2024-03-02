# Import libraries

import random
import time


# Get player decision (Hit or Stand):

def get_player_decision():
    print("\n-----------------------------------------")
    print("What would you like to do? Hit or Stand: ")
    while True:
        hit_or_stand = input("Hit or stand: ").lower().rstrip()
        if not hit_or_stand in ["hit", "stand"]:
            print("--------------------------")
            print("Please enter hit or stand")
            print("--------------------------")
        else:
            print(f"your choice is: {hit_or_stand}")
            break
    return hit_or_stand


# Making and Shuffiling deck:
            
def shuffling_cards():
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        deck = []

        for suit in suits:
            for rank in ranks:
                deck.append(f"{rank} of {suit}")
        return deck


# Calculate player cards value:

def calculate_player_cards_value(Player_cards):
    
    Playar_cards_value = []
    player_total_value = 0
    
    for ilk in Player_cards:
        if ilk[0].isdigit():
            if ilk[0] == "1":
                    Playar_cards_value.append(10)
            else:
                    Playar_cards_value.append(int(ilk[0]))
        elif ilk[0:3] == "Ace":
            Playar_cards_value.append(11)
        else: # ["Jack", "Queen", "King"]
            Playar_cards_value.append(10)
            
    player_total_value = sum(Playar_cards_value) # Player's Card's value addition
    
    return player_total_value


# Calculate dealer cards value:

def calculate_dealer_cards_value(Dealer_cards):
    
    Dealer_cards_value = []
    total_value = 0
    
    for ilk in Dealer_cards:
        if ilk[0].isdigit():
            if ilk[0] == "1":
                Dealer_cards_value.append(10)
            else:
                Dealer_cards_value.append(int(ilk[0]))
        elif ilk[0:3] == "Ace":
            Dealer_cards_value.append(11)
        else: # ["Jack", "Queen", "King"]
            Dealer_cards_value.append(10)
            
    total_value = sum(Dealer_cards_value) # Dealer's Card's alue addition
         
    return total_value

# To get dealer first card and its value:

def first_calculate_dealer_cards_value(Dealer_cards):
    Dealer_cards_value = []
    
    for ilk in Dealer_cards:
        if ilk[0].isdigit():
            if ilk[0] == "1":
                Dealer_cards_value.append(10)
            else:
                Dealer_cards_value.append(int(ilk[0]))
        elif ilk[0:3] == "Ace":
            Dealer_cards_value.append(11)
        else: # ["Jack", "Queen", "King"]
            Dealer_cards_value.append(10)
        
        return Dealer_cards_value


# Printing player cards and values:

def player_printing():
    print(f"Your card's are: -- ' {"  —  ".join(Player_cards)} ' -- and Total is : -- {calculate_player_cards_value(Player_cards)} --")

   
# Printing dealer cards and values:
     
def dealer_printing():
    print(f"Dealer hit card. Now dealer's cards are: -- ' {"  —  ".join(Dealer_cards)} ' -- and Total is : -- {calculate_dealer_cards_value(Dealer_cards)} --")
    
    
# To get result and player wallet:
    
def result(player_bet, player_wallet):
    if calculate_dealer_cards_value(Dealer_cards) > 21:
        player_wallet = player_wallet + (player_bet * 2)
        print(f"You get {player_bet * 2}$. Now you have {player_wallet} dollar")
        
    elif calculate_player_cards_value(Player_cards) == 21:
        player_wallet = player_wallet + (player_bet * 3)
        print(f"You get {player_bet * 3}$ with Black Jack. Now you have {player_wallet} dollar")
        
    elif calculate_dealer_cards_value(Dealer_cards) < calculate_player_cards_value(Player_cards) < 21:
        player_wallet = player_wallet + (player_bet * 2)
        print(f"You get {player_bet * 2}$. Now you have {player_wallet} dollar")
        
    elif calculate_dealer_cards_value(Dealer_cards) == calculate_player_cards_value(Player_cards):
        player_wallet = player_wallet + player_bet
        print(f"You get 0$ (Push). Now you have {player_wallet} dollar")
        
    elif calculate_dealer_cards_value(Dealer_cards) == 21:
        player_wallet = player_wallet
        print(f"You lose :( You have {player_wallet} dollar")
        
    elif calculate_player_cards_value(Player_cards) > 21:
        player_wallet = player_wallet
        print(f"You lose :( You have {player_wallet} dollar")
        
    elif calculate_player_cards_value(Player_cards) < calculate_dealer_cards_value(Dealer_cards) < 21:
        player_wallet = player_wallet
        print(f"You lose :( You have {player_wallet} dollar")
        
    return player_wallet


# If player choose hit:

def hit_phase(player_bet, player_wallet):
    Player_cards.append(random.choice(shuffling_cards()))
    time.sleep(1.5)
    print("----------------------------------------------------------------------")
    print(f"You hit so now your cards are: -- {", ".join(Player_cards)} -- and Total is : -- {calculate_player_cards_value(Player_cards)} --")
    print("----------------------------------------------------------------------")
    if calculate_player_cards_value(Player_cards) > 21:
        time.sleep(1.7)
        print("----------------------------------------------------------------------")
        print("You Lose :(")
        print("----------------------------------------------------------------------")
    else:
        decision = get_player_decision()
        if decision == "stand":
            stand_phase(player_bet, player_wallet)
        else:
            hit_phase(player_bet, player_wallet)
            
      
# If player choose stand:
       
def stand_phase(player_bet, player_wallet):
    time.sleep(1.5)
    print("----------------------------------------------------------------------")
    player_printing()
    print("----------------------------------------------------------------------")
    time.sleep(1.5)
    print("Dealer switched his other card")
    print(f"Now dealer cards are: -- {"  —  ".join(Dealer_cards)} -- and Total is : --{calculate_dealer_cards_value(Dealer_cards)}--")
    while True:
                if calculate_dealer_cards_value(Dealer_cards) < 17:
                    time.sleep(2)
                    print("----------------------------------------------------------------------")
                    Dealer_cards.append(random.choice(shuffling_cards()))
                    dealer_printing()
                    calculate_dealer_cards_value(Dealer_cards)
                else:
                    if calculate_dealer_cards_value(Dealer_cards) > 21:
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print("-- Busted -- You Win :)")
                        print("----------------------------------------------------------------------")
                    elif calculate_player_cards_value(Player_cards) == 21:
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print("-- BlackJack -- You Win :)")
                        print("----------------------------------------------------------------------")
                    elif calculate_dealer_cards_value(Dealer_cards) < calculate_player_cards_value(Player_cards) < 21: 
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print(" You Win :)")
                        print("----------------------------------------------------------------------")
                    elif calculate_dealer_cards_value(Dealer_cards) == 21:
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print("-- BlackJack -- You Lose :( ")
                        print("----------------------------------------------------------------------")
                    elif calculate_dealer_cards_value(Dealer_cards) == calculate_player_cards_value(Player_cards):
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print(" Tie (Push)")
                        print("----------------------------------------------------------------------")
                    elif calculate_player_cards_value(Player_cards) > 21:
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print("-- You Busted -- You Lose :( ")
                        print("----------------------------------------------------------------------")
                    elif calculate_player_cards_value(Player_cards) < calculate_dealer_cards_value(Dealer_cards) < 21:
                        time.sleep(1.7)
                        print("----------------------------------------------------------------------")
                        print(" You Lose :( ")
                        print("----------------------------------------------------------------------")
                    break
                
# Game/Code starting point      
# İnformations and Welcome message:
    
print("\n-- Welcome to Black jack --")
print("\n-Blackjack, also known as twenty-one, is a popular card game played in casinos worldwide.")
print("-The objective is to beat the dealer by having a hand value closer to 21 without exceeding it.")
print("-Each player is dealt two cards initially, and they can choose to 'hit' (receive another card) or 'stand' (keep their current hand).")
print("-Card Values: Jack, Queen, King: Each is worth 10 points. 2 to 10: Represent the face value of the cards.")
print("-Note: In Blackjack, the Ace can typically have a value of 1 or 11. However, in this code, the Ace is assigned a fixed value of 11. Therefore, be mindful that having two Aces could result in a total of 22, exceeding the limit of 21.")
print("\n--- ★ Have Fun ★ ---")


# Game continue until player dont want to play or player lost his/her all money 

player_wallet = 100  # $Dollar for every new game
restart_outer_loop = True

while restart_outer_loop:
    restart_outer_loop = False
    player_bet = 0
    
    # Asking for bet amount:
    
    print(f"\n--- You have {player_wallet}$. How much would you like to bet? ---")
    while True:
        try:
            player_bet = int(input("Place your bet: "))
            if not 0 < player_bet <= player_wallet:
                print("Please bet you have")
            else:
                player_wallet -= player_bet 
                print(f"Your bet is {player_bet}$. Now you have {player_wallet} dollar")
                break
        except ValueError:
            print("Please enter a number")
            
    # Shuffling cards:          
    shuffling_cards()
    
    # Dealer's card determination:
    
    Dealer_cards = []
    Dealer_cards.append(random.choices(shuffling_cards(), k=2))
    Dealer_cards = Dealer_cards[0]  
        
    # Player's card determination:
        
    Player_cards = []
    Player_cards.append(random.choices(shuffling_cards(), k=2))
    Player_cards = Player_cards[0]
    
    # Printing dealer first card and value:
    
    time.sleep(1.7)
    print("----------------------------------------------------------------------")
    player_printing()
    print("----------------------------------------------------------------------")
    print(f"Dealer first card is: -- {Dealer_cards[0]} -- and Total is : -- {first_calculate_dealer_cards_value(Dealer_cards)[0]} --")
    print("----------------------------------------------------------------------")
    
    # ! In code I didn't/couldn't add ace equals 1 or 11, so ace just equals 11. !
    # In here if player or dealer card's value equals 22 game will stop working:
    
    if calculate_player_cards_value(Player_cards) == 22:
        print("\n---------------------------------------------------------------------")
        print("Sorry Player card's total value equals 22. Game please restart game.")
        print("----------------------------------------------------------------------")
        break
    elif calculate_dealer_cards_value(Dealer_cards) == 22:
        print("Dealer switched his other card")
        print(f"Now dealer cards are: -- {", ".join(Dealer_cards)} -- and total is : --{calculate_dealer_cards_value(Dealer_cards)}--")
        print("\n---------------------------------------------------------------------")
        print("Sorry Dealer card's total value equals 22. Game please restart game.")
        print("----------------------------------------------------------------------")
        break
    
    # Hit or stand situation:
        
    hit_or_stand_result = get_player_decision()
    if hit_or_stand_result == "hit":
        hit_phase(player_bet, player_wallet)
    else:
        stand_phase(player_bet, player_wallet)
    
    # Check if player wants to continue playing:
    
    player_wallet = result(player_bet, player_wallet)
    if player_wallet != 0: 
        
        while True:
            print("Do you want to play again?: ")
            print("----------------------------------------------------------------------")
            play_again = input("Do you want to play again? (yes/no): ").lower().strip()
            if play_again in ["yes", "no"]:
                if play_again == "no":
                    print("----------------------------------------------------------------------")
                    print("Thank you for playing!")
                    print("----------------------------------------------------------------------")
                    Player_cards.clear()
                    Dealer_cards.clear()
                    break
                elif play_again == "yes":
                    Player_cards.clear()
                    Dealer_cards.clear()
                    restart_outer_loop = True
                    break
            else:
                print("Please enter a valid input")
                
    else:
        print(f"You have {player_wallet} dollar, so you cannot play again. Sorry :( ")
        print("----------------------------------------------------------------------------")
        break