# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.


def string_writer(fileName, inputString):

    if type(inputString) == str:
        try:
            inputFile = open(fileName, 'w')
            newString = inputString * 10
            inputFile.write(newString)
            inputFile.close()
            return True
        except:
            return False
    else:
        raise TypeError('only string type input accepted!')


print(string_writer('tree.txt', 'apple'))
print(string_writer('tree.txt', 1234))          #test by fake data