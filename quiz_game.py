print("welcome to my computer quiz game :) ")

playing =input("Do you want to play my quiz game ? ")

if playing.lower() != "yes":
    quit()

print("let's start playing :) ")
score =0

answer = input("What does CPU stand for ? ")
if answer.lower()=="central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for ? ")
if answer.lower()=="graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for ? ")
if answer.lower()=="random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for ? ")
if answer.lower()=="power supply":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("YOU GOT " + str(score) + " QUESTIONS CORRECT!")
print("YOU GOT " + str((score/4) *100 ) + "%")