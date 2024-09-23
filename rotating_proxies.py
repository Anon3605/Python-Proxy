import requests
with open("Python Proxy\Validproxys.txt", "r") as valid_proxies:
    proxy_list=valid_proxies.read().strip().split("\n")
valid_proxies.close()
proxy_list.pop(-1)
print("Enter The sites you want to surf: ", end="")
sites=[x for x in input("Input Sites: ").split(",")]
info_file=open(f"Python Proxy\Files\Logs.txt","w")
for site in sites:
    print("Surfing Sites named: ",site)
    proxy_number=0
    while proxy_number<len(proxy_list):
        print(proxy_list[proxy_number])
        try:
            responds=requests.get(site, 
                                proxies={"http":f"{proxy_list[proxy_number]}",
                                        "https":f"{proxy_list[proxy_number]}"},
                                timeout=100)
            print(f"Proxy {proxy_list[proxy_number]} successful")
            info_file.write(f"{proxy_list[proxy_number]} requesting to *** \n{site}")
            info_file.write(responds.text)
        except requests.exceptions.ProxyError:
            print(f"ProxyError: The proxy {proxy_list[proxy_number]} is invalid or not responding.")
        except requests.exceptions.Timeout:
            print(f"TimeoutError: The proxy {proxy_list[proxy_number]} did not respond in time.")
        except requests.exceptions.RequestException as error:
            print(f"RequestException: An error occurred - {error}")
        finally:
            proxy_number+=1
            if proxy_number==len(proxy_list):
                print("Proxy limit Exceeded, Try to get valid proxies again...")
info_file.close()