import os
import json
import time
# import pandas as pd
import requests

from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBEUFF0PTLdv70JV5CQ6uUjlbq-LQY43uo"
my_cse_id = "003009465364088444051:oej79comsvu"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, fileType='jpg', **kwargs).execute()
    return res['items']

for x in range (1,12):
    print("> Working on Jordan {}".format(x))
    data = json.load(open('data/new_searches/{}.json'.format(x)))
    prods = data['Products']
    path = './data/images/{}'.format(x)

    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    for prod in prods:
        f=open("./data/images/{}/{}.txt".format(x, prod['shortDescription']), "w+")
        for startx in range(21, 201, 10):
            results = google_search(
                prod['title'], my_api_key, my_cse_id, searchType='image', start=startx)

            for result in results:
                f.write(result['link']+'\n')
            time.sleep(1)
        f.close()