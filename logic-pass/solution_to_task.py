# Q1/Write a method that will remove any given character from a String.
def remove_char(my_string,removed_char):   
    if removed_char in my_string:
        my_string=my_string.replace(removed_char,'')
        print(my_string)
    else:
        print('The character you entered is not in the string')

my_string='this is a test string that contains a number of words'
print(f'The current string is "{my_string}"')
removed_char=input('Enter a character to be removed from the string: ')
remove_char(my_string,removed_char)


#Q2/Write a program to find all prime numbers up to a given range of numbers?
def find_primes(num):
    prime_numbers = []
    for number in range(1,num): 
        if number > 1:
            for n in range(2, number):
                if (number % n) == 0:
                    break
            else:
                prime_numbers.append(number)
    return prime_numbers

num=int(input('Enter a number: '))
print(find_primes(num))


#Q3/write a function that count how many the given character repeated in a given string?
def count_char(my_string,char):   
    count=my_string.count(char)
    if count:
        print(f'the character appeared {count} times in the string')
    else:
        print('The character you entered is not in the string')

my_string='this is a test string that contains a number of words'
print(f'The current string is "{my_string}"')
char=input('Enter a character to be counted in the string: ')
count_char(my_string,char)
