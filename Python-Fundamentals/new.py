s1='MY string'
s2='2nd string' 
#print(s1)
#print()
print(s1,end='     ')
#print(s1,end='@')
#print(end='@')
print(s2)

#python string
#reverse string
print(s1[::-1],end='@')

# captalize first word capital
#title every word capital

print(s2.split())
print(s2.title())
print(s2.capitalize())
#
""""
Case Conversion   also try swap case
capitalize(): Capitalizes the first character, lowercases the rest.

casefold(): Converts to lowercase aggressively for caseless matching.

lower(): Converts all characters to lowercase.

swapcase(): Swaps uppercase to lowercase and vice versa.

title(): Capitalizes first letter of each word.

upper(): Converts all characters to uppercase.
​

Alignment and Padding
center(width, fillchar=' '): Centers the string with padding.

ljust(width, fillchar=' '): Left-justifies with padding.

rjust(width, fillchar=' '): Right-justifies with padding.

zfill(width): Pads with zeros on the left.
​

Trimming
lstrip(chars=None): Removes leading whitespace or specified chars.

rstrip(chars=None): Removes trailing whitespace or specified chars.

strip(chars=None): Removes both leading and trailing whitespace or chars.
​

Splitting and Joining
join(iterable): Joins elements with the string as separator.

partition(sep): Splits into three parts at first separator.

rpartition(sep): Splits into three parts at last separator.

split(sep=None, maxsplit=-1): Splits on separator or whitespace.

rsplit(sep=None, maxsplit=-1): Splits from right.

splitlines(keepends=False): Splits on line breaks.
​

Searching
endswith(suffix): Checks if string ends with suffix.

find(sub): Returns lowest index of substring or -1.

index(sub): Like find but raises ValueError if not found.

rfind(sub): Returns highest index of substring or -1.

rindex(sub): Like rfind but raises ValueError.

startswith(prefix): Checks if string starts with prefix.
​

Inspection (Boolean)
isalnum(): All alphanumeric.

isalpha(): All alphabetic.

isascii(): All ASCII.

isdecimal(): All decimal.

isdigit(): All digits.

isidentifier(): Valid identifier.

islower(): All lowercase.

isnumeric(): All numeric.

isprintable(): All printable.

isspace(): All whitespace.

istitle(): Title-cased.

isupper(): All uppercase.
​

Other Utilities
count(sub): Counts non-overlapping occurrences.

encode(encoding='utf-8'): Encodes to bytes.

expandtabs(tabsize=8): Expands tabs to spaces.

format(*args): Formats with placeholders.

format_map(mapping): Formats with dict.

maketrans(x, y=None): Creates translation table.

replace(old, new): Replaces occurrences.

translate(table): Translates chars.
​"""

text = "hello"
chars = list(text)
chars[1] = chars[1].upper()
result = ''.join(chars)
print(result)  # Output: "hEllo"

"""
Method	                     Input	               Output/Example
add(element)	          Single element	Adds to set, no change if exists: {1,2}.add(3) → {1,2,3} 
​
update(iterable)       	List/tuple/set	    Adds multiple: {1}.update([2,3]) → {1,2,3} 
​
remove(element)     	Single element	    Removes or raises KeyError: {1,2}.remove(1) → {2} 
​
discard(element)	    Single element	    Removes safely: {1,2}.discard(3) → {1,2} (no error) 
​
pop()	None	    Removes/returns         random element: {1,2}.pop() → {2} returns 1 
​
clear()	None    	Empty set:              {1,2}.clear() → set() 
"""
# Single items work same 
#​ extend and append
lst = [1, 2]

# append() - adds entire list as ONE element
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]]

# Reset and use extend()
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]


"""
Complete List of Set Methods
add() - Adds single element

clear() - Removes all elements

copy() - Returns shallow copy

difference() - Elements only in first set (-)

difference_update() - Removes elements found in another set

discard() - Removes element (no error if missing)

intersection() - Common elements (&)

intersection_update() - Keeps only common elements

isdisjoint() - Returns True if no common elements

issubset() - True if all elements in other set (<=)

issuperset() - True if contains all other elements (>=)

pop() - Removes/returns random element

remove() - Removes element (KeyError if missing)

symmetric_difference() - Elements in either set (^)

symmetric_difference_update() - Keeps elements in either set

union() - All elements from both (|)

update() - Adds multiple elements (|=) 
​

Quick Categories
Add/Modify: add(), update()
Remove: discard(), remove(), pop(), clear()
Operations: union(), intersection(), difference(), symmetric_difference()
Test: issubset(), issuperset(), isdisjoint()

"""




"""
Dictionary Methods: Input & Output
Method       	Input Parameters	                  Example Code	                 Output Result
clear() 	                None	                 d.clear()	                    {} (empty dict)
copy()	                    None	                d.copy()	                    {'a': 1, 'b': 2} (new copy)
fromkeys(keys, value)   	['x','y'], 0        	dict.fromkeys(['x','y'], 0) 	{'x': 0, 'y': 0}
get(key, default)       	'age', 'N/A'        	d.get('age', 'N/A')             25 or 'N/A'
items()                    	None	                d.items()   	                dict_items([('name', 'John'), ('age', 25)])
keys()                  	None	                d.keys()	                    dict_keys(['name', 'age'])
pop(key, default)	        'age', None	            d.pop('age')	                25 (removes key)
popitem()	                None	                d.popitem()	                    ('city', 'NYC') (last pair)
setdefault(key, default)	'job', 'dev'	        d.setdefault('job')           	None (adds 'job': None)
update(other_dict)      	{'z': 3}	            d.update({'z': 3})	            None (merges data)
values()	                   None	                d.values()	                    dict_values(['John', 25])

"""
#Test it:
#tule can not be modifie


