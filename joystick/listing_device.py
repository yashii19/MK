import evdev

def path_devices():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        #print(device.path, device.name, device.phys)
        #print(device.name)
        if (device.name == "SHANWAN Android Gamepad"):
            print(device.path)
            
path_devices()