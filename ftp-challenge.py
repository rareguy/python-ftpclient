from ftplib import FTP
import zipfile
import os.path, os

def helpMenu():
    print("FTP Client 0.1.1")
    print("Available commands:")
    print("LIST\t\t:Directory listing on the current directory")
    print("DOWNLOAD\t:Download a file from server")
    print("UPLOAD\t\t:Upload a file to server")
    print("CREATEDIR\t:Make a directory on the current directory")
    print("DELETEDIR\t:Delete a file from the server")
    print("UPTRACT\t\t:Extract a zip and upload it to the server")
    print("PWD\t\t:See current directory")

def placeFiles(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("Uploading: ", name, localpath)
            ftp.storbinary('STOR ' + name, open(localpath,'rb'))
        elif os.path.isdir(localpath):
            print("Making directory:", name)

            try:
                ftp.mkd(name)

            except error_perm as e:
                if not e.args[0].startswith('550'): 
                    raise

            print("Change directory:", name)
            ftp.cwd(name)
            placeFiles(ftp, localpath)           
            print("Change directory:", "..")
            ftp.cwd("..")

print("FTP CLI 0.1.1")
x = input('IP: ')
y = input('Username: ')
z = input('Password: ')

f = FTP(x)
print("Welcome Message:\n"), f.getwelcome()

f.login(y, z)
print ("Current working directory: " + f.pwd())
print("Type HELP to see available commands")

while True:
    command = input('>> ')
    if command == "LIST":
        a = f.mlsd()
        print('List of directory: ')
        for i in a:
            dire = "[" + i[1]['type'] +"]\t" + i[0] + "\t"
            print(dire)
    elif command == "DOWNLOAD":
        try:
            print('Enter file name (Press Ctrl+C or KeyboardInterrupt to cancel): ')
            b = input()
            fd = open(b, 'wb')
            f.retrbinary('RETR ' + b, fd.write)
            print ("Download "+ b +" success.")
            fd.close()
        except KeyboardInterrupt:
            print("Cancelled!")
            continue
        
    elif command == "UPLOAD":
        try:
            print('Enter file name (Press Ctrl+C or KeyboardInterrupt to cancel): ')
            c = input()
            fd = open(c, 'rb')
            f.storbinary('STOR ' + c, fd)
            print ("Upload " + c + " success.")
            fd.close()
        except KeyboardInterrupt:
            print("Cancelled!")
            continue
    elif command == "CREATEDIR":
        try:
            print('Enter directory name (Press Ctrl+C or KeyboardInterrupt to cancel): ')
            d = input()
            f.mkd(d)
            print ("Create "+ d + " directory success.")
        except KeyboardInterrupt:
            print("Cancelled!")
            continue
    elif command == "RENAME":
        try:
            e = input('Select file to rename (Press Ctrl+C or KeyboardInterrupt to cancel): ')
            g = input('Rename to (Press Ctrl+C or KeyboardInterrupt to cancel): ')
            f.rename(e, g)
            print ("Renaming from " + e + " to " + g +" success.")
        except KeyboardInterrupt:
            print("Cancelled!")
            continue
    elif command == "CHANGEDIR":
        h = input('Select directory: ')
        f.cwd(h)
        print ("Current working directory:", f.pwd())
    elif command == "DELETEDIR":
        try:
            print("Select directory to delete (Press Ctrl+C or KeyboardInterrupt to cancel): ")
            k = input()
            f.rmd(k)
        except KeyboardInterrupt:
            print("Cancelled!")
            continue
        print ("Delete success.")
    elif command == "UPTRACT":
        try:
            print('Select file to upload & extract (Press Ctrl+C or KeyboardInterrupt to cancel): ')
            j = input()
            if zipfile.is_zipfile(j):
                zip_ref = zipfile.ZipFile(j, 'r')
                os.mkdir(j[:-4])
                try:
                    zip_ref.extractall(j[:-4])
                except:
                    print ("Extract failed.")
                else:
                    print ("Extract success.")
                try:
                    placeFiles(f, j[:-4])
                except:
                    print ("Upload " + j + " failed.")
                else:
                    print ("Upload " + j + " success.")
        except KeyboardInterrupt:
            print("Cancelled!")
            continue
    elif command == "PWD":
        print ("Current working directory:", f.pwd())
    elif command == "HELP":
        helpMenu()

f.quit()
