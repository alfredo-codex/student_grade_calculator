# Multiple subjects have been added.
name = input("student name:")
subjects = ["Mathematics","Science","English","ICT","Social Studies"]

total =0
results = []

for subject in subjects:
    score = float(input(f"Enter score for {subject}:"))
    
    while score < 0 or score > 100:
       print("Invalid score,Enter valid score. Enter a score from 0-100")
    if score >=80:
        grade = "A"
        remark = "Excellent"
    elif score >=70:
        grade = "B"
        remark = "Very Good"
    elif score >=60:
        grade = "C"
        remark = "Good"
    elif score >=50:
        remark = "Pass"
        grade = "D"
    else:
        grade = "F"
        remark = "Fail"
    
    total = total + score
    results.append(f"{subject}: {score} \n-Grade {grade} \n-Remark {remark}")

average = total / len(subjects)

print("\n ====== STUDENT RESULT ======")
print("Student:", name)

for line in results:
    print(line)

print("Total Score:", total)
print("Average score:", average)
