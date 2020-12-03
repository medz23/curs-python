def recursive_sum(nr):
    if type(nr) == int:
        if nr <= 0:
            return nr
        else:
            return nr + recursive_sum(nr - 1)