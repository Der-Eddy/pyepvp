import pyepvp.session

#with open("passwd.txt") as txt:
#    passwd = txt
passwd = ""
eddy = pyepvp.session.session("Der-Eddy", passwd, False)
print (eddy.securityToken)