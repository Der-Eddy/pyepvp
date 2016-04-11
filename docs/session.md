Creating a session
---
Creating a session is required for almost every single method in the library. By creating the authenticated session, you  provide login information that is used for logging into your elitepvpers account. Cookies get stored for further usage and are valid until you destroy the session or your scripts ends.

You can also use a guest session with the username `guest`. However, not every function will work with a guest session (e.g. Shoutbox, posting in a topic or TBM functions and such).

### Quick Reference
#### *class* **pyepvp.session**(uname[, passwd=None[, md5bool=False[, secretWord=None]]])

### Creating a user session object and using it

To create a session simple import the `pyepvp` module and use the `session` method

    import pyepvp
    eddy = pyepvp.session("Der-Eddy", passwordmd5hash, True, superSecretWord)
    #do something
    print (eddy.securityToken)

Everything but the username is optional, however you will need to provide either a plain or md5 hashed password if you want to use a user session.  You can also use the md5 hash of your password instead of your plain password by adding `md5bool=True`.  

Other Example

    eddy = pyepvp.session("Der-Eddy", normalPassword)

Or you can use it in a with statement

    with pyepvp.session("Der-Eddy", normalPassword) as eddy:
        #do something

However, keep in mind if you don't set a secret word then you can't use specific TBM functions.


### Creating a guest session

For that, simply use as username `guest`

    guest = pyepvp.session("guest")

Keep in mind that guest session has limited functionality
