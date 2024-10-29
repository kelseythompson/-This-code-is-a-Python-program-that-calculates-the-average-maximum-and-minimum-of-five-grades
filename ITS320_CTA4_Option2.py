# Initialize variables to store grades and statistics
grades = []
total = 0

# Loop to read five floating-point grades from user input. +1 for the zero space in the set. total+ adds all the numbers together
for i in range(5):
    grade = float(input("Enter grade {}: ".format(i + 1)))
    grades.append(grade)
    total += grade

# Calculate statistics
average = total / len(grades)
maximum = max(grades)
minimum = min(grades)

# Print the statistics
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)
