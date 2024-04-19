#  python quiz game


questions = ("Which files a green, white, and orange (in that order) tricolor flag? :",
              "Which city is home to the brandenburg gate?:",
             "Where was the first example of paper money used?: ",
             "Which player is Football player from below options ? :" ,
             "Which following sports is known as world sports ?: , ")


options = (("A. Ireland", "B. Ivory Coast", "C. Italy"),
           ("A. Vienna", "B. Zurich", "C. Berlin"),
           ("A. China", "B. Turkey", "C. Greece"),
           ("A. Cristiano Ronaldo", "B. Virat Kholi", "C. Micahel Jordan"),
           ("A. Basketball", "B. Cricket", "C. Football"),)




answers = ("A", "B", "A", "A", "C",)
guesses = []
score = 0
question_num = 0


for question in questions:
    print("-----------------------------------------")
    print(question)
    for option in options [question_num]:
       print(option)      
    
    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]}  is the correct answer ")
    question_num +=1

print("-------------------------")
print("        RESULTS          ")
print("-------------------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")





       
       