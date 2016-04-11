Viewing and sending shoutbox messages
---
Currently in development

### Quick Reference Sending
#### *static method* **pypepvp.shoutbox.send**(session, message[, channel="general"])
### Quick Reference Viewing
#### *class* **pyepvp.shoutbox**(session[, site=[1, 1][, channel="general"]])
#### *method* **pyepvp.shoutbox.update**(session[, site=[1, 1][, channel="general"]])

### Sample Usage for viewing

    import pyepvp
    sb = pyepvp.shoutbox(session)
    for i in sb.messages:
        print((i['username'] + ' (' + i['usercolor'] + '): ' + i['message']).encode('utf-8'))

### Sample Usage for sending

    import pyepvp
    pyepvp.shoutbox.send(session, 'Ich bin ein Bot')
