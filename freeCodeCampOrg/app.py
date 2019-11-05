# 4 hr youtube video by freeCodeCamp.org

# Hello world
'''
print("Hello world")
'''

# Drawing a shape
'''
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
'''

# Variable and data type
'''
character_name = 'Tenpato'
character_age = 45
ia_male = True

print('Hey my name is ' + character_name + ',')
print('I am ' + character_age + ' years old.')
print('i like the name '+ character_name + ', ')
print("but didn't like being " + character_age + ". ")
'''
# Working with strings
'''
phrase = "Tenzin"
print(phrase + ' is cool')

print('Master\nTenzin')  # New line
print('Master\"Tenzin')  # \ as escape character

x = 'tsundue'
print(x.upper())  # upper is function
print(x.isupper())  # isupper
print(x.islower())  # islower
print(x.upper().isupper())
print(len(x))
print(x[0:3])
print(x.index('u'))  # index
print(x.replace('tsun', 'Son'))
'''

# Working with numbers

'''
my_num = 5
print(-2.09)
print(2* (3+2))
print(my_num)
print(my_num + 3)
string_my_num = str(my_num)
print(string_my_num)

x = -5.56
y = -5
print(abs(x)) # absolute (make it positive)
print(abs(y))
print(pow(3,2)) # power
print(max(4, 6))
print(min(4, 6))
print(round(x)) # round up/down properly
print(abs(round(x))) # fucntion stacking possible 

from math import *
print(floor(3.7))  # round down
print(ceil(3.3))    #round up
print(sqrt(64))     # square root
'''

# Getting input from the user
'''
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print('Hello ' + user_name + '!' '\nyou are ' + user_age )
'''

# Building a basic calculator
'''
num1 = input('Enter a number: ')
num2 = input('Enter a another number: ')
result = float(num1) + float(num2)   #float for decimal number
print(result)
'''

# Mad libs game
'''
color = input('Enter a color: ')
plural_noun = input('Enter a Plural Noun: ')
celebrity = input('Enter a celebrity: ')

print('\nRoses are ' + color)
print(plural_noun + ' are blue')
print('I love ' + celebrity)
'''

# Lists
'''
friends = ['max', 'tyson', 'ray', 'kai', 'dragoon', 'drawnzer', 'driger', 'draciel']
can_be = ['max', 23, True]
print(friends)
print(friends[1])
print(friends[-1])  # print last item
print(friends[0:4]) 
friends[5] = 'Black_drawnzer' # replace 6th position with new item
print(friends)
'''

# List Functions
'''
lucky_numbers = [4, 6, 3, 9]
friends = ['max', 'tyson', 'ray', 'kai']
friends.extend(lucky_numbers) # join two list
friends.append(12) # adding end of the list
friends.insert(4, 'kelly') #insert
print(friends) 
friends.remove('kelly') #remove
print(friends)
friends.pop()  #remove the last element #pop 
print(friends)
print(friends.index('ray')) #index
print(friends.count('ray')) #count
lucky_numbers.sort() #sort
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy() #copy
print(friends2)
'''

# Tuples
# tuples is immutable
'''
coordinates = (4, 5)
print(coordinates[1])
coordinates = [(4, 5), (5, 6), (6, 7)]
print(coordinates)
'''

# Functions
'''
def say_hi(name):    #with parameter name
    print('Hi '+ name + '!')
say_hi('mike')
'''

# Return Statement
'''
def cube(num):
    return num * num * num
    print('apple') #will not print cus return will escape the function
result = cube(4)
print(result)
'''

# If Statements
'''
is_male = True
if is_male:
    print("you are a Male")
else:
    print("you not a Male")

is_tall = True
if is_male and is_tall:
    print ('you are a tall male')
elif is_male and not(is_tall):
    print('you are short male')
elif not(is_male) and is_tall:
    print('you are not male but tall')
else:
    print('you are not male and not tall')
'''

# If statements and Comparisons
'''
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # == equal != not equal (Operators) 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(2,4,122))
'''

# Building a better Calculator
'''
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
operator = input('Enter the operator + - * / :')

if operator == '+':
    print('result: ', float(num1)+float(num2))
elif operator == '-':
    print('result: ', float(num1)-float(num2))
elif operator == '*':
    print('result: ', float(num1)*float(num2))
elif operator == '/':
    print('result: ', float(num1)/float(num2))
else:
    print('Invalid Operator')
'''
'''
def calculator(num1, num2, operator):
    if operator == '+':
        print('result: ', float(num1) + float(num2))
    elif operator == '-':
        print('result: ', float(num1) - float(num2))
    elif operator == '*':
        print('result: ', float(num1) * float(num2))
    elif operator == '/':
        print('result: ', float(num1) / float(num2))
    else:
        print('Invalid Operator')

calculator(4,2,'-')
'''

