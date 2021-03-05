

def priority(n):
    return (n&1==0) + (n&1==0 and (n>>1)&1==0) + ((n==2)*3)


def solution(n):
    pellets = int(n)
    operations = 0

    while pellets > 1:
        chosen = pellets+1
        priority_c = priority(chosen)
        priority_n = priority(pellets-1)
        if priority_n >= priority_c:
            chosen = pellets-1
            priority_c = priority_n
        if pellets&1==0:
            priority_n = priority(pellets>>1)
            if priority_n >= priority_c:
                chosen = pellets>>1
        pellets = chosen
        operations += 1
    return operations