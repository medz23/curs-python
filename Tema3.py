# functie cu nr nedefinit de parametrii care calculeaza suma parametrilor
# your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3)
# your_function() va returna 0
# your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4)


def infinite_parameters(*args, **kwargs):
    result  = 0
    for argument in args:
        if type(argument) == int or type(argument) == float:
            result += argument
        else:
            pass
    return result


print(infinite_parameters(1, 5, -3, 'abc', [12, 56, 'cad']))
print(infinite_parameters())
print(infinite_parameters(2, 4, 'abc', param_1=2))


# functie care citeste de la tastatura si returneaza valoarea daca val > 0, altfel returneaza 0.
def user_input():
    user = input("Enter an integer: ")
    try:
        int(user)
        print("Your number is: ")
    except Exception as e:
        user = 0
        print("It's not an integer")
    finally:
        return user


print(user_input())


# Importuri pentru package-ul tema_curs_3
from tema_curs_3.recursive_sum import recursive_sum as rs
from tema_curs_3.recursive_even_sum import recursive_even_sum as res
from tema_curs_3.recursive_odd_sum import recursive_odd_sum as ros

nr = 5

# functie recursiva care primeste ca parametru un nr intreg returnand:
# suma tuturor numerelor de la [0, n]
print(rs(nr))

# suma numerelor pare de la [0, n]
print(res(nr))

# suma numerelor impare de la [0, n]
print(ros(nr))

