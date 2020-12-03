def recursive_even_sum(nr):
    if type(nr) == int:
        if nr <= 0:
            return nr
        else:
            if nr % 2 == 0:
                return nr + recursive_even_sum(nr - 1)
        return recursive_even_sum(nr - 1)
