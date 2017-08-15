#!/usr/bin/env python

import sys
import json
import logging
import random
import requests

logging.basicConfig(filename='middleware_subCall_Post.log', level=logging.DEBUG)
logging.debug('Middleware "middleware_subCall_Post" called')

def main():
    payload = sys.stdin.readlines()[0]

    logging.debug(payload)

    payload_dict = json.loads(payload)
    resp = payload_dict['request']['body']

    url = "https://reqres.in/api/login"
    payload = {"email":"peter@klaven","password":"cityslicka"}
    response = requests.post(url, data=payload)
    b="Madan"
    logging.debug("----Response----");
    logging.debug(response.status_code);
    #resp1 = "{\"name\":\"" + b +"\",\"job\":\"leader\",\"id\":\"" + "1" + "\",\"createdAt\":\"2017-05-10T13:10:55.820Z\"}"
    resp1 = str(response.text)


    if "request" in payload_dict and "path" in payload_dict["request"]:
        payload_dict["response"]["body"] =  resp1

    print(json.dumps(payload_dict))

if __name__ == "__main__":
    main()