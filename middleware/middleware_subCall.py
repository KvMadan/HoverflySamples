#!/usr/bin/env python

import sys
import json
import logging
import random
import requests

logging.basicConfig(filename='middleware_subCall.log', level=logging.DEBUG)
logging.debug('Middleware "middleware_subCall" called')

def main():
    payload = sys.stdin.readlines()[0]

    logging.debug(payload)

    payload_dict = json.loads(payload)
    resp = payload_dict['request']['body']

    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    b="Madan"
    logging.debug("----Response----");
    logging.debug(response.status_code);
    resp1 = "{\"name\":\"" + b +"\",\"job\":\"leader\",\"id\":\"" + str(response.status_code) + "\",\"createdAt\":\"2017-05-10T13:10:55.820Z\"}"


    if "request" in payload_dict and "path" in payload_dict["request"]:
        payload_dict["response"]["body"] =  resp1

    print(json.dumps(payload_dict))

if __name__ == "__main__":
    main()