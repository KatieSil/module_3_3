def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [[1, 5, 9], False, True]
values_dict = {'a': 15, 'b': 'ветерок', 'c': [2, 4, 6, 8]}
values_list_2 = [2, [1, 3, 5]]

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
