def recursive_odd_sum(nr):
    if type(nr) == int:
        if nr <= 1:
            return nr
        else:
            if nr % 2 == 1:
                return nr + recursive_odd_sum(nr - 1)
        return recursive_odd_sum(nr - 1)