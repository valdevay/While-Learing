s = [1]config.cfg

def select_second(L):
    if len(L) >= 2:
        return L[1]
    else:
        return None

print(select_second(s))
