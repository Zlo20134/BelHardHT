def bread(func):
    def wrapper():
        print("</------------\\>")
        func()
        print("<\\____________/>")
    return wrapper


def tomato(func):
    def wrapper():
        print("*** помидоры ****")
        func()
    return wrapper


def salad(func):
    def wrapper():
        print("~~~~ салат ~~~~~")
        func()
    return wrapper


def cheese(func):
    def wrapper():
        print("^^^^^ сыр ^^^^^^")
        func()
    return wrapper


def onion(func):
    def wrapper():
        print("----- лук ------")
        func()
    return wrapper


@bread
@onion
@tomato
def beef():
    print("### говядина ###")


@bread
@cheese
@salad
def chicken():
    print("|||| курица ||||")

print("гамбургер:")
beef()

print("\nчикенбургер:")
chicken()
