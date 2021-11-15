import mechanize
br = mechanize.Browser()
# br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open(r'https://www.kotaksecurities.com/TSTerminal/Platform/Account/LogIn')

forms = []
for form in br.forms():
    print(form)

for link in br.links():
    print(link.text, link.url)

for control in br.form.controls:
    print(control)
    # print("type=%s, name=%s value=%s" % (control.type, control.name, br[control.name]))


import requests
from requests import session
headers = {
    "Content-Type":"application/x-www-form-urlencoded" #You must send this
    }
payload = {
    'action': 'slds-form slds-p-around_large',
    'login_user': 'niveshs.sanghvi@lntinfotech.com',
    'login_password': 'Iloveaws@123' #Not the actual password . :)
}

with session() as c:
    c.post('https://partnercentral.awspartner.com/APNLogin', headers= headers, data=payload)
    response = c.get('https://partnercentral.awspartner.com/PartnerProfile')
    print(response.headers)
    print(response.text)
    # with open('response1.csv', 'wb') as itd:
    #         itd.write(response.content)
    #         itd.close()
