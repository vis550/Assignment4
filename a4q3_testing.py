#NAME - VIKHYAT SINGH
#NSID - VIS550
#STUDENT NUMBER - 11300244
#INSTRUCTOR - PROFFESOR ERIC

# QUESTION - 2 - TESTING FILE

import a4q3 as S


def close_enough(a, b, tolerance):
    """
    Purpose:
        Check if 2 floating point values are close enough to 
        be considered equal.  See the Addendum in the assignment!
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return True if the difference between a and b is small
    """
    return abs(a - b) < tolerance


#####################################################################
# test Statistics.create()
# We can't test the object's identity, and the attributes are private
# The only thing we can do is check to see if the initial values are correct
# This is indirect testing, and since we're using 2 methods in the test, 
# it's a very limited form of integration testing.


test_item = 'Statistics.create()'
expected = 0
reason = "Initial count value"

# call the operation
stats = S.Statistics()
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


expected = 0
reason = "Initial average value"

# call the operation
stats = S.Statistics()
result = stats.mean()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))




#####################################################################
# test Statistics.add()  
# We can't test add() directly, so check add() + count()
# these are integration tests


test_item = 'add() + count()'
data_in = 0
expected = 1
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


test_item = 'add() + count()'
data_in = [0, 0, 0, 0, 0]
expected = 5
reason = "Check count after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 1 - Only a single integer

test_item = 'add() + count()'
data_in = 5
expected = 1
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 2 - Multiple different Positive Integers

test_item = 'add() + count()'
data_in = [7,1,2,4,5,6,4]
expected = 7
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - Multiple Same Positive Integers

test_item = 'add() + count()'
data_in = [1,1,1,1]
expected = 4
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - Only Single Negative Integer

test_item = 'add() + count()'
data_in = -5
expected = 1
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 5- Multiple Different Negative Integers

test_item = 'add() + count()'
data_in = [-7,-1,-2,-4,-5,-6,-4]
expected = 7
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 6- Multiple Same Negative Integers

test_item = 'add() + count()'
data_in = [-1,-1,-1,-1]
expected = 4
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 7- Positive and Negative Integers

test_item = 'add() + count()'
data_in = [1,-2,-3,4]
expected = 4
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 8- Single Float Number

test_item = 'add() + count()'
data_in = 1.2
expected = 1
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 9 - Multiple Positive Float Numbers

test_item = 'add() + count()'
data_in = [1.2,3.1,4.6,5.1]
expected = 4
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 10 - Multiple Negative Float Numbers

test_item = 'add() + count()'
data_in = [-1.2,-3.1,-4.6,-5.1]
expected = 4
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 11 - Multiple positive and negative float and integers

test_item = 'add() + count()'
data_in = [-1.2,3,4.6,-5, 6, 9.2,-7,2]
expected = 8
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.count()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))



#####################################################################
# test Statistics.mean()


test_item = 'add() + mean()'
data_in = 0
expected = 0
reason = "Check average after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mean()

# We shouldn't test the floating point values for equality, because or roundoff error
# So use the close_enough() function.

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


#####################################################################
# test Statistics.mean()


test_item = 'add() + mean()'
data_in = [0, 0, 0, 0, 0]
expected = 0.0
reason = "Check average after 5 values added"

# call the operation
stats = S.Statistics()
for v in data_in:
    stats.add(v)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 1 - Only a single integer

test_item = 'add() + count()'
data_in = 5
expected = 5.0
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 2 - Multiple different Positive Integers

test_item = 'add() + count()'
data_in = [7,1,2,4,5,6,9]
expected = 4.85714286
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 3 - Multiple Same Positive Integers

test_item = 'add() + count()'
data_in = [1,1,1,1]
expected = 1.0
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 4 - Only Single Negative Integer

test_item = 'add() + count()'
data_in = -5
expected = -5.0
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))


# Test Case 5- Multiple Different Negative Integers

test_item = 'add() + count()'
data_in = [-7,-1,-2,-4,-5,-6,-8]
expected = -4.71428571
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 6- Multiple Same Negative Integers

