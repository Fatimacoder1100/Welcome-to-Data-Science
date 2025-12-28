import numpy as np
#define data type (structured array)
data_type = [
    ('name','S15'), #string of max 15 chracters
    ('class',int),
    ('height',float)
]

students_data = [
    ('Fatima',7,30.7),
    ('Hajira',5,2.8),
    ('Bareeera',3,8.9),
    ('Hussain',1,7.3)
]

#create structured NumPy array
students = np.array(students_data,dtype=data_type)

print("Original Array : ")
print(students)

print("\nSorted by height in ascending order : ")
sorted_students = np.sort(students,order='height')
print(sorted_students)