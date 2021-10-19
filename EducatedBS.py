
def educated_guess(lst, val) {
    index_deviation = len(lst) // 3
    vals_by_deviation = [lst[0], lst[index_deviation], lst[len(lst) - 1 - index_deviation], lst[len(lst) - 1]]
    deviations = [vals_by_deviation[1] - vals_by_deviation[0],
                  vals_by_deviation[2] - vals_by_deviation[1],
                  vals_by_deviation[3] - vals_by_deviation[2]]

    if val < lst[0]:
        return -1
    elif val > lst[len(lst) -1 ]:
        return -1
    else:
        print("TODO: Find likelinesses of being between the deviations")
        return 0
        

def ebs(lst, val) {
        '''
    Description
    -----------
    Faster search with binary by taking an educated guess

    Parameter(s)
    ------------
    lst : list
        the sorted list
    val : comparable
        the value to look for
    '''
    length = len(lst)


    if length == 0:
        return -1
    elif length == 1:
        return 0 if lst[0] == val else -1
    elif length == 2:
        return 0 if lst[0] == val or 1 if lst[1] == val else -1
    elif length == 3:
        return 0 if lst[0] == val or 1 if lst[1] == val or 2 if lst[2] == val else -1
    else:
        return educated_guess(lst, val)

