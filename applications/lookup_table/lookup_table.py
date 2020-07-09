# Your code here
import math #import math since it was used but not imported
import random #random import since it was used and not imported 


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

cache = {

}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # cache = {}

    def slowfun_inner(x, y):
        n = (x, y)
        if n not in cache:
            v = math.pow(x, y)
            v = math.factorial(v)
            v //= (x + y)
            v %= 982451653
            cache[n] = v
        return cache[n]
    return slowfun_inner(x, y)

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
