import os

url1 = "http://image.data.cma.cn/vis/RAD__B0_CR/"
url2 = "/Z_RADA_C_BABJ_"
url3 = "_P_DOR_ACHN_CREF_"
num = 0
count = 0
var = 0
date=input("please input the date:  ")
date=str(date)
print("you input the date: ", date)
# 打开文件进行写入
with open("url.txt", "w") as file:
    # 循环直到达到或超过235400
    while num <= 235400:
        var = 0
        i=0
        formatted_num = f"{num:06d}"
        url4 = "_" + formatted_num + ".png"
        if num==235400:
            for i in range(49,60):
                i+=1
                i=f"{i:06d}"
                i=str(i)
                date2=str(int(date)+1)
                url=url1 + date + url2 + date2 + i + url3 + date + url4
                file.write(url+"\n")
            break
        # 每10次循环后，进位
        if count == 9:
            count = 0
            for var in range(num+4649,num+4720):
                var += 1
                var = f"{var:06d}"
                var = str(var)
                url = url1 + date + url2 + date + var + url3 + date + url4
                file.write(url + "\n")


            num -= 5400
            num += 10000
        else:
            for var in range(num+649, num +720):
                var += 1
                var = f"{var:06d}"
                var = str(var)
                url = url1 + date + url2 + date + var + url3 + date + url4
                file.write(url + "\n")  # 将URL写入文件，每个URL占一行
            num += 600
            count += 1

print("所有URL已保存到 url.txt")
