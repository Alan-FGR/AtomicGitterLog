from collections import OrderedDict
import json

hist = OrderedDict(json.load(open("log.txt", 'r')))
data = []

for key in hist:
    log = hist[key]

    usr = log['user']
    dat = log['date']
    msg = log['html']

    if(len(msg) < 4):
        if ':' in msg:
            continue
	
    if("<img" in log['html']):
        msg = msg.replace('src=', 'src="loading.PNG" data-src=')

	dat = dat[:10] + "<br>" + dat[11:19]
	
    data.append({
		'user':usr,
		'date':dat,
		'html':msg
	})

open("log.json", 'w').write(json.dumps(data))#, indent=2))
