def init():
    try:
        trinal = float(input("Enter Trinal Grade:"))
        midterm = float(input("Enter Midterm Grade:"))
        final = float(input("Enter Final Grade:"))
        average = (trinal + midterm + final) / 3
        print(average)
    except ValueError:
        print("Please enter a valid value.")

    if average >= 0 and average <= 100:
        perfect_grade(average)
        excellent_grade(average)
        great_grade(average)
        good_grade(average)
        average_grade(average)
        barely_pass_grade(average)
        almost_passed_grade(average)
        fail_grade(average)
        withdrawal(average)
    else:
        print("Please enter between 1-100")

def perfect_grade(average):
    if(average == 100):
        print("The student got a perfect grade")

def excellent_grade(average):
    if(average >= 95 and average < 100):
        print("The student got a excellent grade")

def great_grade(average):
    if(average >= 90 and average < 95):
        print("The student got a great grade")

def good_grade(average):
    if(average >= 85 and average < 90):
        print("The student got a good grade")

def average_grade(average):
    if(average >= 80 and average < 85):
        print("The student a an average grade")

def barely_pass_grade(average):
    if(average >= 75 and average < 80):
        print("The student got a barely passed grade")

def almost_passed_grade(average):
    if(average >= 70 and average < 75):
        print("The student got a almost passed grade")

def fail_grade(average):
    if(average >= 65 and average < 70):
        print("This student got a failing grade.")

def withdrawal(average):
    if(average >= 60 and average < 65):
        print("This student failed")

init()