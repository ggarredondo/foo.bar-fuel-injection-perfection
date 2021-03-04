

def check_child(selected, n):
    if selected:
        return (n&1==0 and (n>>1)&1==0) or n==2
    else:
        return n&1==0


def solution(n):
    pellets = int(n)
    counter = int(pellets>1)

    while pellets > 2:
        selected = False
        aux = pellets
        if check_child(selected, pellets+1):
            aux = pellets+1
            selected = True
        if check_child(selected, pellets-1):
            aux = pellets-1
            selected = True
        if pellets&1==0:
            if check_child(selected, pellets>>1):
                aux = pellets>>1
        pellets = aux
        counter += 1
    return counter