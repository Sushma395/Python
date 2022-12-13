print("Welcome to quiz!!!")
name = input("Player name?")
user_input = str(input(f"Hi {name}, wants to play? Y or N "))
if user_input.upper() == "Y":
    game_on = True
else:
    game_on = False

while game_on:
    quiz_ques = {"Q1: India's first Cricket World Cup win? A: 2011 B: 1983 C: 1987 D:2007 ": "A",
                 "Q2: Is list immutable in python? A: Yes B:No ": "A",
                 "Q3: Factorial of 4? A: 12 B:24 C: 48 D: 4 ": "B",
                 "Q4: Is 1241 a palindrome? A: Yes B: No ": "B",
                 "Q5: No. of states in India? A:29 B:27 C: 28 D:30 ": "C"}
    score = 0
    for ques, ans in quiz_ques.items():
        guess = input(ques)
        if guess == ans:
            score += 1
            print(f"Correct!!!")
        else:
            print(f"Incorrect!!! Correct one is {ans}")
    print(f"Game Over!!!")
    print(f"{name}'s score: {score} percentile: {(score / 5) * 100} ")
    game_on = False


