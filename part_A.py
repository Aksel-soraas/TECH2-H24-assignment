"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy as np
from math import sqrt

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # Raise value-error if input is an empty list.
    if len(x) == 0:
        raise ValueError('Empty sequences are not supported')
    

    # Define variables used in the function
    sum_lst = 0                             
    sqrt_lst = []                    
    sqrt_sum= 0                    
    N = 0                                   

    for i in x:                         # Summarizing sequence and counting elements
        sum_lst = sum_lst + i
        N += 1

    mean = (1/N) * sum_lst              # Calculate the mean

    for i in x:                         # Square all elements in num_list and sum together
        sqrt_lst.append(i**2)
    for i in sqrt_lst:
        sqrt_sum = sqrt_sum + i

    S = (1/N) * sqrt_sum                # Calculate the mean of the squared list (S)
    var = S - mean**2                   # Computing the variance (var)
    sd = sqrt(var)                      # Computing the standard deviation (sd)

    return sd


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # Raise value-error if input is an empty list.
    if len(x) == 0:
        raise ValueError('Empty sequences are not supported')
    

    # Define variables used in the function
    sum_lst = sum(x)
    sqrt_lst = []
    N = len(x)

    for i in x:                         # Square all elements in num_list and sum together
        sqrt_lst.append(i**2)
    sqrt_sum = sum(sqrt_lst)

    mean = (1/N) * sum_lst              # Calculate the mean
    S = (1/N) * sqrt_sum                # Calculate the mean of the squared list (S)
    var = S - mean**2                   # Computing the variance (var)
    sd = sqrt(var)                      # Computing the standard deviation (sd)

    return sd

def main():
    x = [1, 2, 3, 4, 5]
    
    looped = std_loops(x)

    builtin = std_builtin(x)

    std_function = np.std(x)
    
    print(f'\nDeviation by loops is: {looped}.\nDeviation by built in functions is: {builtin}.\nDeviation using numpy is: {std_function}.\n')

if __name__ == "__main__":
    main()
