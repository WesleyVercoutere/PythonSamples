def test(args):
    print(type(args))

    if (type(args) == tuple) or (type(args) == list):
        for arg in args:
            print(arg)
    else:
        print(args)

test(1)
test(2)
# test(3, 4, 5)

myList = [10,11,12,13,14,15]
test(myList)

myTuple = (20,21,22,23,24,25)
test(myTuple)
