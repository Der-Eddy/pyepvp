Creating a session
---
Creating a session is required for almost every single function in the library. By creating the authenticated session, you  provide login information that is used for logging into your elitepvpers account. Cookies get stored for further usage and are valid until you destroy the session or your scripts ends.

You can also use a Guest Session with the username `guest`. However, not every function will work with a guest session (e.g. Shoutbox, posting in a topic or TBM functions and such).


#### Creating a user session object and using it

To create a session simple import the `pyepvp.session` module and use the `session` function

    import pyepvp.session
    eddy = pyepvp.session.session("Der-Eddy", passwordmd5hash, True, superSecretWord)

Everything but the username is optional, you can also use either your password or a md5 hash of your passwort by using `md5bool=True`.  

Other Example

    eddy = pyepvp.session.session("Der-Eddy", normalPassword)

However, keep in mind if you don't set a secret world then you can't use specific TBM functions.


### Creating a guest session

For that, simply use as a username `guest`

    guest = pyepvp.session.session("guest")


### Getting Started
...