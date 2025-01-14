import requests
import threading
from concurrent.futures import ThreadPoolExecutor

# 每个线程处理的 URL 数量
URL_BATCH_SIZE = 10

# 获取 URL 列表
def load_urls():
    with open("url.txt") as fp:
        return [line.strip() for line in fp]

# 处理 URL 的函数
def process_url(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            print(f"URL is valid: {url}")
            with open("save.txt", "a") as filesave:
                filesave.write(url + '\r\n')
        elif r.status_code == 302:
            with open("save.txt", "a") as filesave:
                filesave.write(f"{url} - this is a redirect (status 302)\r\n")
    except requests.RequestException:
        print(f"Error with URL: {url}")

# 主函数：通过线程池并发执行
def file_save():
    urls = load_urls()
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(process_url, urls)

if __name__ == '__main__':
    file_save()
print("over")