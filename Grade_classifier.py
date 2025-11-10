# Grade Classifier
score = int(input("Enter your test score (0–100): "))

if 80 <= score <= 100:
    print("Excellent")
elif 50 <= score < 80:
    print("Good")
elif 0 <= score < 50:
    print("Needs Improvement")
else:
    print("Invalid score entered.")
