g = 0  
def outer():
    n = 0  
    commands = []

    for _ in range(int(input())):
        scope, val = input().split()
        commands.append((scope, int(val)))

    def inner():
        nonlocal n
        global g
        for scope, val in commands:
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            elif scope == "local":
                x = val  
        return n

    n = inner()
    return n

n_final = outer()
print(f"{g} {n_final}")