# check the validity of credit card numbers


def add_num(num):
    if num < 10:
        return num
    else:
        sum = (num % 10) + (num // 10)
        return sum


def validate(cc_num):
    rev_num=cc_num[::-1]
    
    final_num=0

    final_num += sum([add_num(2*int(x)) for x in rev_num[1:][::2]])

    final_num += sum([int(x) for x in rev_num[::2]])

    if( final_num % 10 == 0):
        return True
    return False
