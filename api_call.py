#!/usr/bin/python

import sys
import requests

def api_call(admin_url, rev_id):
    admin_url = 'f'
    url = ""()
    rsp = requests.get(url, headers = {"authorization":"", "content-type" : "application/json"})

def main():
    try:
        api_call(sys.argv)
    except PermissionError as e:
        print(e)
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    main()
