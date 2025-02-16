# import lib ที่ใช้
import requests     
import json
from datetime import datetime
import pandas as pd

# กำหนด url ที่จะยิง
url = "https://shopee.co.th/api/v2/item/get_ratings"    

# กำหนด headers ที่จะยิง
headers = {         
    "accept": "application/json",
    "accept-language": "th,en;q=0.9",
    "af-ac-enc-dat": "f877d4ba2c899b95",
    "af-ac-enc-sz-token": "gOabkcqMudEH15OJl3tu1w==|1Va2rh/NAP9BsnbnGVNvptXSI+NGbg4u7nnet0JJfC8/1gmyvlh4FZWPNWxCTFKEYgf4Q1Mg7+DEb+PhK7Q=|kVfZ0Y39RbYTm4tj|08|3",
    "content-type": "application/json",
    "cookie": "_gcl_au=1.1.874328553.1738160475; _fbp=fb.2.1738160474826.16490270327333683; _QPWSDCXHZQA=9f9739fa-e359-4d44-8660-40d4a0a79e37; REC7iLP4Q=d74b7b52-29bf-4453-a660-6d7179ac5de1; SPC_F=HWgMolHUZ9LwMR2o3yoru4kh5m5XlUWz; REC_T_ID=4c65415a-de4c-11ef-9fc8-fe918ae85701; SPC_SI=PKuQZwAAAABpczhucTF3TmJNRQAAAAAAbTRHY0hoM2o=; _gid=GA1.3.1054363950.1738160477; _gac_UA-61914165-6=1.1738160477.Cj0KCQiAwOe8BhCCARIsAGKeD5519dtejXXeM97WTJmHz6SD7QUgUImWm20xjzGHRNs6-SrbWdgRBzYaAhdFEALw_wcB; _gcl_aw=GCL.1738160702.Cj0KCQiAwOe8BhCCARIsAGKeD5519dtejXXeM97WTJmHz6SD7QUgUImWm20xjzGHRNs6-SrbWdgRBzYaAhdFEALw_wcB; _gcl_gs=2.1.k1$i1738160702$u212512342; _med=cpc; SPC_CLIENTID=SFdnTW9sSFVaOUx3qznjruriymgzdpsr; SPC_EC=.Mzk0VkU5ZmJCNHBnU3dCbbOINmdxSf5qoGH3SY4vko5Od8HcEbcflmnURBrhXFE4cHJ6JNl3kWF/+YjfNI8FEls00Y1o1gfkoRFiF+mTgUhov8roRDCg7rM2AmKMcUR63y/y2U2y5etBPLIJci0R6lyFRKs1Pa2h1zkEirWjOKjEZkC6OrrOUaSOlaC1eBTmC2bEQRAKzEXV7cCHpOWz/EhAfXwxz4KFXQ4/ldZrbHKsIIIlsl2i3lBWRX1FTeNF; SPC_ST=.Mzk0VkU5ZmJCNHBnU3dCbbOINmdxSf5qoGH3SY4vko5Od8HcEbcflmnURBrhXFE4cHJ6JNl3kWF/+YjfNI8FEls00Y1o1gfkoRFiF+mTgUhov8roRDCg7rM2AmKMcUR63y/y2U2y5etBPLIJci0R6lyFRKs1Pa2h1zkEirWjOKjEZkC6OrrOUaSOlaC1eBTmC2bEQRAKzEXV7cCHpOWz/EhAfXwxz4KFXQ4/ldZrbHKsIIIlsl2i3lBWRX1FTeNF; SPC_U=153471153; SPC_T_ID=HVNSsBjErVZr8WaMZjKM635ogNqrFC96KN3jAXGdHynAMlwjMdr94wOZr5sS/vPL/Sz9lskNajJ4hS6quZLUxEUkcQt0WzQ9Za6CUlUZx7JNgr4cJpwGWEKGUZTZQ1E0HOLM88/C7/dhZbcRSXAJpegvb+upxhjnCvaA7+d5x0o=; SPC_T_IV=U0hvdjNTZUJ2VHA1UzFjdA==; SPC_R_T_ID=HVNSsBjErVZr8WaMZjKM635ogNqrFC96KN3jAXGdHynAMlwjMdr94wOZr5sS/vPL/Sz9lskNajJ4hS6quZLUxEUkcQt0WzQ9Za6CUlUZx7JNgr4cJpwGWEKGUZTZQ1E0HOLM88/C7/dhZbcRSXAJpegvb+upxhjnCvaA7+d5x0o=; SPC_R_T_IV=U0hvdjNTZUJ2VHA1UzFjdA==; SPC_SC_SESSION=gK11oGeTWplz9OzKVPDaTpMqOTkZUmQq/nO8yi2VVaRNyje2bhSPLA7TdLO+MzOqS8/cJyRXh/50yiB1cjQ3mTOGPFB3tRGbfa56/X8NjUOHPx0ABmT4NEHjKvfv/tTE32FIC6f9NMNejyKmCij0+nshoNiZhfIWaqLjdOo6j5i2AyCbNma/tVijk+uP7EMPnJ9qFbTPqxNLeYL4Z+UL3UxggnzzT/+QSwkuMjSZB8zgItlDgxYBju8MmyYbroloTWq6eB3MwWsJHWAt2Fn4RCA==_1_153471153",
    "priority": "u=1, i",
    "referer": "https://shopee.co.th/Apple-AirPods-4-with-Active-Noise-Cancellation-by-Studio-7-i.301786571.27711386279?sp_atk=94fa3394-2496-4567-81fb-68b77971af2d&xptdk=94fa3394-2496-4567-81fb-68b77971af2d",
    "sec-ch-ua": "\"Not A(Brand);v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "x-api-source": "pc",
    "x-csrftoken": "kLLzH8HkxpFzUtwjFsnQsBxsNQ7SaOXT",
    "x-requested-with": "XMLHttpRequest",
    "x-sap-ri": "d4999b67fd5eda765677f83405016f413d0d4b4ef4392f1735de",
    "x-sap-sec": "IhY9k+LVYRwPyEVmzRbmz35mlRChz7HmRRbUz/HmARZMzQ2muRbuzMjmmRwJz0AmoRaWz3bmFAbSz+Vm4AZFzQHmtRZYzRblSzbmz32m/Ra3zQAmDRx9z2bmMAbwzcbmk5Zrz+6mHRaMz2HmrAbMz3Rm9zxIzKRmnRZez76miRx3zLHmyRZkzc5mvAxqzdbmqRatzBXmmRZZzc6m2Rx8zK2mVzbjz5XlpRxZz6Xm+RbHzNVmpzx7z+bm+zxUz35mzRbUyRbmXr+f/5bmqH5HRpSEwmY8lcX5uTNmz2bDmghSZLHlzRxY0mcNzRagMQraH2Xmz7hWz+IVHURgvpDZRw56UPL/ARbmz6",
}

