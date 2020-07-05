# soal 1

def find_short (s):
    s1= s.split()
    find_min = min(s1, key=len)
    number = len(find_min)
    return (number)


# soal 2

def persistence (n):
    if len(str(n)) == 1:
        return 0

    counter = 0
    while len(str(n)) > 1:
        base_multi = 1
        for num in str(n):
            base_multi *= int(num)
        n = base_multi
        counter +=1
    
    return counter