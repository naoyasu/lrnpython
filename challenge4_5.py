def strin(x):
    """
    Returns float value
    param x : int, float,string value
    """
    try:
        y = float(x)
        return y
    except(ValueError):
        print("error")

f = strin("55.4")
print(f)

