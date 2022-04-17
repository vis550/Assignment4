#NAME - VIKHYAT SINGH
#NSID - VIS550
#STUDENT NUMBER - 11300244
#INSTRUCTOR - PROFFESOR ERIC

# QUESTION - 4 - TESTING

from a4q4 import Card

#####################################################################
# Testing FUNCTION - 1
# Total 52 cards should be created
test_item = 'create()'
expected = 52
reason = "Check count after one value added"

# call the operation
c = Card()
deck_of_cards = c.create()
result = len(deck_of_cards)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#####################################################################

# Testing FUNCTION - 2

# Test Case 1- Removing no cards from deck
test_item = 'deal()'
expected = []
reason = "Check count after one value added"

# call the operation
c = Card()
deck_of_cards = c.create()
result = c.deal(0,0,deck_of_cards)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# cards_dealt = Card.deal(5, 3, deck)
# print(cards_dealt)

# Test Case 2 - REMOVING 20 CARDS FROM THE DECK
test_item = 'deal()'
expected_cards = 5
expected_players = 4
expected_deck_of_card_size = 52 -(5*4)

# call the operation
c = Card()
deck_of_cards = c.create()
result = c.deal(5,4,deck_of_cards)

result_cards = len(result[0])
result_players = len(result)
result_deck_of_card_size = len(deck_of_cards)

if result_cards != expected_cards:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_players != expected_players:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_deck_of_card_size != expected_deck_of_card_size:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 3 - Removing more cards then in deck
test_item = 'deal()'
expected_cards_p1 = 26
expected_cards_p2 = 26
expected_cards_p3 = 0
expected_cards_p4 = 0

expected_players = 4
expected_deck_of_card_size = 0

# call the operation
c = Card()
deck_of_cards = c.create()
result = c.deal(26,4,deck_of_cards)

result_cards_p1 = len(result[0])
result_cards_p2 = len(result[1])
result_cards_p3 = len(result[2])
result_cards_p4 = len(result[3])
result_players = len(result)
result_deck_of_card_size = len(deck_of_cards)

if result_cards_p1 != expected_cards_p1:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_cards_p2 != expected_cards_p2:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_cards_p3 != expected_cards_p3:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_cards_p4 != expected_cards_p4:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_players != expected_players:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

if result_deck_of_card_size != expected_deck_of_card_size:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#####################################################################

# FUNCTION - 3
# Test Case 1- VALUE OF CARDS - A=1 , J=11, Q=12, K= 13

test_item = 'value()'
data_in = ["AS","2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS"]
expected = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# call the operation
c = Card()
deck_of_cards = c.create()
result=[]
for card in data_in:
    result.append(c.value(card))

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#####################################################################

# FUNCTION - 4

# Test Case 1- ALL OF DIFFERENT Suit

test_item = 'highest()'
data_in = ["1D","2H","QS","6C","KH"]
expected = "KH"

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.highest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 2 - ALL OF SAME Suit
test_item = 'highest()'
data_in = ["1D","2D","JD","8D","KD"]
expected = "KD"

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.highest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - EMPTY LIST - NO CARD
test_item = 'highest()'
data_in = []
expected = ""

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.highest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - ONLY ONE VALUE
test_item = 'highest()'
data_in = ["10D"]
expected = "10D"

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.highest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#####################################################################

# FUNCTION - 5
# LOWEST VALUE

# Test Case 1- ALL OF DIFFERENT Suit

test_item = 'lowest()'
data_in = ["1D","2H","QS","6C","KH"]
expected = "1D"

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.lowest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 2 - ALL OF SAME Suit
test_item = 'lowest()'
data_in = ["1D","2D","JD","8D","KD"]
expected = "1D"

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.lowest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - EMPTY LIST - NO CARD
test_item = 'lowest()'
data_in = []
expected = ""

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.lowest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - ONLY ONE VALUE
test_item = 'lowest()'
data_in = ["10D"]
expected = "10D"

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.lowest(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

#####################################################################

# FUNCTION - 6
# AVERAGE VALUE

# ALL VALUES OF DIFFERENT TYPES

# Test Case 1- ALL OF DIFFERENT Suit

test_item = 'average()'
data_in = ["1D","2H","QS","6C","KH"]
expected = 6.8

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.average(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 2 - ALL OF SAME Suit
test_item = 'average()'
data_in = ["1D","2D","JD","8D","KD"]
expected = 7.0

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.average(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - EMPTY LIST - NO CARD
test_item = 'average()'
data_in = []
expected = 0

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.average(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - ONLY ONE VALUE
test_item = 'average()'
data_in = ["10D"]
expected = 10

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.average(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 5 - all cards with A,J,Q,K
test_item = 'average()'
data_in = ["AS","QS","JS","KS"]
expected = 9.25

# call the operation
c = Card()
deck_of_cards = c.create()
result=c.average(data_in)

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))
print("Testing completed !!")