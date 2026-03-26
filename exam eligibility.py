total_classes = 50
attended = int(input("Enter number of classes attended: "))
percentage = (attended / total_classes) * 100
print("Attendance Percentage:", percentage, "%")
if percentage >= 70:
    print("You can sit in the exam")
else:
    print("You cannot sit in the exam")