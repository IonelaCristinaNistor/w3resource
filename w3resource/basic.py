# ----------------- link https://www.w3resource.com/python-exercises/python-basic-exercises.php

# 1 - print text
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# 2 - python version
# import sys
#
# print("Python version ")
# print(sys.version)
# print("Version info. ")
# print(sys.version_info)

# 3 - current Date and Time
# import datetime # for working with date and time
# now = datetime.datetime.now()
# print("Current date and time: ")
# print(now.strftime("%Y-%m-%d %H:%M:%S")) # a specific format
# print(now.astimezone())

# 4 - area of a circle
# from math import pi
# r = float(input("r = "))
# area = pi * (r**2)
# print(f"area of circle = {area:.2f}")

# 5 - reverse full name(first last --> last first)
# firstName = str(input("First name: "))
# lastName = str(input("Last name: "))
# print(f"Hello {lastName} {firstName}")
# print("Hello " + lastName + " " + firstName)

# 6 - List and Tuple generator
# values = input("Input some comma-separated numbers: ")
# listSeq = values.split(",")
# tupleSeq = list(listSeq)
# print("List: ", listSeq)
# print("Tuple: ", tupleSeq)

# 7 - File extension extrator
# filename = input("Input the Filename: ")
# f_ext = filename.split(".")
# print("The extension of the file is: " + repr(f_ext[-1])) # returns the last element in the f_ext, after the "."

# 8 - First and Last Colors
# use the string formatting
# color_list = ["Red", "Green", "White", "Black"]
# print("%s %s" % (color_list[0], color_list[-1]))
# the %s are placeholders that are filled with the values of the color_string[n]

# 9 - Exam schedule formatter
# import datetime
# exam_st_date = (11, 12, 2014)
# print("The examination will start from: %i / %i / %i" % exam_st_date)
# the %i placeholders are filled with the values from the "exam_st_date" tuple

# 10 - Number expansion calculator
# n = int(input("Give a number: "))
# n1 = int("%s" % n) # converts n to an integer
# n2 = int("%s%s" % (n,n))
# n3 = int("%s%s%s" % (n,n,n))
# print(n1 + n2 + n3)

# 11 - Print the documents of Python built-in function(s)
 # Print the docstring (documentation) of the 'abs' function
# print(abs.__doc__)
 # Print the docstring (documentation) of the 'len' function
# print(len.__doc__)
 # Print the docstring (documentation) of the 'sorted' function
# print(sorted.__doc__)
 # Print the docstring (documentation) of the 'sum' function
# print(sum.__doc__)
 # Print the docstring (documentation) of the 'map' function
# print(map.__doc__)
 # Print the docstring (documentation) of the 'filter' function
# print(filter.__doc__)

# 12 - Calendar
# import calendar
# prompt the user to input the year and month
# y = int(input("Input the year: "))
# m = int(input("Input the month: "))
# print the calendar for the specified year and month
# print(calendar.month(y, m))

# 13 - Multi-line string
# print("""
# a string that you "don't" have to escape
# This
# is a ........ multi-line
# heredoc string --------> example
# """)

# 14 - days between dates
# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)

# 15 - sphere volume calculator
# pi = 3.14
# r = 6.0
# V = 4.0/3.0 * pi * r**3
# print(f"The volume of the sphere is: {V:.2f}")

# 16 - difference from 17
# number = int(input("Give a number: "))
# if number <= 17:
#     print(17-number)
# else:
#     print((number - 17)*2)

# ----- with function
# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n - 17) * 2
# print(difference(22))
# print(difference(14))

# 17 - Test whether a number is within 100 or 1000 or 2000 using abs()
# Define a func that takes an integer parameter "n"
# def near_thousand(n):
# Check if the absolute difference between 1000 and n is less than or equal to 100
# OR check if the absolute difference between 2000 and n is less than or equal to 100
#     return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))

# 18 - Triple Sum Calculator
# def triple_sum(x, y, z):
#     sum_t = x + y + z
#     if x == y == z:
#         sum_t = sum_t * 3
#     return sum_t
# print(triple_sum(1, 2, 3))
# print(triple_sum(3, 3, 3))

# 19 - Get a new string from a given string where 'Is' has been added to the front.
# If the given string already begins with 'Is' then return the string unchanged
# def new_string(text):
# Check if the length of the text is greater than or equal to 2
# and if the first two characters of "text" are "Is"
#     if len(text) >= 2 and text[:2] == 'Is':
# If the conditions are met, return the original "text" unchanged
#         return text
#     else:
# If the conditions are not met, prepend "Is" to the "text" and return the modified string
#         return 'Is' + text
# print(new_string("Array"))
# print(new_string("IsEmpty"))

# 20 - String Copy Generator
# def larger_string(text, n):
#     result = ""
#     for i in range(n):
#         result = result + text
#     return result
# print(larger_string('abc', 2))
# print(larger_string('.py', 25))

# 21 - Even or Odd Checker
# def even_or_odd(x):
#     if x % 2 == 1:
#         return "Odd"
#     else:
#         return "Even"
#
# print(even_or_odd(2))
# print(even_or_odd(3))

# ------- with list ---------
# def list_count_4(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count += 1
#     return count
# print(list_count_4([1, 4, 6, 7, 4]))
# print(list_count_4([1, 4, 6, 4, 7, 4]))

# Write a Python program to count occurrences of a specific digit in a list.
# def list_count(nums, n):
#     count = 0
#     for num in nums:
#         if num == n:
#             count += 1
#     return count
# n = int(input("Give a number to count: "))
# print(list_count([1, 4, 6, 7, 4], n))
# print(list_count([1, 4, 6, 4, 7, 4], n))

# Write a script to count how many numbers in a list are divisible by 4
# def list_count(nums):
#     count = 0
#     for num in nums:
#         if num % 4 == 0:
#             count += 1
#     return count
# print(list_count([1, 4, 6, 7, 4, 16, 32]))
# print(list_count([1, 4, 6, 4, 7, 4, 64]))

# Write a Python program to count how many numbers in a list contain digit 4.
# def list_count(nums):
#     count = 0
#     for num in nums:
#         if '4' in str(abs(num)):
#             count += 1
#     return count
# print(list_count([14, 24, 12, 25, 34, 44]))

# Write a function that finds the most frequently occurring number in a list.
def list_count(nums):
    if not nums:
        return None
    freq = {} # empty dictionary
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        # check if "num" already exists in the dictionary
        # if it does, it returns the current count
        # if it doesn't, it returns 0
        # then it adds 1 to that count and stores it back in freq[num]
    most_freq = max(freq, key=freq.get)
    return most_freq
nums_list = [1, 3, 2, 3, 4, 3, 2, 1]
print("Most frequent number: ", list_count(nums_list))