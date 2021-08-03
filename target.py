import requests
import random
import threadpool

def title():
    print('+---------------------------------+')
    print('+ \033[032m漏洞: 备份文件 批量   \033[0m')
    print('+ \033[034m使用格式: python3 target.py    \033[0m')
    print('+ \033[032m域名格式: http://x.x.x.x    \033[0m')
    print('+ \033[032mAuthor: FF    \033[0m')
    print('+---------------------------------+')

list_rar = list(set([i.replace("\n", "") for i in open("rar.txt", "r").readlines()]))
suffix = ['.rar', '.zip', '.tar', '.tar.bz2', '.sql', '.7z', '.bak']
php = ['php.php', 'info.php', 'test.php', 'phpinfo.php']
headerss = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
def scan(urlx):

    ua = random.choice(headerss)
    headers = {'User-Agent': ua}
    # url1 = urlx + '/.svn/entries'
    # try:
    #     r = requests.head(url=url1, headers=headers, timeout=5)
    #     print(r.url + " : " + str(r.status_code))
    #     if r.status_code == 200:
    #         try:
    #             r1 = requests.get(url=url1, headers=headers, timeout=5)
    #             if 'dir' in r1.content and 'svn' in r1.content:
    #                     with open('svn.txt', 'a+')as a:
    #                         a.write(url1 + '\n')
    #             else:
    #                 pass
    #         except Exception as e:
    #             pass
    #     else:
    #         pass
    # except Exception as e:
    #     print(e)
    url2 = urlx + '/' + urlx.split(".", 2)[1]
    for x in suffix:
        url3 = url2 + str(x)
        try:
            ua = random.choice(headerss)
            headers = {'User-Agent': ua}
            r2 = requests.head(url=url3, headers=headers, timeout=5)
            print(r2.url + ' : ' + str(r2.status_code) + ' : ' + str(r2.headers["Content-Length"]))
            try:
                if int(r2.headers["Content-Length"]) > 100000 and r2.status_code == 200:
                    with open('backup.txt', 'a+')as b:
                        b.write(url3 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        except Exception as e:
            pass
    for x in list_rar:
        url4 = urlx + x.replace('\n', '')
        try:
            ua = random.choice(headerss)
            headers = {'User-Agent': ua}
            r6 = requests.head(url=url4, headers=headers, timeout=5)
            print(r6.url + " : " + str(r6.status_code) + ' : ' + str(r6.headers["Content-Length"]))
            try:
                if int(r6.headers["Content-Length"]) > 100000 and r6.status_code == 200:
                    with open('backup.txt', 'a+')as c:
                        c.write(url4 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        except Exception as e:
            pass
    # url5 = urlx + '/WEB-INF/web.xml'
    # try:
    #     r7 = requests.head(url=url5, headers=headers, timeout=5)
    #     print(r7.url + " : " + str(r7.status_code))
    #     if r7.status_code == 200:
    #         try:
    #             r8 = requests.get(url=url5, headers=headers, timeout=5)
    #             if '<web-app' in r8.content:
    #                 with open('webinf.txt', 'a+')as aa:
    #                     aa.write(url5 + '\n')
    #             else:
    #                 pass
    #         except Exception as e:
    #             pass
    #     else:
    #         pass
    # except Exception as e:
    #     pass
    url6 = urlx + '/' + urlx.split("//", 1)[1]
    for x in suffix:
        url7 = url6 + str(x)
        try:
            ua = random.choice(headerss)
            headers = {'User-Agent': ua}
            r9 = requests.head(url=url7, headers=headers, timeout=5)
            print(r9.url + ' : ' + str(r9.status_code) + ' : ' + str(r9.headers["Content-Length"]))
            try:
                if int(r9.headers["Content-Length"]) > 100000 and r9.status_code == 200:
                    with open('backup.txt', 'a+')as b:
                        b.write(url7 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        except Exception as e:
            pass
    for y in php:
        url10 = urlx + '/' + y
        try:
            ua = random.choice(headerss)
            headers = {'User-Agent': ua}
            r10 = requests.get(url=url10, headers=headers, timeout=5)
            print(r10.url + ' : ' + str(r10.status_code))
            try:
                if int(r10.status_code) == 200 and 'PHP Version' in r10.text:
                    with open('backup.txt', 'a+')as g:
                        g.write(url10 + '\n')
                else:
                    pass
            except Exception as e:
                pass
        except Exception as e:
            pass

if __name__=='__main__':
    title()
    print("\033[32m开始检测：\033[0m")
    urls = [z.strip() for z in open('url2.txt', 'r', encoding='utf-8')]
    pool = threadpool.ThreadPool(100)  # 定义线程池数
    reqs = threadpool.makeRequests(scan, urls)  # 定义函数和字典
    [pool.putRequest(req) for req in reqs]  # 遍历执行线程池
    pool.wait()
    print("\033[32m检测完毕！\033[0m")
