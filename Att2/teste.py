def MinimumX(a, b, c, k):
    x = 10**9
    if (k <= c):
        return 0
    h = k - c
    l = 0

    while (l <= h):
        m = (l + h) // 2
        if ((a * m * m) + (b * m) > (k - c)):
            x = min(x, m)
            h = m - 1

        elif ((a * m * m) + (b * m) < (k - c)):
            l = m + 1
        else:
            return m
    return x


# Driver code
a, b, c, k = 3, 2, 4, 1
print(MinimumX(a, b, c, k))
