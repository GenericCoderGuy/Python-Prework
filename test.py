# # Qustion 1 Solution
def hello_name(user_name):
    print("hello_" + user_name +"!")

hello_name("Wei")
hello_name("Maui")


# Qustion 1 Input Solution
# def hello_names():
#     name = input("Enter Name: ")
#     print("hello_" + name +"!")

# hello_names()


# Question 2: Write a python function,
# first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for x in range(1, 101):
        if(x % 2 == 1):
            print(x)
first_odds()

# Question 3: Please write a Python function,
# max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    LowestNum = a_list[0]
    for x in a_list:
        print(x)
        if (x < LowestNum):
            LowestNum = x
    return LowestNum

print (max_num_in_list([50, 1, 41, 100]))

# Question 4: Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
# The return should be boolean Type (true/false). def is_leap_year(a_year):

# def is_leap_year(a_year):
    
#     if(a_year == )
