#!/usr/bin/python

import sys
import requests

def api_call(admin_url, rev_id):
    admin_url = 'https://pnr-webui-test-4admblue26189-varunrijhwani.devatron.net'
    url = "%s/api/policy/v3/casb/profiles/%s"(admin_url,rev_id)
    rsp = requests.get(url, headers = {"authorization":"339931c17ea948fcb1d6812118b210c2", "content-type" : "application/json"})

def main():
    try:
        api_call(sys.argv)
    except PermissionError as e:
        print(e)
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    main()
