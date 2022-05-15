import requests
url='THIS_IS_URL'
response=requests.get(url)
if str(response)=='<Response [401]>':
    print('Success')
else:
    if str(response)!='<Response [401]>':
        print('Failed')