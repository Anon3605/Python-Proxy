import requests

file01=open("Python Proxy\Proxylists.txt", "r")
file02=open("Python Proxy\Validproxys.txt", 'w')
for proxy_ip in file01:
    try:
        check_status_code=requests.get("http://icanhazip.com",
                                        proxies={"http": proxy_ip,
                                                "https": proxy_ip},
                                        timeout=1)
    except:
        continue
    if check_status_code.status_code==200:
        file02.write(f"{proxy_ip.strip()}\n")
print("Operation Finished")
