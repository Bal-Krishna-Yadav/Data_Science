print("--BCA With Specilization Data Science--")
# Get user input
score=int(input("Enter your score(1-100) :"))
if score >= 90 and score <= 100:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50 :
    print("Grade: D")
elif score >= 60 :
    print("Grade: E")
elif score >= 0:
    print("Grade: F")    
else:
    print("Invalid score ! Please enter value between 0 and 100")                        