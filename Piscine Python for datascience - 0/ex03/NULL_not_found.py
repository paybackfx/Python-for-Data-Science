def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    elif obj != obj:
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    elif obj is False:
        print(f"Fake: {obj} {type(obj)}")
        return 0
    elif obj == 0:
        print(f"Zero: {obj} {type(obj)}")
        return 0
    elif obj == '':
        print(f"Empty: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1
