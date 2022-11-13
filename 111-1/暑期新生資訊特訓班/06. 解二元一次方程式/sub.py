a, b, c, e, f, g = list(map(int, input().split()))

times = (e / a)

a2 = a * times
b2 = b * times
c2 = c * times

y = (((c2 - g) * -1) / (b2 - f))

x = ((c2 + (b2 * y))*-1 / a2)

print(f'求出的解為 x = {x}, y = {y}')