# Usage: curl_no_proxy <URL>
  
import sys
import urllib2
   
if len(sys.argv) < 2:
    print('Usage: ' + str(sys.argv[0]) + ' <url>')
    sys.exit(-1)

u = sys.argv[1]

# install null proxy list
proxy_handler = urllib2.ProxyHandler({})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

try:
    req = urllib2.Request(u)
    r = opener.open(req)
    if  r.getcode() == 200:
        print r.read()
        sys.exit(0)
except Exception as e:
    print('Could not access ' + u + ' URL')
    sys.exit(-1)

# vim: tabstop=4 shiftwidth=4 expandtab smartindent
