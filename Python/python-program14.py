# Write a program to input the marks of your PCM steam, using for loop, print its total and its average
marks_total = 0
for i in range(1,7):
    mark=int(input("Enter Marks:"))
    marks_total +=mark
print("Total Marks=",marks_total)
print("Average Marks=",marks_total/6)
