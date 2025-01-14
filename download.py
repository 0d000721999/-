import requests
import webbrowser
import time
with open("save.txt") as fp:
    for i in fp:
        url= i.strip()
        webbrowser.open(url)
        time.sleep(1)
with open("save.txt", "w") as fp:
    fp.truncate(0)
print("已全部下载完成")