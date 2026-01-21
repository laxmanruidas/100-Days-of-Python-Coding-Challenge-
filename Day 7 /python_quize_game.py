# Day 7 - Simple Quiz Game

score = 0
quiz = [
    {
        "question": "What is Python?",
        "options": {
            "a": "Snake",
            "b": "Programming Language",
            "c": "Game",
            "d": "Car"
        },
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {
            "a": "func",
            "b": "define",
            "c": "def",
            "d": "function"
        },
        "answer": "c"
    },
    {
        "question": "Which data type is used to store multiple values?",
        "options": {
            "a": "int",
            "b": "float",
            "c": "string",
            "d": "list"
        },
        "answer": "d"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "a": "//",
            "b": "#",
            "c": "/*",
            "d": "--"
        },
        "answer": "b"
    },
    {
        "question": "Which function is used to take input from user?",
        "options": {
            "a": "print()",
            "b": "input()",
            "c": "scan()",
            "d": "read()"
        },
        "answer": "b"
    }
]
#USER GREEATE MASAGE
print("----------------------------")
print("Welcome to the quize game")
print("----------------------------")

for question in quiz:
    print("\n" + question["question"])
    for key ,value in question["options"].items():
        print(f"{key}. {value}")

    user_ans = input("Enter your answer - (a/b/c/d): ").lower().strip()

    if user_ans == question["answer"]:
        print("Correct ")
        score += 1
    else:
        print("Wrong")

print(f"Your Score: {score}/{len(quiz)}")
print ("Program End!")
