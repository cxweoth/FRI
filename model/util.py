

def xgcd(x, y):
    """
    Input: (x,y) 
    Do: gcd(x,y)=g and find a,b s.t. ax+by=g 
    Output: (a,b,g)
    """
    g_old, g_now = (x, y)
    a_old, a_now = (1, 0)
    b_old, b_now = (0, 1)

    while g_now != 0:
        # when r_now == 0, it means g_old = gcd(x,y), and g_old = a_old*x + b_old*y
        # r_new = r_old - quotient * r_now
        quotient = g_old // g_now
        g_old, g_now = (g_now, g_old - quotient * g_now)
        a_old, a_now = (a_now, a_old - quotient * a_now)
        b_old, b_now = (b_now, b_old - quotient * b_now)

    return g_old, a_old, b_old # a, b, g
