Using the The Black Market API
---
To retrieve transaction from the TBM API you need to provide a `secretWord`. In case you don't have provided a secretWord you will get an `tbmSecretwordException`.
There are several ways to add a secretWord to work with.

### Setting a SecretWord

    import pyepvp.session
    import pyepvp.tbm
    eddy = pyepvp.session.session("Der-Eddy", passwordmd5hash, True, superSecretWord)
    transactions = pyepvp.tbm.tbm(eddy)
    #do something

You can also add a `secretWord` to your already created session

    import pyepvp.session
    import pyepvp.tbm
    eddy = pyepvp.session.session("Der-Eddy", passwordmd5hash, True) #No secretWord!
    eddy.secretWord = "superSecretWord"
    transactions = pyepvp.tbm.tbm(eddy)

Or you can directly provide a `secretWord` to the `tbm` constructor

    import pyepvp.session
    import pyepvp.tbm
    eddy = pyepvp.session.session("Der-Eddy", passwordmd5hash, True) #No secretWord!
    transactions = pyepvp.tbm.tbm(eddy, superSecretWord)

### Get your own transactions from the API

To get the JSON for your own transaction list, use the `tbm.retrieveTransactions` method

    transactions = pyepvp.tbm.tbm(eddy)
    tbmJSON = transactions.retrieveTransactions("received")
    print(tbmJSON[0])

Valid type arguments are `all`, `received` or `sent`

### Get the transactions from an other user as your session

In case you want to retrieve the transactions of an other than your session user, use the `custom` argument by providing the full link

    transactions = pyepvp.tbm.tbm(eddy)
    tbmJSON = transactions.retrieveTransactions(custom="https://www.elitepvpers.com/theblackmarket/api/transactions.php?u=984054&type=all&secretword=secretword")
