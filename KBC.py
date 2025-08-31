# Plan is to create a program which is basically a quiz game which continues its progression if the user gives the correct answer and is automatically restarted if the user gives wrong answer
while True:
    user_name=input("Hello player may I know your name: ")
    print("Okay",user_name,"Let's begin with the game!")
    ques_1=input("""First question
             What is the capital city of Australia?
             1)Sydney
             2)New Delhi
             3)New York
             4)Brisbane:  """)
    if ques_1=="1":
        print("Correct Answer",user_name)
    elif ques_1!=1:
        print("Incorrect Answer",user_name)
        quit=input("Do you want to quit the game? Press 'q' to quit the game: ")
        if quit =="q":
            print("Thanks for playing!")
    break