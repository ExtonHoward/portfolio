
#These are various functions I wrote for practice, generally either from my courses or on CodeWars

#Counting the number of instances of a character in a string
def count_char (string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    print (count_dict)

count_char("hello")


#Returning any names that would be put as duplicate in a list
def return_duplicates(list):
    dups = []
    a_set = set()
    for item in list:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups

a_list = ['Susan','Tommy','Melissa','Susan','Kwame','Tommy','Bryan']
dupes = return_duplicates(a_list)
print (dupes)

#Returns the name of the plane based upon the dictionary
def planet_name(id):
    return {1:"Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
            }.get (id, None)

print (get_planet_name(8))

#Version of FizzBuzz that you can change the words & the instances. Without any input changes, it will default to normal FizzBuzz
def fizz_buzz_custom(string1 = "Fizz", string2 = "Buzz", num1 = 3, num2 = 5):
    answer = []
    for i in range (1,101):
        if i % num1 == 0 and i % num2 == 0:
            answer.append(string1 + string2)
        elif i % num1 == 0:
            answer.append (string1)
        elif i % num2 == 0:
            answer.append(string2)
        else:
            answer.append()
    return answer

print (fizz_buzz_custom("Hey","There",5,6))


#Finding how many times there is an instance of a number in a list
numbers = [1,1,2,2,3,4,4,5,5]
count = {}
for i in numbers:
    if i not in count:
        count [i] = 1
    else:
        count [i] += 1

for key, value in count.items():
    if value == 1:
        print (key)


#Finding a binary search function that involes halving the list to quickly find the answer
def binary_search(list, item):
    first = 0
    last = len(list) -1
    found = False
    while first <= last and not found:
        mid = (first + last)//2
        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

num = list(range(10,21,2))

target = 19

if binary_search(num, target):
    print ("The number", target, "is in the list")
else:
    print ("The number", target, "is not in the list")





#Cash Register application
purchase_amounts = []
subtotal = 0.0
while True:
    purchased = input ('Enter the price of the item or type "Done" to finish: ')
    if purchased.lower().startswith("d"):
        print (purchase_amounts)
        break
    elif purchased.isdigit():
        purchase_amounts.append(purchased)
    else:
        print ("That is not a valid entry")
while purchase_amounts:
    sub = float(purchase_amounts.pop())
    subtotal = subtotal + sub

print ("You're subtotal is:", str(subtotal))





