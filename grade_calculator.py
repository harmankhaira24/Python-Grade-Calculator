print(" Grade Calculator ");
name = input("Enter your name: ");
marks_1= float(input("Enter your marks: "));
marks_2= float(input("Enter your marks: "));
marks_3= float(input("Enter your marks: "));
marks_4= float(input("Enter your marks: "));
marks_5= float(input("Enter your marks: "));
marks_6= float(input("Enter your marks: "));
average = (marks_1 + marks_2 + marks_3 + marks_4 + marks_5 + marks_6) / 6;
if average >= 90:
    grade = "A";
elif average >= 80 and average < 90:
    grade = "B";
elif average >= 70 and average < 80:
    grade = "C";
elif average >= 60 and average < 70:
    grade = "D";
elif average >= 50 and average < 60:
    grade = "E";
elif average < 50 and average >= 0:
    grade = "F";
else:
    grade = "Invalid marks entered";
print("Name: ", name);
print("Average Marks: ", average);
print("Grade: ", grade);
       