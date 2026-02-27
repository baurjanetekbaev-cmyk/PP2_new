from datetime import datetime, timedelta

def parse(line):
    date_part, utc_part = line.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    sign = 1 if "+" in utc_part else -1
    h, m = map(int, utc_part[4:].split(":"))
    offset = timedelta(hours=h, minutes=m)
    
    return dt - offset if sign == 1 else dt + offset


a = parse(input().strip())
b = parse(input().strip())

diff_seconds = abs((a - b).total_seconds())
print(int(diff_seconds // 86400))