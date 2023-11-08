#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import requests
import time
from urllib.parse import urlencode
import urllib
from urllib import parse



keys = [
  '市民手牵手被风吹翻',
  '市民手牵手被风吹',
  '市民手牵手被风',
  '市民手牵手被',
  '市民手牵手',
  '市民手牵',
  '市民手',
  '市民',
  '市',
  '血型与疾病有相关性',
  '血型与疾病有相关',
  '血型与疾病有相',
  '血型与疾病有',
  '血型与疾病',
  '血型与疾',
  '血型与',
  '血型',
  '血',
  '女子乘车因价格跳车',
  '女子乘车因价格跳',
  '女子乘车因价格',
  '女子乘车因价',
  '女子乘车因',
  '女子乘车',
  '女子乘',
  '女子',
  '女',
  '唐嫣成了综艺判官',
  '唐嫣成了综艺判',
  '唐嫣成了综艺',
  '唐嫣成了综',
  '唐嫣成了',
  '唐嫣成',
  '唐嫣',
  '唐',
  '马龙不敌林的儒丢冠',
  '马龙不敌林的儒丢',
  '马龙不敌林的儒',
  '马龙不敌林的',
  '马龙不敌林',
  '马龙不敌',
  '马龙不',
  '马龙',
  '马',
  '河南郑州多名网友发布视频',
  '河南郑州多名网友发布视',
  '河南郑州多名网友发布',
  '河南郑州多名网友发',
  '河南郑州多名网友',
  '河南郑州多名网',
  '河南郑州多名',
  '河南郑州多',
  '河南郑州',
  '河南郑',
  '河南',
  '河',
  '昆明二手房价格已连跌19个月',
  '昆明二手房价格已连跌19个',
  '昆明二手房价格已连跌19',
  '昆明二手房价格已连跌1',
  '昆明二手房价格已连跌',
  '昆明二手房价格已连',
  '昆明二手房价格已',
  '昆明二手房价格',
  '昆明二手房价',
  '昆明二手房',
  '昆明二手',
  '昆明二',
  '昆明',
  '昆'
]


