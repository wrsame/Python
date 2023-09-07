board_of_directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

not_employee_in_board = board_of_directors.difference(employees)
employee_in_board = board_of_directors & employees
management_in_board = management & board_of_directors
all_management_employee = management <= employees
all_management_in_board = management <= board_of_directors
employee_management_board = employees & management & board_of_directors
neither_employee_or_management_board = employees - management - board_of_directors

print("Board members who are not employees:", not_employee_in_board)
print("Board members who are also employees:", employee_in_board)
print("Number of management members who are also on the board:", len(management_in_board))
print("Are all management members also employees?", all_management_employee)
print("Are all management members also on the board?", all_management_in_board)
print("Employees who are also in management and on the board:", employee_management_board)
print("Employees who are neither in management nor on the board:", neither_employee_or_management_board)



# 2
data_dict = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
list_of_tuples = [(key, value) for key, value in data_dict.items()]
print("\nList of tuples:", list_of_tuples)


# 3
set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

union_set = set1.union(set2)
symmetric_difference_set = set1.symmetric_difference(set2)
difference_set = set1.difference(set2)
disjoint_set = set1.isdisjoint(set2)

print("Union set:", union_set)
print("Symmetric Difference set:", symmetric_difference_set)
print("Difference set:", difference_set)
print("Are sets disjoint?", disjoint_set)

