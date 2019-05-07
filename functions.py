def init():
    calling_a_function("Hello world!")
    return_function()
    my_list = [10,20,30]
    pass_reference_function(my_list)
    keyword_function(age=20, name="louis")
    return_variable = function_with_return("Parameter")
    print(return_variable)
    function_with_default_parameter("Parameter")
    total(1,2)

def calling_a_function(str):
   print(str)
   return

def return_function():
    return "Returning Solo"

def pass_reference_function(my_list):
    my_list.append([1,2,3,4])
    print("Values inside the function: {}".format(my_list))
    return

def keyword_function(name, age):
    print("Name: ", name)
    print("Age ", age)
    return

def function_with_return(parameter):
    parameter = "Return value"
    return parameter

def function_with_default_parameter(not_default,default_parameter = "default parameter"):
    print(not_default)
    print(default_parameter)

total = lambda arg1, arg2: print(arg1 + arg2);

init()