#Dictionaries
#key value pair
'''
month_conversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print(month_conversions['Mar'])
#print(month_conversions['Mar']) # will show error
print(month_conversions.get('Dec'))
print(month_conversions.get('Luv'))
'''

# While loop
'''
i = 1
while i <= 10:
    print(i)
    i += 1
print('Done with the loop')
'''

# Building a guessing game
'''
secret_word = "giraffe"
guess = ""
n=1
hint = ['Nan','Its an animal','its a wild animal','its a herbivore animal', 'its has pattern skin', 'its a tall animal', 'Its a god dame Giraffe !' ]
print('Guessing game')
print('You will get 5 chance with hint on each steps')
print('all the character should be in small letter')
i = 1
while i <= 5:
    print(i , 'Hint', hint[i])
    guess = input('Enter guess: ')
    if guess != secret_word:
        print(' Wrong!, Try again')
    elif guess == secret_word:
        print('CORRECT, YOU WON!')
        break
    i += 1
print(hint[6])
'''
'''
secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter guess: ')
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print('You are out of guesses, You lose!')
else:
    print('you win!')
'''

# For loops
'''
for i in range(5):
    print(i)
'''
'''
for i in range(3,10):
    print(i)
'''
'''
for letter in 'Tenzin Tsundue':
    print(letter)
'''
'''
friends = ['Jim', 'Karen', 'Kevin']
print(len(friends))
for index in range(len(friends)):
    print(friends[index])
'''
'''
for index in range(5):
    if index == 0:
        print('First Iteration')
    else:
        print('Not first')
'''

# Exponent Function
'''
print(2**3)

def raise_to_power(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    print(result)
raise_to_power(2,5)
'''

# 2D lists & Nested loops
'''
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, [10, 11, 12]]
]
#print(number_grid[0][1])

for row in number_grid:
    for col in row:
        print(col)
'''

# Build a basic translator
# all vowel to t
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                translation = translation + 'T'
            else:
                translation = translation + 't'
        else:
            translation = translation + letter
    return  translation
print(translate(input('Enter a phrase: ')))
'''

# Comments
# this is a comments
'''
Multiple line
commnets
'''

# Try Except
'''
try:
    number = int(input('Enter a number'))
    print(number)
except:
    print('Invalid Input')
'''
'''
try:
    value = 10/0
    number = int(input('Enter a number'))
    print(number)
except ZeroDivisionError:
    print('Divided by zero')
except ValueError:
    print('Invalid input')
'''

# Reading files
'''
employee_file = open('employee.txt', 'r')   #r for read and w for write and a for append and r+ read and write

print(employee_file.readable()) # show is it readable or not

#print(employee_file.read()) #read entire file

#print(employee_file.readline()) #read a line
#print(employee_file.readline()) #read next line

print(employee_file.readlines()[1])

employee_file.close() #always close the file
'''

# Writing to Files
'''
employee_file = open('employee.txt', 'a')
print(employee_file.write("\nMango text"))
employee_file.close()
'''
'''
employee_file = open('employee.txt', 'w')  #write will overwrite the file 
print(employee_file.write("kiwi text"))    # can create new file with w 
employee_file.close()
'''

# Modules and Pip
#python module list link https://docs.python.org/3/py-modindex.html#cap-r
'''
import usefull_tools as ut

print(ut.roll_dice(10))
print(ut.get_file_ext('tenzin.txt'))
'''
'''
in terminal
pip install python-docx
'''

# Classes and objects

from student import Student   #from student file import Student Class
'''
student1 = Student('Jin', 'Computer Science', 4.3, False)
student2 = Student('Panta', 'Art', 3.3, False)

print(student1.name)
print(student2.gpa)
'''

# Building a Multiple Choice Quiz
'''
from Question import Question

question_prompts = [
    "what color are apples ? \n (a) Red/Green\n (b) Purple\n (c) Orange \n\n",
    "what color are Banana ? \n (a) Teal\n (b) Magenta\n (c) yellow \n\n",
    "what color are Strawberries ? \n (a) Yellow\n (b) Red\n (c) Blue \n\n",
]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    print("you got: " + str(score) + "/" + str(len(questions)) + ' correct')

run_test(questions)
'''

# Class Fuctions
'''
from student1 import Student1

student01 = Student1('Oscar', 'Accounting', 3.3)
student02 = Student1('Phill', 'Business', 4.1)

print(student02.on_honor_roll())
'''

# Inheritance
'''
from Chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()
my_chef.make_special_dish()   #calling class function

my_chinese_chef = ChineseChef()
my_chinese_chef.make_chicken()
my_chinese_chef.make_special_dish()
'''

# Python interpreter
'''
terminal
python3
'''







