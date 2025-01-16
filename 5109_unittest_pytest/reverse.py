def reverse(s):
    if type(s) != str:
        raise TypeError(f'Необходим str, а не {type(s)}')
    return s[::-1]