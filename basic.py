# fruits=["apple","bannana","cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits)
# fruits.append("orange")
# print(fruits)
# print("Number of fruits:",len(fruits))

# questions=["what is 2+2?","What colour is the sky?"]
# for q in questions:
#     print(q)
#     answer=input(q+" ")
#     print("You said:",answer)

#Dictionaries:
# capital={"France":"Paris","Japan":"Takyo"}
# print(capital["France"])
# print(capital["Japan"])
# q1={"question":"What is 2+2?","answer":4}
# print(q1["question"])
# print("Correct answer is:",q1["answer"])

questions=[
    {"question":"What is 2+2?", "answer":"4"},
    {"question":"Capitalof Japan?","answer":"Takyo"},
    {"question":"How many days in week?","answer":"7"}
]
print("First question:",questions[0]["question"])
print("It's answer:",questions[0]["answer"])
score = 0 
for item in questions:
    user_answer=input(item["question"]+" ")
    if user_answer == item["answer"]:
        print("Correct")
        score+=1
    else:
        print("Wrong.The answer was",item["answer"])  
print("Quiz over! You scored", score,"Out of",len(questions)) 
if score == len(questions):
    print("Perfect score! Amazing!")
elif score >= len(questions)/2:
    print("Good  job!")
else:
    print("keep practising - you will get better!")
user_answer = input(item["question"]+" ")
user_answer = user_answer.lower().strip()
if user_answer == item["answer"].lower():
    print("Correst!")
file = open("scores.txt","a")
file.write("A new score line\n")
file.close()               
player = input("what is ypur name?")
file = open("scores.txt","a")
file.write(player  + " scored " + str(score) + "\n")
file.close()
print("Your scores was saved!")

quize_bank = {
    "Maths": [
        {"question":"2+2?","answer":"4"},
        {"question":"10 -3?", "answer":"7"}
    ],
    "Geography":[
        {"question":"Capital of Japan?","answer":"Takyo"}
    ]
}
print("Categories available:")
for name in quize_bank:
    print("-",name)