for i in range(1,21,1):

    # กำหนด params ที่จะยิง เปลี่ยนค่า offset ทุกรอบให้เป็น 50->100->150->...->1000
    params = {
        'exclude_filter': '1',
        'fe_toggle': '',
        'filter': '0',
        'filter_size': '0',
        'flag': '1',
        'fold_filter': '0',
        'itemid': '27711386279',
        'limit': '50',
        'offset': str(i*50),
        'relevant_reviews': 'false',
        'request_source': '2',
        'shopid': '301786571',
        'tag_filter': '',
        'type': '0',
        'variation_filters': ''
    }
    # ทำการยิง API และเก็บค่าไว้ในตัวแปรชื่อ response
    response = requests.get(url, headers=headers, params=params)

    # เอาค่าที่เก็บไว้มาแปลงเป็นไฟล์ Json
    data = response.json()
    
    # Save ไฟล์ Json ไว้ในโฟลเดอร์ response
    file_name = "response/response_data_"+str(i)+".json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# กำหนดตัวแปร list เพื่อเก็บค่าทั้งหมดที่จะเอาไปใส่ใน Excel
list = []

for i in range(0,20,1):     # วน Loop 20 รอบตามไฟล์ Json ที่ Set ไว้
    with open("response/response_data_"+str(i+1)+".json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    for j in range(0,50,1):     # วน Loop 50 รอบตามข้อมูลไฟล์ Json ที่ Set ไว้ 50 ต่อไฟล์
        author_username = data["data"]["ratings"][j]["author_username"]     # เอาข้อมูล author_username เก็บไว้
        create_time = data["data"]["ratings"][j]["ctime"]                   # เอาข้อมูล ctime เก็บไว้
        rating_star = data["data"]["ratings"][j]["rating_star"]             # เอาข้อมูล rating_star เก็บไว้
        comment = data["data"]["ratings"][j]["comment"]                     # เอาข้อมูล comment เก็บไว้
        image = data["data"]["ratings"][j].get("images", None)              # เอาข้อมูล images เก็บไว้
        video = data["data"]["ratings"][j].get("videos", None)              # เอาข้อมูล videos เก็บไว้
        if video is not None:                                               # เช็คว่าเจอ videos มั้ย
           video = data["data"]["ratings"][j]["videos"][0]["url"]           # แปลงค่า url ให้ดูง่าย

        # เอาข้อมูลที่เก็บไว้ใส่ไปใน list
        data_dic = {}
        data_dic["author_username"] = author_username
        data_dic["create_time"] = str(datetime.fromtimestamp(create_time))
        data_dic["rating_star"] = rating_star
        data_dic["comment"] = comment
        data_dic["image"] = image
        data_dic["video"] = video
        list.append(data_dic)

# บันทึกข้อมูลทั้งหมดลง Excel
df = pd.DataFrame(list)
df.to_excel('data_output.xlsx')