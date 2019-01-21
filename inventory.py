stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayinventory():
    for k, v in stuff.items():
        print(stuff[k], " : ", k)
        print()


print(displayinventory())
