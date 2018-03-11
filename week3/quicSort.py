import math

def quickSort(A,comp_inc):
    piv = 'last'
    A_s = []
    n = len(A)
    if n < 2:
        return (A,comp_inc)
    l = 0
    i_last = len(A)-1
    if piv == 'last':
        swap(A,0,i_last)
    if piv == 'median':
        im=int(math.ceil(len(A)/2.))-1
        if A[0] >= A[im] >= A[i_last] or A[i_last] >= A[im] >= A[0]:
            swap(A,0,im)
        if A[0] >= A[i_last] >= A[im] or A[im] >= A[i_last] >= A[0]:
            swap(A,0,i_last)
    (Ap,p) = partition(A,l)
    m = len(Ap[:p])
    if m > 0:
        comp_inc += m 
    A_left,comp_inc = quickSort(Ap[:p],comp_inc)
    m = len(Ap[p+1:])
    if m > 0:
        comp_inc += m 
    A_right,comp_inc = quickSort(Ap[p+1:],comp_inc)
    A_s = A_left
    A_s.append(A[p])
    A_s.extend(A_right)
    return (A_s,comp_inc)

def partition(A,l):
    n = len(A)
    if n < 2:
        return A
    p = A[l]
    i = l + 1
    for j in range (l+1,n):
        if A[j] < p:
            swap(A,i,j)
            i = i + 1
    swap(A,l,i-1)
    return (A,i-1)

def swap(A,i,j):
    l = A[i]
    A[i] = A[j]
    A[j] = l
