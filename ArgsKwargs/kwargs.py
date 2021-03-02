def test(*args, **kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    print(kwargs["fname"])
    print(kwargs["lname"])

    key = "test"
    
    if key in kwargs: 
        print(kwargs["test"])
    else:
        print(f"{key} not in **kwargs")

test(fname = "Wesley", lname = "Vercoutere")