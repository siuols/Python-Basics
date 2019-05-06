def init():
    num = []
    dictionary_list = {}
    num.append(int(input("Enter first number: ")))
    num.append(int(input("Enter second number: ")))
    num.append(int(input("Enter third number: ")))

    dictionary_list = {
        "first_num" : num[0],
        "second_num" : num[1],
        "third_num" : num[2]
    }

    updating_value(dictionary_list)
    adding_value(dictionary_list)
    deleting_value(dictionary_list)
    searching_key(dictionary_list)
    replacing_key_in_the_dictionary(dictionary_list)
    return_keys(dictionary_list)

def adding_value(dictionary_list):
    dictionary_list['fourth_num'] = 20
    print("Added value to the dictionary : " + str(dictionary_list))

def updating_value(dictionary_list):
    dictionary_list['third_num'] = 20
    print("The last value on the dictionary was updated into 20, " + str(dictionary_list))

def deleting_value(dictionary_list):
    del dictionary_list['second_num'];
    print("Deleting a value from the dictionary : " + str(dictionary_list))

def replacing_key_in_the_dictionary(dictionary_list):
    dictionary_list["second_num"] = dictionary_list.pop("third_num")
    print("Replaced second_num key into Laundry key : " + str(dictionary_list))

def searching_key(dictionary_list):
    if "third_num" in dictionary_list:
        print("third_num is found in the dictioanary!")
    else:
        print("third_num is not found in the dictionary!")

def return_keys(dictionary_list):
    print("List of all keys in the dictionary are : " + str(dictionary_list.keys()))


init()