test_item = 'add() + count()'
data_in = [-1,-1,-1,-1]
expected = -1.0
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 7- Positive and Negative Integers

test_item = 'add() + count()'
data_in = [1,-2,-3,4,8,-6]
expected = 0.33333333
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 8- Single Float Number

test_item = 'add() + count()'
data_in = 1.2
expected = 1.2
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 9 - Multiple Positive Float Numbers

test_item = 'add() + count()'
data_in = [1.2,3.1,4.6,5.1]
expected = 3.5
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 10 - Multiple Negative Float Numbers

test_item = 'add() + count()'
data_in = [-1.2,-3.1,-4.6,-5.7]
expected = -3.65
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 11 - Multiple positive and negative float and integers

test_item = 'add() + count()'
data_in = [-1.2,3,4.6,-5, 6, 9.2,-7,2]
expected = 1.45
reason = "Check count after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mean()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))


#####################################################################
# test Statistics.range()

# Test Case 1 - Single positive Interger

test_item = 'range()'
data_in = 5
expected = 0
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 2 - Single Negative Integer

test_item = 'range()'
data_in = -5
expected = 0
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - Single Float Number

test_item = 'range()'
data_in = 5.0
expected = 0
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - Multiple positive Integers

test_item = 'range()'
data_in = [1,2,4,5,6,9]
expected = 8
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 5 - Multiple Negative Integers

test_item = 'range()'
data_in = [-1,-2,-4,-5,-6,-9]
expected = 8
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 6 - Multiple Positive Float Numbers
test_item = 'range()'
data_in = [1.1,2.4,4.6,5.2,6.9,9.5]
expected = 8.4
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 7 - Multiple Negative Float Numbers

test_item = 'range()'
data_in = [-1.1,-2.4,-4.6,-5.2,-6.9,-9.5]
expected = 8.4
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 8- Multiple positive, negative and float numbers

test_item = 'range()'
data_in = [1.1,5,2.4,-1,4.6,5.2,6.9,9.5,5,6,8]
expected = 10.5
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 9 - Multiple same positive integers

test_item = 'range()'
data_in = [1,1,1,1,1,1]
expected = 0
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 10 - Multiple same negative Integers

test_item = 'range()'
data_in = [-1,-1,-1,-1,-1,-1]
expected = 0
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 11 - Multiple same float numbers
test_item = 'range()'
data_in = [1.1,1.1,1.1,1.1,1.1,1.1]
expected = 0
reason = "Check range after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.range()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


#####################################################################
# test Statistics.mode()

# Test Case 1 - Single positive Interger

test_item = 'mode()'
data_in = 5
expected = 5
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mode()

# Test Case 2 - Single Negative Integer

test_item = 'mode()'
data_in = 5
expected = 5
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - Single Float Number

test_item = 'mode()'
data_in = 5.0
expected = 5.0
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.mode()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 4 - Multiple positive Integers

test_item = 'mode()'
data_in = [1,2,2,3,3,3,4,5,6,9]
expected = 3
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 5 - Multiple Negative Integers

test_item = 'mode()'
data_in = [-1,-2,-1,-1,-4,-5,-6,-9]
expected = -1
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 6 - Multiple Positive Float Numbers
test_item = 'mode()'
data_in = [1.1,2.4,4.6,5.2,6.9,9.5, 9.5, 5.2,5.2]
expected = 5.2
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 7 - Multiple Negative Float Numbers

test_item = 'mode()'
data_in = [-1.1,-2.4,-4.6,-5.2,-6.9,-9.5, -9.5, -5.2,-5.2]
expected = -5.2
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 8- Multiple positive, negative and float numbers

test_item = 'mode()'
data_in = [1.1,5,2.4,-1,4.6,5.2,6.9,9.5,5,6,8]
expected = 5
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 9 - Multiple same positive integers

test_item = 'mode()'
data_in = [1,1,1,1,1,1]
expected = 1
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 10 - Multiple same negative Integers

