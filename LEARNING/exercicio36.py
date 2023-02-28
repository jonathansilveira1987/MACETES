def foo(k):
    k[0] = 1
q = [0]
foo(q)
print(q)