#All about For Loop
fruits=["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+" pie")
print(fruits)

student_scores=[150,142,185,171,184,149,24,59,68,199,78]
total_exam_score=sum(student_scores)
sum=0
for score in student_scores:
    sum+=score
print(sum)

#maximum number functionality 
maximum_number=0
for i in range(0,len(student_scores)):
    if maximum_number<student_scores[i]:
        maximum_number=student_scores[i]
print(maximum_number)


#Range function

for number in range(1,10,3):
    print(number)

sum=0
for numbers in range(1,101):
    sum+=numbers

print(sum)