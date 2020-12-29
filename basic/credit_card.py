def check_card(id):
    id_str = str(id)
    assert len(id_str) == 15
    other_digit = [int(j) for i,j in enumerate(id_str) if i%2==1]
    other_digit = [i*2 for i in other_digit]
    sum1 = sum([int(j) for i,j in enumerate(id_str) if i%2==0])
    sum2 = 0
    for x in other_digit:
        tick = True
        while tick:
            sum2 += x%10
            x = x//10
            if x==0:
                tick = False
    print('sum1: %s, sum2: %s' % (sum1, sum2))
    if (sum1+sum2) == 60:
        return True
    else:
        return False

if __name__ == "__main__":
    AmEx = 378282246310005
    print(check_card(AmEx))
