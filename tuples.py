def init():
    num = []
    list_tuple = ()
    try:
        num.append(input("Enter first string: "))
        num.append(input("Enter second string: "))
        num.append(input("Enter third string: "))
        num.append(input("Enter fourth string: "))
        list_tuple = tuple(num)
        indexing(list_tuple)
        negative_indexing(list_tuple)
        slicing(list_tuple)
        combining_tuples(list_tuple)
        cos(list_tuple)
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


init()