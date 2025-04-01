
def pad(number: int):
    # trims and pad a number
    n = hex(number)[2:].upper()
    while len(n) < 8:
        n = "0"+n
    return n 
