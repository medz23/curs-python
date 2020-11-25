# Lista cu valori
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]


# Afisare in ordine ascendenta
my_ascending_list = my_list.copy()
my_ascending_list.sort()
print(my_ascending_list)

# Afisare in ordine descendenta
my_descending_list = my_ascending_list.copy()
my_descending_list.reverse()
print(my_descending_list)

# Afisare numere pare din lista folosind slice
my_even_list = my_ascending_list[1::2]
print(my_even_list)

# Afisare numere impare din lista folosind slice
my_odd_list = my_ascending_list[0::2]
print(my_odd_list)

# Afisarea elementelor multipli ai lui 3
my_multiple_of_3_list = my_ascending_list[2::3]
print(my_multiple_of_3_list)