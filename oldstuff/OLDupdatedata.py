from collections import OrderedDict
import json

hist = OrderedDict(json.load(open("log.txt", 'r')))

c=0

gawdsrt = ""

for key in hist:
    c+=1
    if(c>300): break;
    log = hist[key]

    usr = log['user']
    dat = log['date']
    msg = log['html']

    if("<img" in log['html']):
        msg = msg.replace('src=', 'src="loading.PNG" data-src=')

    dat = dat[:10] + "<br>" + dat[11:19]

    gawdsrt += "<tr><td>"+dat+"</td><td>"+usr+"</td><td>"+msg+"</td></tr>"


#open("index.html", 'w').write(open("template.html", 'r').read().replace("[SHITGOESHERE]", gawdsrt))
