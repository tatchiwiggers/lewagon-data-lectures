beatles = ['paul', "john", "ringo", "george", 'paul']
beatles.remove('paul')
del beatles[0]
# print(beatles)

staff = ["Ben", "Alex", "Lucien", "Arthur", "Anne", "Blair", "Sam"]
for staff_member in staff:
    print(staff_member)

for index, staff_member in enumerate(staff):
    print(f"{index + 1} - {staff_member}")

# print([member for member in enumerate(staff)])
# [(0, 'Ben'), (1, 'Alex'), (2, 'Lucien'), (3, 'Arthur'), (4, 'Anne'), (5, 'Blair'), (6, 'Sam')]