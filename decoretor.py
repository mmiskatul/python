def add_springkel(func):
    def wrapper():
        print("**You add  Sprinkles 🎊**")
        func()
    return wrapper()
def add_fudge(func):
    def wrapper():
        print("You add fudge 🍫")
        func()
    return wrapper()
@add_springkel
def get_ice_cream():
    print("Here is your ice cream 🍨")
get_ice_cream()