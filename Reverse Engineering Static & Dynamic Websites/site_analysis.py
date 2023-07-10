import requests

url = "https://www.3m.com/snaps2/api/pcp-show-next/https/www.3m.com/3M/en_US/p/c/abrasives/?size=51&start=51"

payload = {}
headers = {
  'authority': 'www.3m.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cookie': 's_ecid=MCMID%7C59326459415538522070910865485264800156; ak_bmsc=2A66C34E518B693A33325959C1A9E6F0~000000000000000000000000000000~YAAQ9VM2F0ofnQGJAQAAblWbQBSJg3EDGAbX83meQ26LuI8QJ2ch1nK0lshW8B+4nnAI/oid6VURI0jInPQUorRvVk8AiOh/lZnCSPHzrp9JGkiDIg/ZpDk+VS8pAYkwtAiSzfFNnnJ2/Utq+ncH0isyc2SHTdFiiokrYeS9SnbrJc5+65PyM+HS78lLcPN56PI3EzxfTIOqpbR9vt6YSmXJox8Ypooz7JJHpMuzbx1765K4VibwzwR6qTnQF9YH/XB9Mt1C6c0wankmzViRorihopPxTEB9uiahGfiIxoP6TJxsTQvv1ReLjgjOQMDxBpEIQ/W3X/OVVcImTUqGR2y1HyfA3D6O5MsLT0DQuwNBl/XCfUE4BNyDAxHpbYAXvi6fnGhcJQhOxneaZuFKGy07g0oYII3Wtndg8Uc1f+aLkcm1aWlGSSWGL8HwPPPHct+9EuontR4pePVCfxbtNVKpxfqVCQAuk1f8I2Hax5RXXd0jSVdHh1qJVkcErcdrkN6LDewo8g6EQwNVEf/P; BVBRANDID=a6184fd6-9130-4f20-b858-4c01f6368295; ELOQUA=GUID=8E860A5BCD6148E182A4328F9D34C19B; gclid=undefined; _gcl_au=1.1.2076742939.1689006081; _fbp=fb.1.1689006082391.480510058; ln_or=eyIxNzA5NTUiOiJkIn0%3D; mdLogger=false; kampyle_userid=7534-c362-f052-0963-dea5-407f-1542-8224; _pin_unauth=dWlkPU1qQXdNR1U1TVdJdFpqYzVOeTAwWVRFeUxUbG1NREl0WWpGbFkyUmtZV05pTWpSbQ; _tt_enable_cookie=1; _ttp=t3NVKY9JJroxsZHVNJ4YlxQWIKX; at_check=true; rxVisitor=1689009946900FL861EQ1QLT3R843P5J9GNJRSQVT2CB8; BVBRANDSID=7c77af68-f5fa-49a3-a76d-06a088494437; mboxEdgeCluster=38; AMCVS_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1; AMCV_FEE4BDD95841FCAE0A495C3D%40AdobeOrg=1406116232%7CMCIDTS%7C19549%7CMCMID%7C59326459415538522070910865485264800156%7CMCAAMLH-1689614749%7C3%7CMCAAMB-1689614749%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1689017149s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.5.0; s_cc=true; dtCookie=v_4_srv_8_sn_SQ6BMKJL7KFLOSFEAR8R45T86CUARVNT_perc_100000_ol_0_mul_1_app-3A51e330a77f3260d5_1; ee1b5d445b4a4f48723fa58a17090439=d9b03c2380b72a24e6462e8180ead03f; 0f627b32de4b1b5c65ff57c6010a5e0b=e127fc05feeabc02c76602ab60c800da; kampylePageLoadedTimestamp=1689009953884; AKA_A2=A; rxvt=1689011822397|1689009946900; dtPC=8^$10019744_50h-vPFTMVKJPRNPRKROWDRDAAHJKWLARVGHF-0e0; dtSa=true%7CU%7C-1%7Csps2-pdp_pSelector--container%7C-%7C1689010029981%7C10019744_50%7Chttps%3A%2F%2Fwww.3m.com%2F3M%2Fen_5FUS%2Fp%2Fd%2Fv000176338%2F%7C%7C%7C%7C; RT="z=1&dm=www.3m.com&si=012f84d5-0116-42f9-a9a4-fcadb3ef84bf&ss=ljx4wvii&sl=5&tt=8m4&obo=3&rl=1"; AWSALB=B9bB1v3oqbiCdw0ne/ZSPHkSOIDlWjistg/YIlwfM6WnSXtcSiL5yxJlyKizIfNGBFr4M75MirZnzBSdeNkY6WGix8DPx6qf5PAnCGlxL/J58lvZWeDdWihj+/6Z; AWSALBCORS=B9bB1v3oqbiCdw0ne/ZSPHkSOIDlWjistg/YIlwfM6WnSXtcSiL5yxJlyKizIfNGBFr4M75MirZnzBSdeNkY6WGix8DPx6qf5PAnCGlxL/J58lvZWeDdWihj+/6Z; bm_sv=0DFBFD3FF7AF3F86452B8D2C9355EF89~YAAQN1ITApvJZgOJAQAABrPXQBTNMqbEYjDyXX0sVb5fg2G0J5eH6esHTtbAPdbNPdMBfDJgCKC4yZIZ/df7JxJs7B+MT/i9SfC9G7OtHFewEt8HWk4BQ9tqYW1MTCRHCPZ4T3mTjuQa3AxWITNQD3QnHEbGAbjqtdAuLEVQ1dz97fPFvSxUxGR7h3xAlG90mHzV8VDCOG7apb36p0vanLSx2O7J7o9KFfKOvAV8/R4seHYrcFiTa7XErd6j~1; mbox=PC^#6abc72b4a2364c87a54739dba8feef00.38_0^#1752254831|session^#f50c0c5a62224c89b6650cb7a6656c94^#1689011891; utag_main=v_id:0189409b70e40002ca932e71810d0506f002a06700bd0^$_n:2^$_e:11^$_s:0^$_t:1689011830752^$vapi_domain:3m.com^$dc_visit:2^$ses_id:1689009947864%3Bexp-session^$_n:6%3Bexp-session^$_revpage:MMM-ext%3Bexp-1689013630780^$dc_event:11%3Bexp-session^$dc_region:eu-central-1%3Bexp-session; _uetsid=ced424301f3d11eeb10a3d7803d842af; _uetvid=ced449801f3d11eea250916dd48c8bdd; adcloud={%22_les_v%22:%22y%2C3m.com%2C1689011830%22}; kampyleUserSession=1689010031420; kampyleUserSessionsCount=7; kampyleSessionPageCounter=1; kampyleUserPercentile=36.72192784829722; s_sess=%20tp%3D8696%3B%20s_ppv%3D%252F3M%252Fen_US%252Fp%252Fc%252Fabrasives%252F%252C100%252C24%252C8696%3B; s_pers=%20gpv_pN%3D%252F3M%252Fen_US%252Fp%252Fc%252Fabrasives%252F%7C1689011890493%3B%20gpv_pURL%3Dwww.3m.com%252F3M%252Fen_US%252Fp%252Fc%252Fabrasives%252F%7C1689011890494%3B; s_sq=3mproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253D%25252F3M%25252Fen_US%25252Fp%25252Fc%25252Fabrasives%25252F%2526link%253DShow%252520more%2526region%253DSNAPS2_root%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253D%25252F3M%25252Fen_US%25252Fp%25252Fc%25252Fabrasives%25252F%2526pidt%253D1%2526oid%253Dfunctionsn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; bm_sv=0DFBFD3FF7AF3F86452B8D2C9355EF89~YAAQrGV0aPNk1RCJAQAA73nZQBQgVrkg3qgub9U7FOim0nkhjEW3611SLZFEItrp5O59ifV/7NufFgKmzP2f6dafpp15O7dtmA5Cpwtbt2DpePh6lwVwK+AJ4L6Z9USrjdmo2IM/7223/17eWF07R6Th25JpcBnDTgaPiak7bEgoHISTkJpWt2QQYi0L+UP1t9VJYegbb7buq1KKtdGMM9fGktWi0Xayg5xnSsrVNEhd+2p1B/lQ6w2CR86z~1; AWSALB=acUoXi+f2gK7eYV05dsDbbtPKKs4qRKFGuXobaSklqF9FstpsFhdfJsxCwz1dQ326/NGWfcdZmI99L31Dj42iYZcaWHr1DTWwV+Km16nr6XH/bnTJLoCBV9P7O+N; AWSALBCORS=acUoXi+f2gK7eYV05dsDbbtPKKs4qRKFGuXobaSklqF9FstpsFhdfJsxCwz1dQ326/NGWfcdZmI99L31Dj42iYZcaWHr1DTWwV+Km16nr6XH/bnTJLoCBV9P7O+N',
  'referer': 'https://www.3m.com/3M/en_US/p/c/abrasives/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

obj = response.json()

urls = []
name = []
stock_num = []

for i in range(0,10):
    url = obj.get('items')[i].get('url')
    urls.append(url)

for i in range(0,10):
    names = obj.get('items')[i].get('name')
    name.append(names)

for i in range(0,10):
    stockN = obj.get('items')[i].get('stockNumber')
    stock_num.append(stockN)

print(stock_num, name, urls)

