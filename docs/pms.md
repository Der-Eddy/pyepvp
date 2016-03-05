Viewing and sending private messages
---
Currently in development

### Quick Reference Sending
#### *class* **pyepvp.privatemessage**(session, title, message, recipients[, bccrecipients=''[, icon="0"[, pm_id='Not yet initiliazed'[, date='Not yet initiliazed'[, newFlag=False]]]]])
#### *method* **pypepvp.privatemessage.send**([savecopy='1'])
### Quick Reference Viewing
#### *class* **pyepvp.privatemessages**(session[, folder=0])

### Sample Usage

    import pyepvp.privatemessages
    pm = pyepvp.privatemessages.privatemessage(session, 'Test', 'Test Message\r\neven with new lines!', 'Der-Eddy', icon='2').send()
