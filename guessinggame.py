'''
#curl ONLY works in Jupyter notebook. linux coding.
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements.txt
elements_file = open('elements.txt', 'r')
elements_list = []
for num in range(1, 20):
    element = elements_file.readline().strip().title()
    elements_list.append(element)
#end Jupyter specific coding here
'''
elements_list = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium',
                 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium']



def elements_guessing():
    print("List any 5 elements in the first 20 elements on the Periodic Table")
    guessed = []
    count = 0
    while count < 5:
        guess = input("Enter an element: ").title()
        if guess in guessed:
            print(guess, "already been guessed. Try again")
        else:
            guessed.append(guess)
            count += 1
    print("Guesses: \n", guessed, "\n")
    return guessed

answers = elements_guessing()

right_answers = []
wrong_answers = []

for item in answers:
    if item in elements_list:
        right_answers.append(item)
    else:
        wrong_answers.append(item)


score = float(len(right_answers) / len(answers)) * 100
print ("You had", score,  "% correct")
print ("Right answers:", ", ".join(right_answers))
print ("Wrong answers:", ", ".join(wrong_answers))

