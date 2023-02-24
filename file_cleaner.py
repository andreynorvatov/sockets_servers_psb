# import os
#
#
# dir = 'dumps'
# file_cnt = 0
# for f in os.listdir(dir):
#     # print(f'{file_cnt+1} - {f}')
#     os.remove(os.path.join(dir, f))
#     file_cnt += 1
#
# print(f'Removed: {file_cnt} files')

import re


l = '''
</label>
<div class="readonly">19 октября 2022 г. 0:48</div>
</div>
</label>
<div class="not">21 уаца 332 г. 0:48</div>
'''

q = re.findall(r'</label>\n<div class="readonly">(.+?)</div>', l)
print(q)