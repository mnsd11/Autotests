import requests

with open('file.txt') as file:
    x = str(file.readline())
r=eval(x)

url2 = 'THIS_IS_URL'
headers2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection': 'keep-alive',
'Content-Length': '70',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': '_snrs_p=host:THIS_IS_URL&permUuid:0cefafe9-56a5-4580-9d2b-5b43b06de582&uuid:0cefafe9-56a5-4580-9d2b-5b43b06de582&emailHash:&user_hash:&init:1568840483&last:1569765417.321&current:1569765571&uniqueVisits:4&allVisits:44; _snrs_uuid=0cefafe9-56a5-4580-9d2b-5b43b06de582; _snrs_puuid=0cefafe9-56a5-4580-9d2b-5b43b06de582; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2019-09-29%2016%3A59%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2FTHIS_IS_URL%2Fservice%2Fdecoding_vin%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.ru%2F; sbjs_first_add=fd%3D2019-09-19%2000%3A01%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2FTHIS_IS_URL%2Fservice%2Fspecial%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28none%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D5%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A69.0%29%20Gecko%2F20100101%20Firefox%2F69.0; _ym_uid=156884048422467326; _ym_d=1568840484; _ga=GA1.2.814049024.1568840484; _gcl_au=1.1.54710140.1568840484; _fbp=fb.1.1568840484705.1363972775; NAME_PROJECT_SM_NAME_PROJECT_TMP_W=980; PHPSESSID=7PQQSCEBThy2aTxYYbWlO1WuRPBPkDrP; session-updated=7PQQSCEBThy2aTxYYbWlO1WuRPBPkDrP; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2FTHIS_IS_URL%2Fservice%2Fdecoding_vin%2F; _gid=GA1.2.1331705767.1569765418; _ym_isad=2; tmr_detect=0%7C1569765574571; NAME_PROJECT_TD_POPUP_HIT_COUNTER=1',
'Host': 'THIS_IS_URL',
'Referer': 'THIS_IS_URL',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
data2 = ({'sessid': 'c96a4541d3ee9ccd7a833bde12c8abeb', 'VIN': r[0], 'submit': 'Y'})  
req2=requests.post(url=url2,data=data2, headers=headers2)
newdata=req2.text
file2 = open('RES1.txt', 'w')
file2.write(newdata)

file_name = 'RES1.txt'
with open('RES1.txt', 'r') as text_file:
    lines = [3568]  # диапазон строк    #3558 or another = no inf
    i = 0    
    for line in text_file:
        if i in lines:
            i += 1
            print('line: ', line)
        else:
            i +=1 	
			
url3 = 'THIS_IS_URL'
headers3 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection': 'keep-alive',
'Content-Length': '70',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': '_snrs_p=host:THIS_IS_URL&permUuid:0cefafe9-56a5-4580-9d2b-5b43b06de582&uuid:0cefafe9-56a5-4580-9d2b-5b43b06de582&emailHash:&user_hash:&init:1568840483&last:1569765417.321&current:1569765571&uniqueVisits:4&allVisits:44; _snrs_uuid=0cefafe9-56a5-4580-9d2b-5b43b06de582; _snrs_puuid=0cefafe9-56a5-4580-9d2b-5b43b06de582; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2019-09-29%2016%3A59%3A31%7C%7C%7Cep%3Dhttps%3A%2F%2FTHIS_IS_URL%2Fservice%2Fdecoding_vin%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.ru%2F; sbjs_first_add=fd%3D2019-09-19%2000%3A01%3A23%7C%7C%7Cep%3Dhttps%3A%2F%2FTHIS_IS_URL%2Fservice%2Fspecial%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28none%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D5%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A69.0%29%20Gecko%2F20100101%20Firefox%2F69.0; _ym_uid=156884048422467326; _ym_d=1568840484; _ga=GA1.2.814049024.1568840484; _gcl_au=1.1.54710140.1568840484; _fbp=fb.1.1568840484705.1363972775; NAME_PROJECT_SM_NAME_PROJECT_TMP_W=980; PHPSESSID=7PQQSCEBThy2aTxYYbWlO1WuRPBPkDrP; session-updated=7PQQSCEBThy2aTxYYbWlO1WuRPBPkDrP; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2FTHIS_IS_URL%2Fservice%2Fdecoding_vin%2F; _gid=GA1.2.1331705767.1569765418; _ym_isad=2; tmr_detect=0%7C1569765574571; NAME_PROJECT_TD_POPUP_HIT_COUNTER=1',
'Host': 'THIS_IS_URL',
'Referer': 'THIS_IS_URL',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
data3 = ({'sessid': 'c96a4541d3ee9ccd7a833bde12c8abeb', 'VIN': r[1], 'submit': 'Y'})  
req3=requests.post(url=url3,data=data3, headers=headers3)
newdata3=req3.text
file3 = open('RES2.txt', 'w')
file3.write(newdata3)

file_name = 'RES2.txt'
with open('RES2.txt', 'r') as text_file:
    lines = [3568]  # диапазон строк
    i = 0    
    for line in text_file:
        if i in lines:
            i += 1
            print('line: ', line)
        else:
            i +=1 