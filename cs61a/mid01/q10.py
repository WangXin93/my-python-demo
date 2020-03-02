def sum_range(lower, upper):
    """
    >>> sum_range(45, 60) # Printer 1 prints within this range
    True
    >>> sum_range(40, 55) # Printer 1 can print a number 55-60
    False
    >>> sum_range(170, 201) # Printer 1 + 2 will print between 180 and 200 copies total
    True
    """
    def copies(pmin, pmax):
        if pmin >= lower and pmax <= upper:
            return True
        elif pmin >= lower and pmax > upper:
            return False
        return copies(pmin+50, pmax+60) or copies(pmin+130, pmax+140)
    return copies(0, 0)
