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
    print("Querying Jordan {}".format(x))
    f=open("./data/new_searches/{}.txt".format(x), "w+")
    search_query = "Air Jordan Retro {}".format(x)
    for startx in range(1, 1001, 10):
        results = google_search(
            search_query, my_api_key, my_cse_id, searchType='image', start=startx)

        for result in results:
            f.write(result['link']+'\n')
        time.sleep(1)
    f.close()