questions=("What is the capital of France?",
           "Which planet is known as the Red Planet?",
           "What is the chemical symbol for water?",
           "Which mountain is the tallest in the world?",
           "Who is the co-founder of Microsoft Corporation?")

options=(("Paris", "Berlin", "London", "Rome"),
         ("Earth", "Mars", "Jupiter", "Venus"),
         ('a. H2O','b. CO2','c. O2','d. N2'),
         ('a. Mount Everest','b. K2','c. Kangchenjunga','d. Lhotse'),
         ('a. Steve Jobs','b. Mark Zuckerberg','c. Bill Gates','d. Jeff Bezos'))

answers=("A","B","A","A","C")
guesses=[]
score=0
qeustion_num=0

for q in questions:
    print("-----------------------------")
    print("                      ")
    print(q)
    for o in options[qeustion_num]:
        print(o)

    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[qeustion_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[qeustion_num]} is the correct answer")
    
    qeustion_num=qeustion_num+1
    
score=int(score/len(questions)*100)
print("Your score is:",score,"%")
