# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# My solution

def move_zeros(lst):
    new_lst = []
    zero_count = []
    for number in lst:
        if number == 0:
            zero_count.append(0)
        else: 
            new_lst.append(number)
    for zero in zero_count:
        new_lst.append(zero)
    return new_lst