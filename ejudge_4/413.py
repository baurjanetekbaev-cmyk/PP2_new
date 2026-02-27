import json
import re

data = json.loads(input())
q = int(input())

pattern = re.compile(r'([a-zA-Z_]\w*)|\[(\d+)\]')

for _ in range(q):
    query = input()
    cur = data
    ok = True

    tokens = pattern.findall(query)

    for key, idx in tokens:
        if key:  # доступ к словарю
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                ok = False
                break
        else:  # доступ к списку
            i = int(idx)
            if isinstance(cur, list) and 0 <= i < len(cur):
                cur = cur[i]
            else:
                ok = False
                break

    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")