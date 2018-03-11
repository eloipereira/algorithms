
def mergeSort(l):
    if len(l) <=1:
        return (l,0)
    left = l[:len(l)//2]
    right = l[len(l)//2:]
    (left_sorted,il) = mergeSort(left)
    (right_sorted,ir) = mergeSort(right)
    (merged,i) = merge_loop(left_sorted,right_sorted)
    return (merged,il+ir+i)


def merge_loop(a,b):
    c = []
    i = 0
    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
            i = i + len(a) 
    if len(a) == 0:
        c += b
    else:
        c += a
    return (c,i)
        

def merge_rec(l0,l1,inv_acc):
    l = []
    if len(l0) == 0:
        return (l1,inv_acc)
    elif len(l1) == 0:
        return (l0,inv_acc)
    elif l0[0] <= l1[0]:
        l.append(l0[0])
        (lm,i) = merge(l0[1:],l1,inv_acc)
        l.extend(lm)
        return (l,i)
    else:
        l.append(l1[0])
        (lm,i) = merge(l0,l1[1:],inv_acc)
        l.extend(lm)
        return (l,i+len(l0))
