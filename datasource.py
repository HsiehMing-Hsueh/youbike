import requests


sarea_list = None
def getInfo():
    global sarea_list
    #下載資料
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    response = requests.get(url)
    #抓資料
    data_list = response.json()
    sarea_temp =set()
    for item in data_list:
        sarea_temp.add(item["sarea"])
    sarea_list = list(sarea_temp)
getInfo()
