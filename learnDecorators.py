def check(func):
    def inside(a, b):
        if(b == 0):
            print("Can't divide by 0")
            return
        func(a, b)
    return inside # execute the inside function.

@check # "@check" == "div = check(div)"
def div(a, b):
    return a / b



print(div(10, 0))