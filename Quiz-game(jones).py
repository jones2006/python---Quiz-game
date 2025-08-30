print("Welcome to a Quiz game")
playgame = input("Are you play a game ?")

if playgame.lower() != "yes":
    print("Okay :( ")
    quit()

print("Okay,start a game :) ")

# one line if else syntax "value_if_true if <condition> else value_if_false"

# question 1
qns_1 = input("CS full form :")
ans_1 = "correct" if qns_1 == "Computer science" else "incorrect"
print(ans_1)


# question 2
qns_2 = input("CPU full form :")
ans_2 = "correct" if qns_2 == "Central processing unit" else "incorrect"
print(ans_2)


# question 3
qns_3 = input("GPU full form :")
ans_3 = "correct" if qns_3 == "Graphics processing unit" else "incorrect"
print(ans_3)

print("Thank you for playing!")
