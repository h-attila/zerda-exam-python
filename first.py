# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].


def second_element_function(inputList):
    if type(inputList) == list:
        return inputList[1::2]
    else:
        raise TypeError('only list type input accepted!')


testList = [1, 2, 3, 4, 5]
print(second_element_function(testList))

testFakeList = 'alma'
print(second_element_function(testFakeList))