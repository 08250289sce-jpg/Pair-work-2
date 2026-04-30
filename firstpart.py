# Step 1: predefined student id 
id1 = 208250275  # id of lhendup 
id2 = 208250289  # std id of Wangchen

# displaying two student id
print("The student id of Lhendup:", id1)
print("The student id of Wangchen:", id2)

# Extract last two digits using modulus (%) operator
last1 = id1 % 100   # %100 gives last 2 digit and%10 gives single digit
last2 = id2 % 100   

# displaying the last two id
print("Last two digits of Student Lhebdup Dorji:", last1)
print("Last two digits of Student Wangchen Lhamo:", last2)

# Generate unique value
unique_value = (last1 + last2) % 10   # Add and take mod 10

# Display the unique value
print("Unique value:", unique_value)

student = {} #creating dict to store std name

while True: # uses while loop to conitinuously ask input
    name = input("Enter student name and type exit to stop after entering the name: ")

    if name == "exit": # stops the loop if the user type exit
        break

    if name == "": # if user keep blank printing warning
        print("Warning: Name can't be blank")
    else:
        student[name] = 0   # initial score

#Displaying the name 
print("\nStudents List:")
for name in student:
    print(name)
# starting quiz
print("\nLets start quiz") #Everything after \n goes to the next line

# now quize section for each student
for name in student: # using for loop and refering to student in dict
    print("\nStudent:", name)
    score = 0   # reset score for each student

# Giving the instruction

print("For the quizes below refer the given unique values ")

#question 1 with options
print("\n Q1)What is the sum of unique_value + 4") # question that uses unique values
print("A:", unique_value + 1) # options that uses unoque values
print("B:", unique_value + 2)
print("C:", unique_value + 3)
print("D:", unique_value + 4) # correct option

ans1 = input("write your correct option (A/B/C/D): ")
if ans1 == "D":
    score = score + 1
    print("Correct Answer")
else:
    print("Incorrect answer!! and correct option is A")


#question 2 
print("\n Q2)What is the product of unique_value  * 5")
print("A:", unique_value * 3)
print("B:", unique_value * 5)# this is the correct ans
print("C:", unique_value * 4)
print("D:", unique_value * 1)

ans2 = input("write your correct option (A/B/C/D): ")
if ans2 == "B":
    score = score + 1
    print("Correct Answer")
else:
    print("Incorrect answer!! and correct option is B ")

#question 3
print("\nQ3) What is the quotient of unique_value / 2?")
print("A:", f"{unique_value / 1:.2f}")
print("B:", f"{unique_value / 3:.2f}") # using string formating 
print("C:", f"{unique_value / 2:.2f}")   # Correct option
print("D:", f"{unique_value / 4:.2f}")

ans3 = input("write your correct option (A/B/C/D): ")
if ans3 == "C":
    score = score + 1
    print("Correct Answer")
else:
    print("Incorrect answer!! and correct option is B ")

student[name] = score

# now create the permormance and checking for eligibility of certificate
print("\nResults of Quiz")

for name in student: # using for loops through each student name in the dictionary
    score = student[name] # Get the score of the current student from the dictionary
    print("Student Name:",name)
    print("Score:", score)

# now check performance and certificate
    if score == 3:
        print("Excellent and Eligible for Certificate")
    elif score == 2:
        print("Good and Eligible for certificate")
    elif score == 1:
        print("Average and not elifible for certificate") 
    else:
        print("POOR PERFORMANCE !! Need Improvement ")

# star pattern according to their grade
print("Pattern:")

if score == 0:
        print("")  
        # No pattern for 0 score

else:
    for i in range(1, score + 1):
        print("*" * i)
        
















    
    