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
    
    cookies = 'MUID=296442F40A08612F2DC251930BDA6072; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=5B6636F873964FCF98DE8D53CC4E9849&dmnchg=1; _UR=QS=0&TQS=0; ANON=A=6D00A494BC5F05D52DFE0278FFFFFFFF&E=1cab&W=1; NAP=V=1.9&E=1c51&C=6kTquXV1K7V2LUCnbEZTEQ_fwQWpDRR58pp8PHepgHHKpg03jvQMEg&W=1; PPLState=1; MUIDB=296442F40A08612F2DC251930BDA6072; vdp=%7B%22ex%22%3Atrue%2C%22red%22%3Afalse%7D; MicrosoftApplicationsTelemetryDeviceId=6c10b423-06e9-4de6-8f0d-b8095e3ac9c4; MicrosoftApplicationsTelemetryFirstLaunchTime=2023-08-08T11:09:21.919Z; MSCC=cid=afy6eku0t9nxe2uplnhjxj9w-c1=2-c2=2-c3=2; MMCASM=ID=C9A3F3BFDBF84DF483F2132C93A3CE6C; ANIMIA=FRE=1; MUIDV=NU=1; GI_FRE_COOKIE=gi_prompt=1; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd&isADRU=0; _TTSS_OUT=hist=WyJlbiIsIml0IiwiemgtSGFucyJd; _EDGE_S=SID=1B9154E62657644A3ED14727271D65DC; WLS=C=655aa9915f2a28ab&N=%e6%99%af%e5%8b%87; _Rwho=u=d; GRNID=3d0a778a-1e86-4fac-a41c-54fd62b8c2f2; USRLOC=HS=1&ELOC=LAT=26.041475296020508|LON=119.20262908935547|N=%E9%97%BD%E4%BE%AF%E5%8E%BF%EF%BC%8C%E7%A6%8F%E5%BB%BA%E7%9C%81|ELT=6|; tifacfaatcs=CfDJ8J7TD5ChFXpDv5r23nhm9W9ZzMF3haW4wGrL_F0SbLw1baHJ4s-WdcuJldt60KyoU-K2Qb6P90p5fAfNR2rgmTeobz4wbT4Lmxe6EkQbSglkQV5hMdgXDNM9FOs8lSrKeOcLJAHJqGktDAMhE_qG66bJrgjaec9Y4-s0P3HY8XqwVSPwXsKorcqypKBGhIiUaPfqUihF6RQDbEmuAguv5LW3yQQYu6kjW0nyGLwAlTbvURoDxlNkJvjy4t_VwQfCd2RqsJ52aqYFVpxvS2B10bU-ZsdvQ1U1jUYMNDR31QZ_456vwYUNgxUkTFkLGLQEPQLfs95HgMeQjeQdYRScX5rXe7P1pDs8-z2WPfIKtMfZ4XdgnWgras1696U9JaxKP9c9uaNjWR8IokdIb95OP2KubNHNlBqPTUD00B6a26qyVmWTdKctODSzmxeq8BdsjHRZCgIGYwK9FvOOKTJfyTgOICHNPrymfV_kS3_VNFz8aVvB-TCztwF_aHWeNGLGbIy_2fSb8kjVTclfsmU9lHpi6tFB4oceadiOj0EdM-vYuxLBlAbiY1Ls0lFvsKj7MMkpNnxE5JunEiKH_dwuF0HyHWkDRpWHpLfaxCM15s55BWI5fAupLDNLDSxTcYf-21n8FXCuwJm7loziOXoQtZqrx3JKbY3zM2cC9tsplI_ufs6fuj3_JV6PN1Qso3CU5o7JSnaojaR6CNV1LzCB9hppvEn6JEEjf-Oj0Z8X9I5plvBEkrrKieFlkmhn7hEN4V5xFgxZQRurx9dDa4W0To7q34-Adk4UaQp3DcXo-_0-JpnHQn982zSdwSarm0Nuu0Lf5ns1Mtjs_W2GKx2SqvLy4CSG05-lk04qGCTW0EeBLqxOk8uiejd_q-_HrQ05Aj_OyT4-VeIHcLckc4FDBZ4hnT8kIgDx4Vb8gucELUOCYNSivC0ycDWZgRdChvUzuBSoeKtgvW26IPUQq4v5zzAkOOsWtfAWd46YMzn6UhylbtYr3LmQXavbkeCjYg8LFvnNC99_A3LH62C__bGc-lhofb-WqZsCo9_UJE6LYCu0KtAocY6t_N6FDiWF0hN5PdRNxPV-NDMr2z1S-WLAYKHbbUoJMaXTi76gwuwTighIO8brcZenyjC9VwhDrb5GmGcTz48KHpL8R2ghByg9d2pnfUcnl-2SVORIAT4rSalVIAnPPWG0W6O-UnJj7u0f0DTdoYBnHqGlVruIvC7i1Kfovo3DZ4sO52pZrDlHdfGG1B9GVWZFEMh1G3uK6fyy_htv1uizJiIEN-qm61kJriyWRYnp08Jb8fuEXz5thTk_zJKG62sSq8nojn-TqdXPaLqjQ-xv1cTpTD4q7NMC1qSR9FTUVgOlWlwnm0epTXTphJ321Qp0QhEKBPRz9_z8X8n31XR4n6jHGAhv9RW9RnZsXQDsUTlu2rKoUsHPVbTWjy1ypLxLCWnEw5GXAeRaYXQ_u0EHXHRFiv-fAlFOz7ytiYW5lvNqSRYGct7B88MkE6LtXWAaLVokX7lYMLdZqimDJQmrWpQNek04scwR0K9rjOGjh5lL2QnF2AUlyQuu4bktvRYJedBplU3izeof-LppNuU4rlp_XToNKUkdZ90AEwlR4yehOU2ODvaVJRvF0VdU_HrPAjBe5xZLflA7Muc4VigiUWMVAQqspRIjSaHVvO97oVOf0wIIjBKi7vULw19seP_Zh7GC63uH_fPPv2N5bjPJTu2CusWJ7NlQ2uU6KBT5JfKpttMqdv0yUmgmkOTjmB1bGKpIJz2KoJC4tP9y-l-El8RUH2OZmMsu5iUZ8aJcSWjSvpm6ElJQmyO_4wd8hJpHeO5djbom25tX6wXT4y2OUtNuFwO2nEy86_0ojO-M3-cZThve4ucAa9gxtzRU7LddoorVzaSqp69WIMZwV6M2CcQB9idOHVs3WHJ11Pjo4N5kNbhM2wbAl_gWJF6fML1XVerfe7Ovxy_ei6q5hGnKU15meXHJ8pGW9k0JYP7IM6SYtS4d7sAoUUk7xwB4XS016dVFELeJ04LyXePVngbqLNLaPinN1MiAWK9rm2VwaeQrO5_6tCjLPT60LLIlmns9267SxC3DBb8VoGi3w19XorfruWW4TJzfNZ3bFq_FNIZ3PF2O3ATgBVhyQFCpNfphP6F_uTwShWbk8KKb-ZeQ9k0S3ShjjIT-oUwPI7tAb7D1IXz4Q3-zXm8Hyeu1UJ63SkCNcMQrwwY0jiRfZ2kx38VCSLb3rqPuB1lRY8en483BHzA8VDAxjuGnVilk5Gq6JSkSBZ2YaZj_YMitE3jA0k26p9g59e9FizTdV4GPcXiwI8eyZ-cWX6k8msHVuBBwkITC0b9q1LVvbCEY2ESXcEZIgKAFR_63mRDDFMPGq_gnA-VWXdEbWJd3lroNMoZpx81MATjWH5RuyiRIa0sNdjhokkUXywLZED4JjEA5mEzNQnUe87sUYzlBtN7yv4kvzWVx-bqyPt1Lytuj0emQfdIuH62gHodyWgHPlEw5In0dbBhdqD-nLGeLmHJMn4rdJeMzQ0wwtuXKxmS272JhEQdUlDc6zf8jr9iBI_DQJaqJnye3vZ8yGm3VB1PYut6xQ6BqsUzZXlPOFrB1UWdVm2uT1j-FsPpUw42gXqo1yx4P7WC7USSKgEF4_dvDzhO2vMBkChNyEdp_CrXdk5moWpqxTg3H4hkTLB_IHliQVfXoyzvxLR4tnaFI83wNClT3jh_LU5qdr-xOqd_9PxXtaNNSAzI_Ktr164nZkQnA8vy3Mr4TAya1z2WENrc-mXiaQKwLQ7BPAGDgihQl41T4iQkzcAQw5vMXfncj_-YmUiHYo7A3HCTkU56ZEr_JounC1goTBMtBRRIU6rPAgvBl_7rE4pWPUjQl6r5KaP-BGrjuyBflSWkGnb1StpzFZ65ueY28qpGGOElw8Vvh_TwvEU2ObtJCTHC3pD9BWdZaO50dappxhvX22WVZJBPr8ZkEmf7XvfXVIX8KKNVr-P4Nc3NcMA9JFqIvCtSK1P7nbZ6aAcYRMOXZGSpKOkuktaag2OYXUNKegisTpf2Te-pwQUjncYxWyb-36-eZbWjzmETL5KahQrr1mbAJWh9wYPGm877MyWOnHoDgC5cgoCGpXneAivBHWwTdpTnfY63pxRUjF0alJCgqfPghibMiwRbde4ZSRo8mxv1ryg89EccVp_z9hCjVcmtnoomG_xaUjwedilcOlGEZ80xtjuXe4MHHzB71rBiCZ2UVncjbV58xStxcoWOTmVkM5vhD1EuZnBdapU1tPI7rZBG6EGOT4bc3htZ5kP4v7d5d8_Kx-FpHgqUE3v-_0FxqPWgudpahzkDkPDRjEBzpSMmrNb4LtIcfnJAAy7iRPJyNozQiNl_yZwHE1GoIBSzpBoum4-PgG6QUHCjnDuYa0EbUSve94QYgatdXpttMZ-C0Rn4s9c9Z02MMALHLrSo9CekwSC7ttGX7hTmoZfCSwJJBMMMqekPVDL90ZjwWl-RBIb_2leSSyYpNKegmtQ_m4AFnUqiYJWj-0u2-n2M9esYY; .AspNetCore.Antiforgery.icPscOZlg04=CfDJ8J7TD5ChFXpDv5r23nhm9W-lza-wc6KvPB5v9z6fVC6cYhohad2eF-mFZuFYYVwZEcq0JWO-wookiiG52BoNUPd5dxFzRnsbVEIf0UQ8RKAIwD5DCfQNHwR3oW-TwA2I634EEvWFdwzXoaAZ4f8faOM; SRCHS=PC=U531; BFPRResults=FirstPageUrls=66515FD0B981F14F4369DBFC9D8C6860%2C7D2A9C2D611732B12B2ABFB4F5C77693%2C807497D8186C92A7832BA20A1E749EE1%2CA7931D0C461FAA49D72889D63DAEB85D%2CEAC29DFED8C5239F8587E7C1FB7F7BF6%2C772C5A6F0189CC1A18343858A0259D84%2CDF3404192BFB560F0640BF4E731D8610%2CCAF9D4CFF8037EA44D6552911491BDD9%2CAEF6188A8652ED936290B314E4E8581F%2C47A51A84D6EC302CCBA4F33254B4DD23&FPIG=33D203BDAE204202BF258F8B4FFDFBEF; ABDEF=V=13&ABDV=13&MRB=0&MRNB=1699318997072; SRCHUSR=DOB=20230808&T=1699318996000; ipv6=hit=1699322601563&t=4; _clck=4v149t|2|fgi|1|1315; SNRHOP=I=&TS=; _U=1TQ1WeFMAWCAf1IM6uO-7ANFCtgX02PLcbDi2YHVLFm7Pajt_O_3c0VMno9Bi2MWc-vjnJGMaFvH8OFfyFDEim8PQp5rdxqzEU9EIDfFpCWQlWbLK1mZ1PtHAWaXE-Z2oBYDj9NKG4ksnwJo5YvvA7Sc74NNEPzMK4MLSlZwS3nky982sLvmKGNf6MnYnxdcV4k-VKp-NoO5Lqev91girLRnmwtZgaoofWw8535gfIS0; _HPVN=CS=eyJQbiI6eyJDbiI6MzMsIlN0IjoyLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjMzLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjozMywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMS0wN1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MTE0LCJIdG9iIjowfQ==; _RwBf=ilt=9&ihpd=2&ispd=7&rc=5598&rb=5598&gb=0&rg=0&pc=5598&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=22&l=2023-11-06T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=8637&s=2023-03-22T05:59:55.2529859+00:00&ts=2023-11-07T01:32:20.3760398+00:00&rwred=0&wls=0&wlb=0&lka=0&lkt=0&TH=&dci=3&mta=0&e=mFaoMRDmKvr07zgl-12Xx7YZanMXF7WVxEGICdM7AH1j6Davce3hfMPf1pUeNJMJEGgvu4myHaJmI5AdVUZjiw&A=&aad=0; _SS=SID=1B9154E62657644A3ED14727271D65DC&PC=U531&OCID=ML2BF0&R=5598&RB=5598&GB=0&RG=0&RP=5598; SRCHHPGUSR=BRW=XW&BRH=M&CW=1912&CH=932&SCW=1897&SCH=3090&DPR=1.0&UTC=480&SRCHLANG=zh-Hans&PV=3.0.0&HV=1699320741&BZA=0&PRVCW=1912&PRVCH=932&DM=1&EXLTT=31&IG=3A36D4462B434EBA99A6E641B801F2D6&THEME=1&WEBTHEME=0; _uetsid=357ec2507c4911eeaf09b3d07f48fbc9; _uetvid=2b056ae0365011eeaf594d5218a6908a; webisession=%7B%22impressionId%22%3A%222c59f95e-643d-440b-84a3-b8341db3d365%22%2C%22sessionid%22%3A%2251436ae7-9474-4633-ba18-a86d90ecc29a%22%2C%22sessionNumber%22%3A16%7D; _clsk=r5jal9|1699321813366|14|0|k.clarity.ms/collect; GC=kY2yn2cauTkRjQpgQFECGZ0yVwNUDOeW2G31GdgF0EqH8Kbtrp18KAf1D_k8C-BanVLZcya_fc0QIgJp4s6zMg'
    
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
      response = requests.post(url, headers=headers, data=data)     
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

   
