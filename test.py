import pyepvp.session

with open("passwd.txt") as txt:
    passwd = txt.read()
#passwd = "my md5 hash password"
eddy = pyepvp.session.session("Der-Eddy", passwd, True)
print (eddy.securityToken)

guest = pyepvp.session.session("guest")
print (guest.securityToken)