test_item = 'mode()'
data_in = [-1,-1,-1,-1,-1,-1]
expected = -1
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 11 - Multiple same float numbers
test_item = 'mode()'
data_in = [1.1,1.1,1.1,1.1,1.1,1.1]
expected = 1.1
reason = "Check mode after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.mode()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

#####################################################################
# test Statistics.max() 

# Test Case 1 - Single positive Interger

test_item = 'max()'
data_in = 5
expected = 5
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 2 - Single Negative Integer

test_item = 'max()'
data_in = -5
expected = -5
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - Single Float Number

test_item = 'max()'
data_in = 5.0
expected = 5.0
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - Multiple positive Integers

test_item = 'max()'
data_in = [1,2,4,5,6,9]
expected = 9
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 5 - Multiple Negative Integers

test_item = 'max()'
data_in = [-1,-2,-4,-5,-6,-9]
expected = -1
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 6 - Multiple Positive Float Numbers
test_item = 'max()'
data_in = [1.1,2.4,4.6,5.2,6.9,9.5]
expected = 9.5
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 7 - Multiple Negative Float Numbers

test_item = 'max()'
data_in = [-1.1,-2.4,-4.6,-5.2,-6.9,-9.5]
expected = -1.1
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 8- Multiple positive, negative and float numbers

test_item = 'max()'
data_in = [1.1,5,2.4,-1,4.6,5.2,6.9,9.5,5,6,8]
expected = 9.5
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 9 - Multiple same positive integers

test_item = 'max()'
data_in = [1,1,1,1,1,1]
expected = 1
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 10 - Multiple same negative Integers

test_item = 'max()'
data_in = [-1,-1,-1,-1,-1,-1]
expected = -1
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 11 - Multiple same float numbers
test_item = 'max()'
data_in = [1.1,1.1,1.1,1.1,1.1,1.1]
expected = 1.1
reason = "Check max after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.max()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))


#####################################################################
# test Statistics.min() 

# Test Case 1 - Single positive Interger

test_item = 'min()'
data_in = 5
expected = 5
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))


# Test Case 2 - Single Negative Integer

test_item = 'min()'
data_in = -5
expected = -5
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 3 - Single Float Number

test_item = 'min()'
data_in = 5.0
expected = 5.0
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
stats.add(data_in)
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 4 - Multiple positive Integers

test_item = 'min()'
data_in = [1,2,4,5,6,9]
expected = 1
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 5 - Multiple Negative Integers

test_item = 'min()'
data_in = [-1,-2,-4,-5,-6,-9]
expected = -9
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 6 - Multiple Positive Float Numbers
test_item = 'min()'
data_in = [1.1,2.4,4.6,5.2,6.9,9.5]
expected = 1.1
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 7 - Multiple Negative Float Numbers

test_item = 'min()'
data_in = [-1.1,-2.4,-4.6,-5.2,-6.9,-9.5]
expected = -9.5
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 8- Multiple positive, negative and float numbers

test_item = 'min()'
data_in = [1.1,5,2.4,-1,4.6,5.2,6.9,9.5,5,6,8]
expected = -1
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))

# Test Case 9 - Multiple same positive integers

test_item = 'min()'
data_in = [1,1,1,1,1,1]
expected = 1
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 10 - Multiple same negative Integers

test_item = 'min()'
data_in = [-1,-1,-1,-1,-1,-1]
expected = -1
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if result != expected:
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item, expected, result, reason))

# Test Case 11 - Multiple same float numbers
test_item = 'min()'
data_in = [1.1,1.1,1.1,1.1,1.1,1.1]
expected = 1.1
reason = "Check min after one value added"

# call the operation
stats = S.Statistics()
for i in range(len(data_in)):
    stats.add(data_in[i])
result = stats.min()

if not close_enough(expected, result, 0.0001):
    print('Error in {}: expected {} but obtained {} -- {}'.format(test_item,
expected, result, reason))


#####################################################################
print('*** Test script completed ***')