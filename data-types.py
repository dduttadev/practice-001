s1 = "Hello"
s2 = "Welcome to"
num1 = 3
pi = 3.14
result = True

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'Language']

student1 = {'name':"Ram", 'age':19, 'status':"enrolled"}
student2 = {'name':"Shyam", 'age':19, 'status':"TBC"}
student3 = {'name':"Madhu", 'age':20, 'status':"TBC"}

students = student1, student2, student3

print ("Type of variable ''s1'' is:",type(s1))
print ("Type of variable ''num1'' is:",type(num1))
print ("Type of variable ''pi'' is:",type(pi))
print ("Type of variable ''result'' is:",type(result))
print ("Type of variable ''subjects'' is:",type(subjects))
print ("Type of variable ''student1'' is:",type(student1))
print ("Type of variable ''students'' is:",type(students))

for i in students :
   print(i)

#print ("Sudent-1:",student1['name'],"whose age is:",student1['age'])

#print (students)
#print (students[1]['status'])

#print("Student-1:",students[0]['name'])
print()

#'''
print ("Here is a list of new students, yet to enrol:")
for i in students :
    if i['status'] == "TBC" :
        print (i['name'])
#'''

# def get_user_info (str )