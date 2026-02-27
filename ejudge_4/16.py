from datetime import datetime, timedelta
import re

def parse(line):
    dt_str, tz_str = line.rsplit(' ', 1)
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    sign = 1 if '+' in tz_str else -1
    h, m = map(int, re.findall(r'(\d{2}):(\d{2})', tz_str)[0])
    offset = timedelta(hours=h*sign, minutes=m*sign)
    return dt - offset  # переводим в UTC

start = parse(input().strip())
end = parse(input().strip())

duration = int((end - start).total_seconds())
print(duration)