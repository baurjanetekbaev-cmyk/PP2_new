import json

def diff(a, b, path=""):
    res = []

    # все ключи из обоих JSON
    keys = set(a.keys()) | set(b.keys())

    for k in keys:
        new_path = f"{path}.{k}" if path else k

        if k not in a:
            res.append(f"{new_path} : <missing> -> {json.dumps(b[k], separators=(',', ':'))}")

        elif k not in b:
            res.append(f"{new_path} : {json.dumps(a[k], separators=(',', ':'))} -> <missing>")

        else:
            if isinstance(a[k], dict) and isinstance(b[k], dict):
                res.extend(diff(a[k], b[k], new_path))
            elif a[k] != b[k]:
                res.append(
                    f"{new_path} : {json.dumps(a[k], separators=(',', ':'))} -> {json.dumps(b[k], separators=(',', ':'))}"
                )

    return res
a = json.loads(input())
b = json.loads(input())

ans = diff(a, b)

if not ans:
    print("No differences")
else:
    for line in sorted(ans):
        print(line)