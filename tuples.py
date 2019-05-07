def init():
    num = []
    list_tuple = ()
    try:
        num.append(int(input("Enter first number: ")))
        num.append(int(input("Enter second number: ")))
        num.append(int(input("Enter third number: ")))
        num.append(int(input("Enter fourth number: ")))
        list_tuple = tuple(num)
        indexing(list_tuple)
        negative_indexing(list_tuple)
        slicing(list_tuple)
        combining_tuples(list_tuple)
        tuple_list_count(list_tuple)
        search_specific_word_tuple(list_tuple)
        maximum_number(list_tuple)
        minimum_number(list_tuple)
        multiplying_tuple(list_tuple)
        deleting_element(list_tuple)

    except ValueError:
        print("Invalid input")

def indexing(list_tuple):
    print("\nIndexing")
    print(list_tuple[0])
    print(list_tuple[3])

def negative_indexing(list_tuple):
    print("\nNegative Indexing")
    print(list_tuple[-1])
    print(list_tuple[-3])

def slicing(list_tuple):
    print("\nSlicing")
    print(str(list_tuple[0:3]))

def combining_tuples(list_tuple):
    another_tuple = tuple(list_tuple)
    another_tuple = another_tuple + another_tuple
    print("Combining two tuples : " + str(another_tuple))

def tuple_list_count(list_tuple):
    print(list_tuple, 'length is', len(list_tuple))

def search_specific_word_tuple(list_tuple):
    if "louis" in list_tuple:
        print("'louis' is on the tuple {}.".format(list_tuple))
    else:
        print("'louis' is not found on the tuple {}.".format(list_tuple))

def maximum_number(list_tuple):
    print ("The maximum value of the tuple is {}.".format(max(list_tuple)))

def minimum_number(list_tuple):
    print ("The minumum value of the tuple is {}.".format(min(list_tuple)))

def multiplying_tuple(list_tuple):
    print("Multiplying the tuple by 2 looks like this {}.".format(list_tuple * 2))

def deleting_element(list_tuple):
    lists = list(list_tuple)
    del lists[2]
    conv_tuple = tuple(lists)
    print("deleting {} in a tuple {}.".format(conv_tuple, list_tuple))

init()