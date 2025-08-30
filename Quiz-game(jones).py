print("Welcome to a Quiz game")
playgame = input("Are you play a game ?")
score = 0

if playgame.lower() != "yes":
    print("Okay,Exit a game :( ")
    quit()

print("Okay,start a game :) ")


qns_1 = input("CS full form :")
if qns_1.lower() == "computer science":
    print("correct")
    score += 1
else:
    print("incorrect")


qns_2 = input("CPU full form :")
if qns_2.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")


qns_3 = input("GPU full form :")
if qns_3.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

print("your score is "+str(score) + " and " +
      "Percentage is " + str((score/3) * 100) + "%")
print("Thank you for playing!")
