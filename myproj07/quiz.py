# fmt: off

def mysum2(x, y):
    return x + y + 10


def mysum3(x, y, z):
    return x + y + z + 10

# 가변인자
def mysum(x, y, *args): # *붙이면 0개부터 무제한으로 호출받음
    # args is tuple
    print("args :", args)
    return x + y + sum(args) + 10

# print(mysum())
# print(mysum(1))
print(mysum(1, 2))
print(mysum(1, 2, 3))
