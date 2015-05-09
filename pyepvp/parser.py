import requests
import bs4
import re

def getSections(session):
    #r = requests.get("http://www.elitepvpers.com/forum/main/announcement-attention-achtung-problem-multiaccounting-acc-trading.html", headers=session.headers, cookies=session.cookieJar)
    r = requests.get("http://www.elitepvpers.com/forum/main/announcement-attention-achtung-problem-multiaccounting-acc-trading.html?langid=1")
    soup = bs4.BeautifulSoup(r.content, "html5lib")
    return soup

content = getSections("")

print(type(content.optgroup))
print(content.find(tag="select", name="f"))
print(content.find(attrs={"label": "Site Areas"}))
print(content.find_all(re.compile("^s")))
for tag in content.find_all(re.compile("^optgroup")):
    print(tag)
print(content.find(class_="fjdpth0"))
print(content.find_all("option"))