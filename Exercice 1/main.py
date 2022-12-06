
d = 1
h = 4
m = 66
s = 100

if s >= 60:
    s = s - 60
    m = m + 1

if m >= 60:
    m = m - 60
    h = h + 1

if h >= 24:
    h = h - 24

if h >= 7:
    d = d + 1

print(d, h, m, s)

