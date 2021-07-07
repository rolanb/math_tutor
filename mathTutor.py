"""
Filename: mathTutor.py
Name of programmer: Rolan Belgrave
Program description: This program will help the user practice simple
mathematical problems (addition, substraction, multiplication) as many
times as they choose.
Algorithm:
- Import randint function
- Define choice prompt fuction
- Define choice verification function
- Define main menu display and verification as function
- Define practise function:
    - set number limits depending on difficulty
    - if addition:
        - interate through amount of excerices and display them:
            - prompt answer
            - check answer:
                - if correct: print recognition and add to total of correct answers
                - else: print is a wrong answer and what correct answer would be
    - if substraction:
        - interate through amount of excerices and display them:
            - prompt answer
            - check answer:
                - if correct: print recognition and add to total of correct answers
                - else: print is a wrong answer and what correct answer would be
    - if multiplication:
        - interate through amount of excerices and display them:
            - prompt answer
            - check answer:
                - if correct: print recognition and add to total of correct answers
                - else: print is a wrong answer and what correct answer would be
    - display how many correct answers and grade
- Display main menu
- If choice is 1:  display instruction
- if your choice is 2:
    - Prompt what operation user wants to practice
    - Prompt what level of dificulty
    - prompt how many exercises to take
    - Run practice of exercises with parameters prompted 
- if your choice is 3: Exit program


"""
#Import randint function
from random import randint

#Define choice prompt fuction
def prompt_choice():
    choice_selected = int(input("\nEnter your choice here: "))
    return choice_selected

#Define choice verification function
def verify_choice(choice, num):
    good_choices = list(range(1,num + 1))
    if choice in good_choices:
        return True
    else:
        return False

#Define main menu display and verification as function
def main_menu():
    choice = 0
    while choice < 1 or choice > 3:
        print("Choose from the following options:\n")
        print("1) See instructions")
        print("2) Practice math")
        print("3) Exit program\n")
        choice = prompt_choice()
        if choice < 1 or choice > 3:
            print("\nSorry, choice must be either 1, 2 or 3\n")
    return choice

#Define practise function
def practice(operation, level, amount):
    nums = []
    correct_answers = 0

    #set number limits depending on difficulty
    if level == 1:
        nums = [1, 9]
    else:
        nums = [10, 99]
    if operation == 1: #Addition
        print("Let'd do some addition!")

        #interate through amount of excerices and display them
        for problem in range(1, amount + 1):
            print("\nProblem ", problem, ":")
            num1 = randint(nums[0], nums[1])
            num2 = randint(nums[0], nums[1])

            #prompt answer and check
            answer = int(input(str(num1) + " + " + str(num2) + " = "))
            right_answer = num1 + num2

            #if correct: print recognition and add to total of correct answers
            if answer == right_answer:
                print("Good job! Correct!")
                correct_answers += 1
            else:
                print("Oops!, correct answer was ", right_answer)

    elif operation == 2: #Substraction
        print("Let'd do some substraction!")
        #interate through amount of excerices and display them
        for problem in range(1, amount + 1):
            print("\nProblem ", problem, ":")
            num1 = randint(nums[0], nums[1])
            num2 = randint(nums[0], nums[1])

            #prompt answer and check
            answer = int(input(str(num1) + " - " + str(num2) + " = "))
            right_answer = num1 - num2

            #if correct: print recognition and add to total of correct answers
            if answer == right_answer:
                print("Good job! Correct!")
                correct_answers += 1
            else:
                print("Oops!, correct answer was ", right_answer)
    else: #Multiplication
        print("Let'd do some multiplication!")
        #interate through amount of excerices and display them
        for problem in range(1, amount + 1):
            print("\nProblem ", problem, ":")
            num1 = randint(nums[0], nums[1])
            num2 = randint(nums[0], nums[1])

            #prompt answer and check
            answer = int(input(str(num1) + " * " + str(num2) + " = "))
            right_answer = num1 * num2

            #if correct: print recognition and add to total of correct answers
            if answer == right_answer:
                print("Good job! Correct!")
                correct_answers += 1
            else:
                print("Oops!, correct answer was ", right_answer)
    correct_porcentage = (correct_answers / amount) * 100

    #display how many correct answers and grade
    print("\nYou answered ", correct_answers, " out of ", amount, " correctly. Your score is = ", correct_porcentage, "%")
    

def main():
    print("\nWelcome to the Math Tutor program, by Rolan\n")
    option = 2

    #Display main menu
    while option != 3:
        option = main_menu()

        #If choice is 1:  display instruction
        if option == 1:
            print("\nThis program will help you practice your math skills." )
            print("First, you will choose Addition, Subtraction or Multiplication.  ")
            print("Next, you will choose a level.  Level 1 will give you problems with single digits and Level 2 will use two-digit numbers. ")
            print("Then, you will choose how many math problems you would like to complete." ) 
            print("After you have completed all your problems, you will be given a score.")
            print("\nYou can play as many times as you want.  Have fun!!\n")
        elif option == 2:
            print("\nLet's do some math!")
            math_choice = 0
            #Prompt what operation user wants to practice
            while verify_choice(math_choice, 3) == False:    
                print("Choose which operation you want to practice:\n")
                print("1) Addition")
                print("2) Substraction")
                print("3) Multiplication\n")
                math_choice = prompt_choice()
                if verify_choice(math_choice, 3) == False:
                    print("\nSorry, your choice is not valid")
            print("\nGreat, what level of difficulty want to try?\n")
            level_choice = 0
            #Prompt what level of dificulty
            while verify_choice(level_choice, 2) == False:
                print("Choose which level of difficulty you want")
                print("1) Level 1: Easy")
                print("2) Level 2: Medium")
                level_choice = prompt_choice()
                if verify_choice(math_choice, 3) == False:
                    print("\nSorry, your choice is not valid")
            print("\nExcellent, and how many excerice do you want to do?")
            amt_exercises = 0

            #prompt how many exercises to take
            while amt_exercises < 1:
                amt_exercises = prompt_choice()
                if amt_exercises < 1:
                    print("Invalid, your choice must be a positive integer")

            #Run practice of exercises with parameters prompted        
            practice(math_choice, level_choice, amt_exercises)
            
                
    #if your choice is 3: Exit program     
    print("\nYou chose 3, exiting program, Good bye!\n")
    

main()
