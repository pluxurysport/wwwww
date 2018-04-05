class readwrite():
    def read(self):
        try:
            namefile = input("File name: ")
            with open(namefile, "rb") as r:
                byte = r.read(1)
                k = 0
                while byte:
                    try:
                        byte = r.read(1).decode("utf-8")
                    except:
                        continue
                    print(byte, end="")
                    k += 1
        except FileNotFoundError:
            print("\n[x] File: '" + str(namefile) + "' is not defined!")
            raise SystemExit
        else:
            print("\n[+] Number of bytes in the '" + str(namefile) + "': " + str(k))
    def write(self):
        try:
            namefile = input("File name: ")
            with open(namefile, 'ab') as file:
                text = input("Write the text: ")
                file.write(text.encode("utf-8"))
        except FileNotFoundError:
            print("[x] File: '" + str(namefile) + "' is not defined!")
            raise SystemExit
        else:
            print("[+] File: " + str(namefile) + " successfully overwritten!")
if __name__=='__main__':
    obj = readwrite()
    obj.write()
    obj.read()
