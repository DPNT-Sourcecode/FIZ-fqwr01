# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    # raise NotImplementedError()
    if isinstance(x,int) and isinstance(y,int):
        if 0 <= x <= 100 and 0 <= y <= 100:
            return x + y
    else:
        return None
