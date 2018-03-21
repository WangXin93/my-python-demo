import json
import re
data = json.load(open('./lecture_infos.json'))
for d in data[:10]:
    print(re.sub(r'时间.*$', '', d['speaker']))