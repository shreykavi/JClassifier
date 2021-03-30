# import urllib.request
# from urllib.error import HTTPError, URLError
import os
import requests
import shutil

# urllib.request.urlretrieve(image_url, "local-filename.jpg")

for x in range (1,11): #TODO: make this 11 to 24 once all links included
    print("> Downloading images for Jordan {}s".format(x))
    fails = open('./data/downloads/fails_{}.txt'.format(x), "w+")
    # data = json.load(open('data/searches/{}.json'.format(x)))
    # prods = data['Products']
    path = './data/images/{}'.format(x)
    d_path = './data/downloads/{}'.format(x)
    try:
        os.mkdir(d_path) 
    except OSError as error: 
        print(error)

    for filename in os.listdir(path):
        f=open(path+'/'+filename, "r")
        lines = f.readlines()
        for idx, line in enumerate(lines):
            name = d_path+'/'+filename[0:-4]+ "_0" + str(idx+1) + ".png"
            # try:
            #     urllib.request.urlretrieve(line, name)
            # except (HTTPError, URLError):
            #     print("> Failed Download:\nLink: {}\nName:{}".format(line, name))
            #     fails.write("Link: {}\nName:{}\n\n".format(line, name))
            try:
                r = requests.get(line, stream=True, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                print("> Failed Download:\nLink: {}\nName:{}".format(line, name))
                fails.write("Link: {}Name:{}\n".format(line, name))

            if r.status_code == 200:
                with open(name, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
            else:
                print("> Failed Download:\nLink: {}\nName:{}\n".format(line, name))
                print("statuscode = {}".format(r.status_code))
                fails.write("Link: {}Name:{}\nReason: {}\n\n".format(line, name,r.status_code))
        f.close()
    fails.close()
