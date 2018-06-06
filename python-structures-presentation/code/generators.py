# generator function
def g_range(n):
    for i in range(n):
        yield i

r = g_range(2)

print(next(r))  # 0
print(next(r))  # 1
print(next(r))  # 2
print(next(r))  # raises StopIteration!