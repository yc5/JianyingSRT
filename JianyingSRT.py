import json

f = open('C:\\Users\\USER\AppData\\Local\\JianyingPro\\User Data\\Projects\\com.lveditor.draft\\DATETIME\\draft_content.json', encoding="utf-8")

data = json.load(f)

for idx, i in enumerate(data['materials']['texts']):
    print(idx+1)
    
    time_range = data['tracks'][1]['segments'][idx]['target_timerange']
    t = time_range['start']
    ans = t / 1000000
    print(f'{int(ans/3600%60):02}:{int(ans/60%60):02}:{int(ans%60):02},{int(t%1000000/1000):03}', end='')
    
    print(" --> ", end='')
    
    t = time_range['start'] + time_range['duration']
    ans = t / 1000000
    print(f'{int(ans/3600%60):02}:{int(ans/60%60):02}:{int(ans%60):02},{int(t%1000000/1000):03}')
    
    print(i['content'])
    print()

f.close()
