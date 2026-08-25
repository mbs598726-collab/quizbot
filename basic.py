fruits=["apple","bannana","cherry"]
print(fruits[0])
print(fruits[1])
print(fruits)
fruits.append("orange")
print(fruits)
print("Number of fruits:",len(fruits))

questions=["what is 2+2?","What colour is the sky?"]
for q in questions:
    print(q)
    answer=input(q+" ")
    print("You said:",answer)

Dictionaries:
capital={"France":"Paris","Japan":"Takyo"}
print(capital["France"])
print(capital["Japan"])
q1={"question":"What is 2+2?","answer":4}
print(q1["question"])
print("Correct answer is:",q1["answer"])

questions=[
    {"question":"What is 2+2?", "answer":"4"},
    {"question":"Capitalof Japan?","answer":"Takyo"},
    {"question":"How many days in week?","answer":"7"}
]
print("First question:",questions[0]["question"])
print("It's answer:",questions[0]["answer"])

score =0
for item in questions:
    print(item["question"])
    answer=input("Your answer: ")
    if answer==item["answer"]:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is:",item["answer"])
print("Quiz over! You scored", score,"out of",len(questions))
if score ==  len(questions):
    print("Congratulations! You got all answers correct!")
elif score >= len(questions)/2:
    print("Good job! You got more than half correct.")
else:
    print("Better luck next time! You got less than half correct.")
user_answer = input(item["question"] + " ")
user_answer = user_answer.strip().lower()
if user_answer == item["answer"].lower():
    print("Correct!")
    score += 1
file = open("scores.json", "w")
file.write("Samscored 3\n") 
file.close()
print("Saved!")
player = input("Enter your name: ")
file = open("scores.txt","a")       
file.write(f"{player}: {score}/{len(questions)}\n")
file.close()
print("Score saved!")
quiz_bank = {
"Maths": [
{"question": "2 + 2?", "answer": "4"},
{"question": "10 - 3?", "answer": "7"}
],
"Geography": [
{"question": "Capital of Japan?", "answer": "Tokyo"}
]
}
print("Categories available:")
for name in quiz_bank:
print("-", name)
