def akkerman(m, n):
    if m == 0:
        return n + 1
    elif n == 0 and m > 0:
        return akkerman(m - 1, 1)
    else:
        return akkerman(m - 1, akkerman(m, n - 1))


akkerman(3, 2)
