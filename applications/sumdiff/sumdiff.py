"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


def solution(q):
    for i in q:
        for j in q:
            for k in q:
                for m in q:
                    if f(i) + f(j) == f(k) - f(m):
                        print(f'{f(i)} + {f(j)} = {f(k)} - {f(m)}')


print(solution(q))
