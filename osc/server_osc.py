import OSC
import types

localhost = '127.0.0.1'
s = OSC.OSCServer(('0.0.0.0', 9999))
s.timeout = 0

def default_handler(addr, tags, stuff, source):
    print("SERVER : No handler registered for ", addr)
    return None

def user_callback(path, tags, args, source):
    #which user will be determined by path:
    #we just throw away all slashes and join together what's left
    #print(path,tags,args,source)
    user = ''.join(path.split("/"))
    
    print("Now do something with", user, args[0], args[1], args[2], args[3], args[4])
    print(path, tags,args, source)
    s.close()
    #return arg(path, tags, args, source)

    
def handler(addr, tags, data, client_adress):
    txt = "OSCMessage '%s' from %s: " %(addr, client_adress)
    txt +=str(data)
    print(txt)


    
#CONNEXION AU SYSTCAST SON IP ET PORT DE CONFIGURATION   
    
s.addMsgHandler('/startup', handler)
s.addMsgHandler("/Kart1/IP", user_callback)
#s.addMsgHandler("/Kart2/IP", user_callback)
#s.addMsgHandler("/Kart3/IP", user_callback)
#s.addMsgHandler("/Kart4/IP", user_callback)
print (s.getOSCAddressSpace())
s.serve_forever()


s = OSC.OSCServer(('0.0.0.0', 9999))
s.timeout = 0
client = OSC.OSCClient()
client.setServer(s)
client.connect(('192.168.1.3',8000))
configmsg = OSC.OSCMessage()
configmsg.setAddress("/Kart1/Target")
configmsg.append('iiiiii')
configmsg.append([127,0,0,1,8888])
configmsg.append(('172.20.10.3', 10001, 10002))

client.send(configmsg)
print(client)
print(configmsg)


     


    
    