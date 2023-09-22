lookup = {1: "one", 2: "two"}

def find(n: bool):
    print("Looking up " + str(n))
    global lookup
    return lookup[n]

print(find(2))
