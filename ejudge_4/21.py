n = int(input())
for _ in range(n):
    line = input().split()
    module_path, attr = line[0], line[1]
    try:
        mod = __import__(module_path)
        
        for part in module_path.split('.')[1:]:
            mod = getattr(mod, part)
    except ImportError:
        print("MODULE_NOT_FOUND")
        continue
    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
    else:
        if callable(getattr(mod, attr)):
            print("CALLABLE")
        else:
            print("VALUE")