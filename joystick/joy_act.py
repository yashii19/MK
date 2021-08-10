import evdev
from evdev import InputDevice, categorize, ecodes
import threading
from threading import Thread

#find the right input for the gamepads
def path_devices():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    res = []
    for device in devices:
        #print(device.path, device.name, device.phys)
        #print(device.name)
        if (device.name == "SHANWAN Android Gamepad"):
            res.append(device)
    return res

def namestr(obj,namespace):
    return [name for name in namespace if namespace[name] is obj][0]

def gamepad_touch(gamepad_list):
    
    aBtn = 304
    bBtn = 305
    xBtn = 308
    yBtn = 307
    lBtn = 310
    rBtn = 311
    selBtn = 314
    staBtn = 315

    
    #display codes
    for gamepad in gamepad_list:
        for event in gamepad.read_loop():
            #buttons
            if event.type == ecodes.EV_KEY:
        #        print(event.type)
                if event.value == 1:
                    if event.code == xBtn:
                        print(namestr(gamepad, globals())," : X")
                    elif event.code == bBtn:
                        print(namestr(gamepad, globals()), " : B")
                    elif event.code == aBtn:
                        print(namestr(gamepad, globals())," : A")
                    elif event.code == yBtn:
                        print(namestr(gamepad, globals()), " : Y")
                    elif event.code == lBtn:
                        print(namestr(gamepad, globals()), " : L1")
                    elif event.code == rBtn:
                        print(namestr(gamepad, globals()), " : R1")
                    elif event.code == selBtn:
                        print(namestr(gamepad, globals()), " : SELECT")
                    elif event.code == staBtn:
                        print(namestr(gamepad, globals()), " : START")

            #analog gamepad
            elif event.type == ecodes.EV_ABS:
                absevent = categorize(event)
                if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
                    if absevent.event.value == 0:
                        print(namestr(gamepad, globals()), " : JL_LEFT")
                    elif absevent.event.value == 255:
                        print(namestr(gamepad, globals()), " : JL_RIGHT")
         #           elif absevent.event.value == 127:
         #               print("JL_CENTER")
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
                    if absevent.event.value == 0:
                        print(namestr(gamepad, globals()), " : JL_UP")
                    elif absevent.event.value == 255:
                        print(namestr(gamepad, globals()), " : JL_DOWN")
        #            elif absevent.event.value == 127:
        #                print("JL_CENTER")
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Z":
                    if absevent.event.value == 0:
                        print(namestr(gamepad, globals()), " : JR_LEFT")
                    elif absevent.event.value == 255:
                        print(namestr(gamepad, globals()), " : JR_RIGHT")
        #            elif absevent.event.value == 127:
        #                print("JR_CENTER")
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_RZ":
                    if absevent.event.value == 0:
                        print(namestr(gamepad, globals()), " : JR_UP")
                    elif absevent.event.value == 255:
                        print(namestr(gamepad, globals()), " : JR_DOWN")
        #            elif absevent.event.value == 127:
        #                print("JR_CENTER")
            
            #elif event.type == ecodes.EV_ABS:
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0X":
                    if absevent.event.value == -1:
                        print(namestr(gamepad, globals()), " : B_LEFT")
                    elif absevent.event.value == 1:
                        print(namestr(gamepad, globals()), " : B_RIGHT")
                elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_HAT0Y":
                    if absevent.event.value == -1:
                        print(namestr(gamepad, globals()), " : B_UP")
                    elif absevent.event.value == 1:
                        print(namestr(gamepad, globals()), " : B_DOWN")


# creates objects gamepad
list_path = path_devices()
gamepad_list = []
#print(list_path)
nb_players = len(list_path)
#print(nb_players)
if (nb_players == 1):
    gamepad1 = InputDevice(list_path[0])
    gamepad_list.append(gamepad1)
if (nb_players == 2):
    gamepad1 = InputDevice(list_path[0])
    gamepad2 = InputDevice(list_path[1])
    gamepad_list.extend([gamepad1, gamepad2])
if (nb_players == 3):
    gamepad1 = InputDevice(list_path[0])
    gamepad2 = InputDevice(list_path[1])
    gamepad3 = InputDevice(list_path[2])
    gamepad_list.extend([gamepad1, gamepad2, gamepad3])
if (nb_players == 4):
    gamepad1 = InputDevice(list_path[0])
    gamepad2 = InputDevice(list_path[1])
    gamepad3 = InputDevice(list_path[2])
    gamepad4 = InputDevice(list_path[3])
    gamepad_list.extend([gamepad1, gamepad2, gamepad3, gamepad4])

#prints out device info at start

#print(gamepad1)
#print(gamepad2)
#print(namestr(gamepad1, globals()))
#gamepad_touch(gamepad1)
#gamepad_touch(gamepad2)
print(gamepad_list)
gamepad_touch(gamepad_list)


