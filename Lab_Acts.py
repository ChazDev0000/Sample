# Exercise 1: Calculate the multiplication and sum of two numbers

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def get_thesum():
    return num1 + num2

def get_product():
    return num1 * num2

sum_result = get_thesum()
product_result = get_product()

print(f"The sum of {num1} and {num2} is {sum_result}")
print(f"The product of {num1} and {num2} is {product_result}")
print(" ")

#Exercise 2: Print the sum of the current number and the previous number

previous = 0
current = 0

while True:
    user_input = input("Enter a number (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    previous = int(current)
    current = int(user_input)
    Sum_prev_curr = previous + current

print(f"The sum of previous and current number is: {Sum_prev_curr}")

print(" ")

#Exercise 3: Print characters from a string that are present at an even index number

def even_index(input_string):
    even_chars = input_string[1::2] 
    #even_chars = ''.join(char for char in even_chars if char != ' ') //remove comment if you you dont' want spaces to be counted in counting for even 
    print(even_chars)


user_input = input("Enter a word or sentence: ")
even_index(user_input)

print(" ")

#Exercise 4: Remove first n characters from a string

def remove_firstString(input_string, n):
    result_string = input_string[n:]
    return result_string

input_string = input("Enter a string: ")

n = int(input("Enter the number of characters to remove: "))

new_string = remove_firstString(input_string, n)

print(new_string)

print(" ")

#Exercise 5: Check if the first and last number of a list is the same

def check_firstLast(input_list):
    return input_list[0] == input_list[-1]

user_input = input("Enter a list of numbers: (space seprated) ")
user_list = [int(x) for x in user_input.split(' ')]

result = check_firstLast(user_list)

if result:
    print("The first and last elements are the same.")
else:
    print("The first and last elements are different.")

print(" ")

#Exercise 6: Display numbers divisible by 5 from a list

def check_divisible(input_list):
    divisible = [num for num in input_list if num % 5 == 0]
    return divisible

user_input = input("Enter a list of numbers (space separated): ")
user_list = [int(x) for x in user_input.split(' ')]

divisible = check_divisible(user_list)


print(f"The numbers divisible by 5 are: {divisible}")