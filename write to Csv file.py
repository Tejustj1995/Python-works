import csv
#import pandas
n = int(input("Please enter number of students:"))
#$m = int(input("Please enter number of subjects:"))

student_data = []
for i in range(0, n):
    stud_name = input('Enter the name of student: ')
    print(stud_name)
    mark1 = int(input('Enter marks 1: '))
    print(mark1)
    mark2 = int(input('Enter marks 2: '))
    print(mark2)
    mark3 = int(input('Enter marks 3: '))
    print(mark3)
    total = mark1 + mark2 + mark3
    print("Total is: ", total)

    average = total // 3
    print("{0}'s Average is : {1}".format(stud_name, average))

    student_data.append({stud_name: {'sub':{'math': mark1, 'physics': mark2, 'chemistry': mark3}, 'Total': total, 'Average': average}})
    print(student_data)
    for student in student_data:
        print('\n')
        for key, value in student.items():
            print('{0}: {1}'.format(key, value))



with open("tejus.csv", 'w') as fp:
    output = csv.writer(fp, delimiter='\t')
    output.writerow(["Name\t", "maths\t", "chemistry\t","physics\t", "total\t", "average\t"])
    output.writerow(student_data)
fp.close()

