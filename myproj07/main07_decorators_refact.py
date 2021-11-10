import time


# cached = {}


# def mysum2(x, y):
#     key = (x, y)
#     if key not in cached:
#         time.sleep(1)  # 1초간 대기
#         cached[key] = x + y + 10
#     return cached[key]


def memoize(fn):
    cached = {}  # 호출때마다 새로운 cached가 만들어진다 **중요포인트!

    def wrap(x, y):
        key = (x, y)
        if key not in cached:
            cached[key] = fn(x, y)
        return cached[key]

    return wrap


@memoize  # 장식자 = decorators
def mysum2(x, y):
    time.sleep(1)
    return x + y + 10


# mysum2 = memoize(mysum2)
# mysum2(1, 2)


@memoize
def mymultiply2(x, y):
    time.sleep(1)
    return x * y + 10


# mymultiply2 = memoize(mymultiply2)
# mymultiply2(1, 2)


print(mysum2(1, 2))
print(mysum2(1, 3))
print(mysum2(1, 3))
print(mysum2(1, 2))
print(mysum2(1, 2))

print(mymultiply2(1, 2))
print(mymultiply2(1, 2))
print(mymultiply2(1, 3))
print(mymultiply2(1, 3))
