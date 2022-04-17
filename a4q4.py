#NAME - VIKHYAT SINGH
#NSID - VIS550
#STUDENT NUMBER - 11300244
#INSTRUCTOR - PROFFESOR ERIC

# Question 4

import random as ran

class Card(object):

    # Function 1- Creates the  list of all possible cards that can be drawn from the 52 card playing deck.
    # ["AH","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH" ,...]
    # Repeated for the 3 other suits (D,S,C)

    def create(self):
        """
            Purpose:
                This function creates a list of all possible cards that can be drawn from the 52 playing card deck.
            Pre-Conditions:
                :param None
            Post-Conditions:
                none
            Return:
                :return List of all possible cards that can be drawn from the 52 card playing card deck.
        """

        list_of_cards=[]
        suits= ['H','D','S','C']
        values=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

        # Appends the card value with the suit value and pushes into the list_of_cards list.

        for suit in suits:
            for value in values:
                list_of_cards.append(str(value)+str(suit))

        return list_of_cards

    # Function 2 - Randomly deals a number of cards to a number of players from the given deck.
    # Tells the player numbers if enough cards are not dealt.

    def deal(self,num_cards, num_players, deck):

        """
            Purpose:
                This function distributes the given random cards to player. 
            Pre-Conditions:
                :param num_cards: number of cards for each player
                :param num_players: total number of players
                :param deck: list of cards
            Post-Conditions:
                card is removed from the deck
            Return:
                :return List of cards explaining the card linked with player

            """
        all_players_dealt_cards=[]

        # Selects the player to distribute card
        for player in range(num_players):
            each_player_cards=[]
            for card in range(num_cards):

                # Only distributes if cards are available in the deck.
                if len(deck)>0:
                    selected_card= ran.choice(deck)

                    # Removes the selected card from the deck
                    deck.remove(selected_card)

                    # Appends the selected card of that player
                    each_player_cards.append(selected_card)
                
            # If certain player does not get required card this statement will run
            if len(each_player_cards)!=num_cards:
                print("Player "+ str(player+1) +" did not receive "+ str(num_cards) +" cards!")

            # Appends the list of card of each player to all players dealt card list
            all_players_dealt_cards.append(each_player_cards)
        
        return all_players_dealt_cards

    # Function 3 - Takes in the string of a card, and returns its integer value.

    def value(self, card):
        """
        Purpose:
            This function takes in the string of a card, and returns its integer value.
        Pre-Conditions:
            :param card: card in the deck
        Post-Conditions:
            none
        Return:
            :return The numerical/interger value of card is returned
        """

        # A dictionary to store the numerical value of certain cards.
        card_value={"A":1, "J":11, "Q":12,"K":13, "10":10}
        if len(card)<3:
            val=card[0]

            # If the key of that card is found in dictionary returns the integer value of that card
            if(card_value.get(val)!= None):
                return card_value.get(val)
            
            # Else returns the integer value of that string
            else:
                return int(val)
        
        # Only cards with number 10 has 3 characters in the string so return 10 if the length of string is 3.
        else:
            return 10

    # Funciton 4- Takes a list of cards, and returns the card string with the highest value.

    def highest(self, list_of_cards):
        """
        Purpose:
            This function returns the highest valued card.
        Pre-Conditions:
            :param list_of_cards: all the list of cards in the deck
        Post-Conditions:
            none
        Return:
            :return The highest valued card is returned.
        """

        highest_value_of_card = 0
        highest_card=""
        
        # This loop will calculates the value of each card and if card with more value is encountered updates the highest value card.
        for each_card in list_of_cards:
            value_of_card=self.value(each_card)
            if highest_value_of_card < value_of_card:
                highest_card=each_card
                highest_value_of_card=value_of_card

        return highest_card

    # Function 5- Takes a list of cards, and returns the card string with lowest value.

    def lowest(self, list_of_cards):
        """
            Purpose:
                This function returns the lowest valued card.
            Pre-Conditions:
                :param list_of_cards: all the list of cards in the deck
            Post-Conditions:
                none
            Return:
                :return The lowest valued card is returned.
        """
        lowest_value_of_card=14
        lowest_card=""

        # This loop will calculates the value of each card and if card with less value is encountered updates the lowest value card.
        for each_card in list_of_cards:
            value_of_card= self.value(each_card)
            if lowest_value_of_card > value_of_card:
                lowest_card = each_card
                lowest_value_of_card = value_of_card

        return lowest_card

    # Function 6- Takes a list of cards, and d returns the average (float) value of this given list of cards.

    def average(self, list_of_cards):
        """
        Purpose:
            This function calculates the average of cards
        Pre-Conditions:
            :param list_of_cards: all the list of cards in the deck
        Post-Conditions:
            none
        Return:
            :return The average is calcuated and floating value is returned.
        """
        sum_of_all_cards=0
        if len(list_of_cards) == 0:
            return 0

        # Calculates the value of each card and calculates the sum of all the card
        for each_card in list_of_cards:
            value_of_card = self.value(each_card)
            sum_of_all_cards+=value_of_card

        # To get the mean total sum is divided by the total number of cards.
        mean_of_cards=sum_of_all_cards/len(list_of_cards)


        return mean_of_cards


