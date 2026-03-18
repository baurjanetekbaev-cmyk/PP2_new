
#10
import re
c_str=input()
s_str=re.sub(r'([A-Z])',lambda x:'_'+x.group(1).lower(),c_str)
s_str=s_str.lstrip('_')
print(s_str)