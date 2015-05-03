#-*- coding:utf-8 -*-
import requests
import http.cookiejar
import hashlib
import time
from . import regexp

class session:
    headers = {
        "User-Agent" : "linux:net.eddy-dev.pyepvp:v1.0dev (by Der-Eddy)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "de-DE,de;q=0.8,en-US;q=0.6,en;q=0.4",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3"
    }
    cookiejar = ""
    securityToken = ""
    content = ""

    def __init__(self, uname, passwd, md5bool=False):
        if md5bool == True:
            md5 = passwd
        else:
            md5 = hashlib.md5(passwd.encode("utf-8"));md5 = md5.hexdigest()
        self.login(uname, md5)

    def login(self, uname, md5):
        loginnurl = "http://www.elitepvpers.com/forum/login.php?do=login&langid=1"

        params = {
            "do": "login",
            "vb_login_md5password": md5,
            "vb_login_md5password_utf": md5,
            "s": "",
            "cookieuser": "1",
            "vb_login_username": uname, 
            "security_token": "guest"
        }

        r = requests.post(loginnurl, data=params, headers=self.headers)
        
        self.cookiejar = r.cookies

        r = requests.get("http://www.elitepvpers.com/forum/usercp.php", headers=self.headers, cookies=self.cookiejar)
        self.securityToken = regexp.regexp.match("SECURITYTOKEN = \"(\S+)\";", r.content)
        self.content = str(r.content)

    def logout(self):
        requests.get("http://www.elitepvpers.com/forum/login.php?do=logout&logouthash=" + securityToken, headers=self.headers, cookies=self.cookiejar)