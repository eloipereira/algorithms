def rec_mult(int_str0,int_str1):

    n = max(len(int_str0),len(int_str1))
    int_str0 = int_str0.zfill(n)
    int_str1 = int_str1.zfill(n)
    
    if n == 1:
        return str(int(int_str0) * int(int_str1))

    a, b = int_str0[:n/2], int_str0[n/2:]
    c, d = int_str1[:n/2], int_str1[n/2:]

    ac = rec_mult(a,c)
    ad = rec_mult(a,d)
    bc = rec_mult(b,c)
    bd = rec_mult(b,d)

    A = ac.ljust(len(ac)+n,'0')
    
    B = str(int(ad) + int(bc))
    B = B.ljust(len(B) + n/2,'0')
    
    return str(int(A) + int(B) + int(bd))
    
