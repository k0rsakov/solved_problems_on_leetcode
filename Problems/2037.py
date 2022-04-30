seats = [4,1,5,9]
students = [1,3,2,6]

seats.sort()
students.sort()

counter = 0
for i in range(len(seats)):
    counter+=abs(seats[i] - students[i])

print(counter)