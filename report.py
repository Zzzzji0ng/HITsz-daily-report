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
  '马'
]


def sendRequest():
    y=0
    
    cookies = 'MUID=296442F40A08612F2DC251930BDA6072; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=5B6636F873964FCF98DE8D53CC4E9849&dmnchg=1; MUIDB=296442F40A08612F2DC251930BDA6072; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=494e00cd-22bf-4c1e-8336-950d835ab739; ANON=A=6D00A494BC5F05D52DFE0278FFFFFFFF&E=1cab&W=1; NAP=V=1.9&E=1c51&C=6kTquXV1K7V2LUCnbEZTEQ_fwQWpDRR58pp8PHepgHHKpg03jvQMEg&W=1; PPLState=1; MSCC=cid=afy6eku0t9nxe2uplnhjxj9w-c1=2-c2=2-c3=2; MMCASM=ID=C9A3F3BFDBF84DF483F2132C93A3CE6C; ANIMIA=FRE=1; MUIDV=NU=1; GI_FRE_COOKIE=gi_prompt=1; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd&isADRU=0; _TTSS_OUT=hist=WyJlbiIsIml0IiwiemgtSGFucyJd; _EDGE_S=SID=1B9154E62657644A3ED14727271D65DC; WLS=C=655aa9915f2a28ab&N=%e6%99%af%e5%8b%87; _Rwho=u=d; _HPVN=CS=eyJQbiI6eyJDbiI6MzIsIlN0IjoyLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjMyLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjozMiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMS0wNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTEzLCJIdG9iIjowfQ==; USRLOC=HS=1&ELOC=LAT=26.041475296020508|LON=119.20262908935547|N=%E9%97%BD%E4%BE%AF%E5%8E%BF%EF%BC%8C%E7%A6%8F%E5%BB%BA%E7%9C%81|ELT=6|; _clck=4v149t|2|fgh|1|1315; SRCHS=PC=U531; _SS=SID=1B9154E62657644A3ED14727271D65DC&PC=U531&OCID=ML2BF0&R=5452&RB=5452&GB=0&RG=0&RP=5452; BFPRResults=FirstPageUrls=66515FD0B981F14F4369DBFC9D8C6860%2C7D2A9C2D611732B12B2ABFB4F5C77693%2C807497D8186C92A7832BA20A1E749EE1%2CA7931D0C461FAA49D72889D63DAEB85D%2CEAC29DFED8C5239F8587E7C1FB7F7BF6%2C772C5A6F0189CC1A18343858A0259D84%2CDF3404192BFB560F0640BF4E731D8610%2CCAF9D4CFF8037EA44D6552911491BDD9%2CAEF6188A8652ED936290B314E4E8581F%2C47A51A84D6EC302CCBA4F33254B4DD23&FPIG=33D203BDAE204202BF258F8B4FFDFBEF; SNRHOP=I=&TS=; _U=1fQdSVK92PLkIdPLiaMTKYWoqDxXx-oQnMCWoJBT4BrJbeJ19esWBmccxA4WEMnfLSvIXgthkAcobHBfwx_lSi2gLmjy9M-RxDlaIEbzeVRzeHr9W9DkivxEKWyyktiRpmdlj6VETIsYfJFgb0ely5UT2SbUcb3PLMuonKXmcBUvujG7W_fYzCK5V48NMJ7_-SH7aynAxm2n6OKgzikRMSOzIMv1zUgRlNPo6N5GglfQ; SRCHUSR=DOB=20230808&T=1699258520000; ipv6=hit=1699262123447&t=4; _uetsid=357ec2507c4911eeaf09b3d07f48fbc9; _uetvid=2b056ae0365011eeaf594d5218a6908a; GC=kY2yn2cauTkRjQpgQFECGZ0yVwNUDOeW2G31GdgF0EorAOAxDFRX4_hZEgcg5aBXOtcURCHZXSocOMKIJq1eSQ; _clsk=9bjg7m|1699259450349|3|1|k.clarity.ms/collect; ABDEF=V=13&ABDV=13&MRB=0&MRNB=1699259461188; _RwBf=ilt=9&ihpd=2&ispd=7&rc=5452&rb=5452&gb=0&rg=0&pc=5452&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=4&l=2023-11-06T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=8637&s=2023-03-22T05:59:55.2529859+00:00&ts=2023-11-06T08:31:01.6646937+00:00&rwred=0&wls=0&wlb=0&lka=0&lkt=0&TH=&dci=3&mta=0&e=mFaoMRDmKvr07zgl-12Xx7YZanMXF7WVxEGICdM7AH1j6Davce3hfMPf1pUeNJMJEGgvu4myHaJmI5AdVUZjiw&A=&aad=0; SRCHHPGUSR=BRW=XW&BRH=S&CW=1912&CH=513&SCW=1897&SCH=4335&DPR=1.0&UTC=480&SRCHLANG=zh-Hans&PV=3.0.0&HV=1699259462&BZA=0&PRVCW=1912&PRVCH=932&DM=1&EXLTT=31&IG=3A36D4462B434EBA99A6E641B801F2D6&THEME=1&WEBTHEME=0'
    
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
      print(referer)
      
      data = urllib.parse.quote('url=' + referer + '&V=web')
      print(data)
    
      
      
      # 发送请求
      response = requests.post(url, headers=headers, data=data)     
      
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

   
