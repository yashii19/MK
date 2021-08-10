import OSC

c = OSC.OSCClient()
c.connect(('127.0.0.1', 9999))   # connect to localhost
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/startup")
oscmsg.append('HELLO')
print(oscmsg)
c.send(oscmsg)
print(c)