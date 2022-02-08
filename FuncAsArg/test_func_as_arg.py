
def test():
    print(test)

def test2(name):
    print(f"test {name}")



test01 = test
test02 = test2

test01()

test03 = test02

test03('yep')
test03()