def sendRequest():
    y=0
    
    cookies = 'MUID=296442F40A08612F2DC251930BDA6072; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=5B6636F873964FCF98DE8D53CC4E9849&dmnchg=1; MUIDB=296442F40A08612F2DC251930BDA6072; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=494e00cd-22bf-4c1e-8336-950d835ab739; ANON=A=6D00A494BC5F05D52DFE0278FFFFFFFF&E=1cab&W=1; NAP=V=1.9&E=1c51&C=6kTquXV1K7V2LUCnbEZTEQ_fwQWpDRR58pp8PHepgHHKpg03jvQMEg&W=1; PPLState=1; MSCC=cid=afy6eku0t9nxe2uplnhjxj9w-c1=2-c2=2-c3=2; MMCASM=ID=C9A3F3BFDBF84DF483F2132C93A3CE6C; ANIMIA=FRE=1; MUIDV=NU=1; GI_FRE_COOKIE=gi_prompt=1; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd&isADRU=0; _TTSS_OUT=hist=WyJlbiIsIml0IiwiemgtSGFucyJd; _HPVN=CS=eyJQbiI6eyJDbiI6MzMsIlN0IjoyLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjMzLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjozMywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMS0wN1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTE2LCJIdG9iIjowfQ==; ABDEF=V=13&ABDV=13&MRB=0&MRNB=1699341748903; USRLOC=HS=1&ELOC=LAT=26.03900718688965|LON=119.19595336914062|N=%E9%97%BD%E4%BE%AF%E5%8E%BF%EF%BC%8C%E7%A6%8F%E5%BB%BA%E7%9C%81|ELT=4|; SRCHUSR=DOB=20230808&T=1699422920000; _uetsid=6e08d8f07dfb11eebf5af3d193e2926a; _uetvid=2b056ae0365011eeaf594d5218a6908a; _clck=4v149t|2|fgj|1|1315; _clsk=ga211d|1699422943298|2|0|k.clarity.ms/collect; GC=kY2yn2cauTkRjQpgQFECGZ0yVwNUDOeW2G31GdgF0Eqc30wHvmYN6BInyUbN1amivZQdRdLZT0TbriDWDUmcxw; _EDGE_S=SID=2F3BF4E63F9260F62A32E7253EBC6189; WLS=C=655aa9915f2a28ab&N=%e6%99%af%e5%8b%87; _U=1emcPNESJV2wI2mBEnd8SIptcm1i46pjti3P0uGYo0chzJ-yWKeJUsBUECVfHPLB3TqXEXeAhVloighEliNJUzHWO1E56XDYKTjeFY4JJaa67uScV0J_y_32_5Bz_GDYCL3cIHfikxVntnBdfs-mxtEyj59K-hjYZ3S-4L16FM4OITXvg1aAIsUBWfgXmdFXNcGzJ707DhGVswsFRBvh0YtrpH16nV4Z7QpDhunW5ZeI; SNRHOP=I=&TS=; _Rwho=u=d; ipv6=hit=1699426750676&t=4; _RwBf=ilt=9&ihpd=2&ispd=7&rc=5705&rb=5705&gb=0&rg=0&pc=5702&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=6&l=2023-11-07T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=BINGTRIAL5TO250P2'
    
    headers = {    
      'accept': '*/*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'zh-CN,zh;q=0.9',
      'content-type': 'application/x-www-form-urlencoded',
      'cookie': cookies,
      'origin': 'https://cn.bing.com',
      'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
      'sec-ch-ua-arch': "x86",
      'sec-ch-ua-bitness': "64",
      'sec-ch-ua-full-version': "118.0.5993.120",
      'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.120", "Google Chrome";v="118.0.5993.120", "Not=A?Brand";v="99.0.0.0"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-model': "",
      'sec-ch-ua-platform': "Windows",
      'sec-ch-ua-platform-version': "3.0.0",
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': '*',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
      'Host': 'cn.bing.com'
    }
    
    # cookies = {
    #     'cookie_name': 'cookie_value'  # 设置cookies
    # }
    
    for key in(keys):
      # url = 'https://cn.bing.com/rewardsapp/reportActivity?IG=77463973657B464ABAE3CB682928B018&IID=SERP.5056&q={{urlEncode_content}}&qs=PN&sc=8-0&cvid=C94F9B4B10CE409B94C1E2EA0D328615&FORM=QBLH&sp=1&lq=0'
      params1 = {
        'IG': "77463973657B464ABAE3CB682928B018",
        'ID': "SERP.5056",
        'q': key,
        'qs': 'PN',
        'sc': '8-0',
        'cvid': 'C94F9B4B10CE409B94C1E2EA0D328615',
        'FORM': 'QBLH',
        'sp': '1',
        'lq': 0
      }
      base_url = "https://cn.bing.com/rewardsapp/reportActivity?"
      url = base_url + urlencode(params1)
      print(url)
      
      
      params2 = {
        'q': key,
        'qs': 'PN',
        'sc': '8-0',
        'cvid': 'C94F9B4B10CE409B94C1E2EA0D328615',
        'FORM': 'QBLH',
        'sp': '1',
        'lq': 0
      }
      base_url1 = 'https://cn.bing.com/search?'
      referer = base_url1 + urlencode(params2)
      headers['referer'] = referer
      # print(referer)
      
      data = urllib.parse.quote('url=' + referer + '&V=web')
      # print(data)
    
      
      
      # 发送请求
      response = requests.post(url, headers=headers, data=data, cookies=cookies)     
      print(response)
      
      # 睡眠1s
      time.sleep(1)
    
      
       
    return y

 
if __name__ == "__main__":
    print ('This is main of module "hello.py"')
    sendRequest()
    print(__name__+'from hello.main')

 # finally:
 #        current = datetime.today().strftime('%Y-%m-%d_%H:%M:%S')
 #        if arguments.sckey:
 #            requests.get(f'https://sc.ftqq.com/{arguments.sckey}.send?text={report_msg}{current}')
 #            logging.info("微信提醒消息已发送。")

   
