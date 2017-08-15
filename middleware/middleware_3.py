#!/usr/bin/env python

import sys
import json
import logging
import random
import sqlite3

logging.basicConfig(filename='middleware_2.log', level=logging.DEBUG)
logging.debug('Middleware "modify_request" called')

def main():
    payload = sys.stdin.readlines()[0]

    logging.debug(payload)

    payload_dict = json.loads(payload)
    resp = payload_dict['request']['body']
    #out = resp.find("name")
    conn = sqlite3.connect("C:\Dev\sqlite\demo.db")
    logging.debug("Opened DB Successfully")
    cursor = conn.execute("select a, b from first")

    for row in cursor:
     a = row[0]
     b = row[1]
    #out = resp[9:15]

    conn.close()
    resp1 = "{\"name\":\"" + b +"\",\"job\":\"leader\",\"id\":\"" + str(a) + "\",\"createdAt\":\"2017-05-10T13:10:55.820Z\"}"

    if "request" in payload_dict and "path" in payload_dict["request"]:
        payload_dict["response"]["body"] =  resp1

    print(json.dumps(payload_dict))

if __name__ == "__main__":
    main()