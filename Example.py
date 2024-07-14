from ba63usb import BA63USB

def test():
    devs = BA63USB.get()
    dev = BA63USB(devs[0]["path"])

    dev.clear()
    dev.set_charset(0x34) # Change to 858 codepage Latin1+€
    dev.set_cursor(1,1)
    dev.print("Test °äöü€#*\n\rCount")

    for i in range(255):
        dev.print_at(f"{i}".ljust(3),2,7)
    

if __name__ == "__main__":
    test()