# Quiz-spill

questions_answers = [
    ("Spørsmål 1", "1"),
    ("Spørsmål 2", "2"),
    ("Spørsmål 3", "3"),
    ("Spørsmål 4", "4"),
    ("Spørsmål 5", "5"),
    ("Spørsmål 6", "6"),
    ("Spørsmål 7", "7"),
]

score_dårlig = 1/3
score_middels = 2/3

points = 0

for qa in questions_answers:

    print(qa[0])
    user_answer = input("Ditt svar: ")

    if (user_answer.lower() == qa[1]):
        print("Riktig!")
        points += 1
    else:
        print("Feil!")

score = points / len(questions_answers)

if (score <= score_dårlig):
    print("Du fikk karakteren 'DÅRLIG'")
elif (score <= score_middels):
    print("Du fikk karakteren 'MIDDELS'")
else:
    print("Du fikk karakteren 'GOD'")



