import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# deal one card for each of dealer and player. update card lists
def dealPlayer(player_cards):
    player_cards.append(random.choice(cards))
    # print(f"| *** Your cards: {player_cards}")

def dealDealer(dealer_cards):
    dealer_cards.append(random.choice(cards))
    # print(f"| *** Dealer cards: {dealer_cards}")

# return sum of cards in hand
def checkSum(card_list):
    return sum(card_list)

def showCards(should_continue, player_cards, dealer_cards):
    print("+===========================")
    if should_continue:
        print(f"| Your cards: {player_cards}")
        covered_cards = [0]
        covered_cards += dealer_cards[1:]
        print(f"| Dealer cards: {covered_cards}")
        print("| ** '0' represents covered card")
    else:
        print(f"| Your cards: {player_cards}")
        print(f"| Dealer cards: {dealer_cards}")
    print("+===========================")

def whoWins(player_sum, dealer_sum):
    if dealer_sum == 21:
        print("You lose")
    elif player_sum == 21:
        print("You Win!")
    elif player_sum > dealer_sum:
        print("You Win!")
    else:
        print("You lose")

def blackjack():
    dealer_cards = []
    player_cards = []
    # start game
    should_continue = True
    print("Welcome to blackjack!")
    # initial cards for each one
    dealPlayer(player_cards)
    dealDealer(dealer_cards)
    dealPlayer(player_cards)
    dealDealer(dealer_cards)
    while should_continue:
        dealer_sum = checkSum(dealer_cards)
        player_sum = checkSum(player_cards)
        # print(f"*** p: {player_sum}, d: {dealer_sum}")
        if player_sum == 21:
            should_continue = False
            print("You Win!")
            showCards(should_continue, player_cards, dealer_cards)
        elif player_sum > 21:
            # check if there is A in cards
            if 11 in player_cards:
                player_cards[player_cards.index(11)] = 1
                continue
            should_continue = False
            showCards(should_continue, player_cards, dealer_cards)
            print("Bust")
        elif dealer_sum > 21:
            should_continue = False
            showCards(should_continue, player_cards, dealer_cards)
            print("You Win!")
        else:
            showCards(should_continue, player_cards, dealer_cards)
            valid_input = False
            while not valid_input:
                choice = input("Do you want another card? Type y for yes, n for no: ")
                if choice == "y":  # Yes
                    valid_input = True
                    # deal one card to player
                    dealPlayer(player_cards)
                    # check to see if dealer need another card
                    if dealer_sum < 17:  # TODO: more check with A values
                        dealDealer(dealer_cards)
                    else:
                        if 11 in dealer_cards:
                            dealer_cards[dealer_cards.index(11)] = 1
                            dealDealer(dealer_cards)
                elif choice == "n":  # No
                    valid_input = True
                    # check to see if dealer need another card
                    if dealer_sum < 17:  # TODO: more check with A values
                        dealDealer(dealer_cards)
                        dealer_sum = checkSum(dealer_cards)
                        # if 11 in dealer_cards:
                        #     print("make disition")
                        #     disition = random.choice([0, 1])
                        #     print("dddddddddddd" + str(disition))
                        #     if disition == 1:  # A as 1
                        #         dealer_cards[dealer_cards.index(11)] = 1
                        #         dealDealer(dealer_cards)
                    else:
                        if 11 in dealer_cards:
                            disition = random.choice([0, 1])
                            if disition == 1:  # A as 1
                                dealer_cards[dealer_cards.index(11)] = 1
                                dealDealer(dealer_cards)
                                dealer_sum = checkSum(dealer_cards)
                    # calculate result
                    should_continue = False
                    whoWins(player_sum, dealer_sum)
                    showCards(should_continue, player_cards, dealer_cards)
                    break
                else:
                    print("Invalid input")
    if input("New game? Type y for yes: ") == "y":
        blackjack()


blackjack()