d = {'name': 'John', 'age': 25}
print(d.get('name'))     # 'John'
print(d.pop('age'))      # 25


#dictinary
fruits = {'apple': 100, 'banana': 80}
print(fruits.get('apple'))  # 100
print(fruits.pop('banana')) # 80

#tuple
t = ('apple', 'banana', 42)  
print(t[0])     # 'apple'  
# print(t.pop(1)) # AttributeError [web:11]

#list
l = ['apple', 'banana', 42]  
print(l[0])     # 'apple'  
print(l.pop(1)) # 'banana' [web:11]

#INT STRING MUTABLE AND INMUTABLE

#create a system that tells u wheather u are qua;ified for entrance or  ot stae ,marks 
#  maths and science  condition if belong to  taotal >120
#if belong to gujrat >110 and check age>20 for delhi >22 and disqualified also

#write a program that checks if a given number
#ai virtual activity 
#reginal showcase


#Write a function calculate average that takes a ist of numbers as an argument and returns the average of the numbers. Then, use this function to calculate the average of a list of scores

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage with scores
scores = [85, 92, 78, 96, 89]
average = calculate_average(scores)
print(f"The average of {scores} is {average}")  # Output: 88.0



#Write a function multiply_list that takes a list of numbers and a multiplier as arguments and returns a new list with each number multiplied by the multiplier Then, use this function to multiply a list of prices by 1.2 (to add 20% tax)
def calculate_average(numbers):
    if len(numbers) == 0:  # Check empty list first
        return 0
    return sum(numbers) / len(numbers)

scores = [85, 92, 78]
print(f"Scores count: {len(scores)}")  # 3
print(f"Average: {calculate_average(scores)}")  # 85.0



# pattern to create star r*c
#function
def bar(l):
    r=max(l)
    c=len(l)
    for i in range(r):
        for j in range(c):
            print('*' ,end='  ')

        print()
bar([2,5,0,6])

#bar graph problem
#function
def bar(l):
    r = max(l)
    c = len(l)
    for i in range(r):
        for j in range(c):
            if l[j]+i>=max(l):
                print('*', end='  ')
            else:
                print(' ',end='  ')
        print()

bar([2,5,0,6])
"""
output:
         *
   *     *
   *     *
   *     *
*  *     *
*  *     *
2  5  0  6
"""
 
#file handeling
with open('abc.txt','r')as file:
    content = file.read()
    print(content)
file.close()


"""
| Mode | Purpose             | Behavior if File Exists      | Behavior if No File  |
| ---- | ------------------- | ---------------------------- | -------------------- |
| 'r'  | Read (input) only   | Opens from start             | Error (FileNotFound) |
| 'w'  | Write (output) only | Truncates/overwrites content | Creates new file     |
| 'a'  | Append (output)     | Adds to end                  | Creates new file     |
| 'r+' | Read + Write        | Allows both, no truncate     | Error                |
| 'w+' | Write + Read        | Truncates, allows both       | Creates new file     |
| 'a+' | Append + Read       | Allows both, writes to end   | Creates new file     |
"""

def fileh(age,marks,state,E):
    import time
    with open('abc.txt', 'a') as file:
        time=time.ctime()
        file.write(f'\n{age},{marks},{state},{time},{E}')
    file.close()
def eligibility_checker():
    print('Welcome to Eligibility Checker!')
    E='Eligible'
    for i in range(1,11):
        age = int(input(f'Enter the age : '))
        Marks=float(input(f'Enter the marks obtained'))
        state=input(f'Enter the state (GJ for Gujarat,DL for Delhi, O for Others): ')
        if age <=20 and Marks>=60 : 
            print('You are eligible to apply!')
            E='Eligible'
        elif age<=20 and Marks>=50 and state=='GJ':
            print('You are eligible to apply!')
            E='Eligible'
        elif age<=22 and Marks>=60 and state=='DL':
            print('You are eligible to apply!')
            E='Eligible'
        else:
            print('You are not eligible to apply!')
            E='Not Eligible'
        fileh(age,Marks,state,E)
        choice=input('Do you want to check another eligibility (Y/N)? ')
        if choice.upper() != 'Y':
            break
    print('Thank you for using Eligibility Checker!')

eligibility_checker()

#activity
#Q1 Write a program that writes a list of tuples, each containing a student's name and grade, to a text file. Each line in the file should contain the student's name and grade separated by a comma. Assume the file is named 'students.txt' and the list of students is predefined.
#Ans 1:
# Predefined list of tuples with student data
students = [
    ('John Doe', 85.5),
    ('Jane Smith', 92.0),
    ('Bob Johnson', 78.5),
    ('Alice Brown', 95.0)
]

# Write students data to text file
with open('students.txt', 'w') as file:
    for name, grade in students:
        file.write(f"{name},{grade}\n")


#Q2 Write a program that reads a CSV file named 'product.csv' containing products and their prices. The program should calculate the total cost of all products by summing the price values and print the result formatted to two decimal places. Assume the file has a header row that should be skipped
# answer 2:
#def calculate total_cost(filename):
total_cost = 0.0  # Initialize as float for decimal sums

with open('products.csv', 'r') as file:
    next(file)  # Skip header row (assumes first line is header)
    for line in file:
        product, price = line.strip().split(',')
        total_cost += float(price)  # Fixed: =+ to +=

print(f"Total cost: ${total_cost:.2f}")  # Fixed formatting syntax

