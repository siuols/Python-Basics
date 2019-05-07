def init():
    input_string = input("Enter a string: ")
    count = 0
    upper_string(input_string)
    lower_string(input_string)
    count_string(input_string)
    convertion_to_list(input_string)
    indexing(input_string)
    count_string(input_string)
    reverse(input_string)
    slicing(input_string)
    start_end(input_string)
    split(input_string)

def upper_string(input_string):
    upper = input_string.upper()
    print("String {} is uppered case.".format(upper))

def lower_string(input_string):
    lower = input_string.lower()
    print("String {} is lowered case.".format(lower))

def count_string(input_string):
    print("the total length of {} is : {}".format(input_string, len(input_string)))

def convertion_to_list(input_string):
    string_list = list(input_string)
    print(string_list)

def indexing(input_string):
    #this method only recognizes the first 'o'.
    print("number of 'o' is {} is: {}".format(input_string, input_string.index("o")))

def count_string(input_string):
    #this method counts the all 'l or L' in the string
    print("number of 'l' is {} is: {}".format(input_string,input_string.count("l")))

def reverse(input_string):
    reverse_word = ""
    i = len(input_string)-1
    while(i != -1):
        reverse_word += input_string[i]
        i-=1
    print("The reverse string of {} is {}".format(input_string, reverse_word))

def slicing(input_string):
    #This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].
    print("string from 3 to 7 skipping one character is: " + input_string[3:7:1])

def start_end(input_string):
    #This is used to determine whether the string starts with something or ends with something, respectively. The first one will print True,
    print("if the inputted string starts with 'hello' it will return to : {}".format(input_string.startswith("Hello")))
    print("if the inputted string starts with 'hello' it will return to : {}".format(input_string.endswith("world")))

def split(input_string):
    #This splits the string into a bunch of strings grouped together in a list.
    word = input_string.split(" ")
    print(word)

init()