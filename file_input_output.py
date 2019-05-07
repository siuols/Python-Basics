def init():

    infile = "Input.txt"
    sample = list()
    with open(infile) as f1:
        for line in f1:
            row = line.split(",")
            sample.append(row)
        print(sample)

    input_to_output()
    input_to_writer_ouput_not_appending()
    input_to_writer_ouput()
    input_reader()

def input_data():
    input_value = input("Enter your full name: ")
    return input_value

def input_to_output():
    entered=input_data()
    print("Received Input is: " + entered)

def input_reader():
    with open('Input.txt','r') as output:
        lists = output.read()
        print (lists)
        output.close()

def writer_data(entered):
    with open('Output.txt', 'w') as output:
        output.write(entered + '\n')
        output.close()
    print("{} is written to Output.txt".format(entered))

def output_writer(entered):
    with open('Output.txt', 'a') as output:
        output.write(entered + '\n')
        output.close()
    print("{} is written to Output.txt".format(entered))

def input_to_writer_ouput_not_appending():
    entered=input_data()
    writer_data(entered)

def input_to_writer_ouput():
    entered=input_data()
    output_writer(entered)

init();