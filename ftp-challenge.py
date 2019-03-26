from ftplib import FTP
import zipfile
import os.path, os

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

x = input('IP: ')
y = input('Username: ')
z = input('Password: ')

f = FTP(x)
print("Welcome:"), f.getwelcome()

f.login(y, z)
print ("Current working directory: " + f.pwd())

while True:
    command = input('>> ')
    if command == "LIST":
        a = f.nlst()
        print('List of directory: ')
        for i in a:
            print(i)
    elif command == "DOWNLOAD":
        b = input('Enter file name: ')
        fd = open(b, 'wb')
        f.retrbinary('RETR ' + b, fd.write)
        print ("Download success.")
        fd.close()
    elif command == "UPLOAD":
        c = input('Enter file name: ')
        fd = open(c, 'rb')
        f.storbinary('STOR ' + c, fd)
        print ("Upload success.")
        fd.close()
    elif command == "CREATEDIR":
        d = input('Enter directory name: ')
        f.mkd(d)
        print ("Create directory success.")
    elif command == "RENAME":
        e = input('Select file to rename: ')
        g = input('Rename to: ')
        f.rename(e, g)
        print ("Rename success.")
    elif command == "CHANGEDIR":
        h = input('Select directory: ')
        f.cwd(h)
        print ("Current working directory:", f.pwd())
    elif command == "DELETE":
        k = input('Select file to delete: ')
        f.rmd(k)
        print ("Delete success.")
    elif command == "UPTRACT":
        j = input('Select file to upload & extract: ')
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
            print ("Upload failed.")
        else:
            print ("Upload success.")
    elif command == "PWD":
        print ("Current working directory:", f.pwd())
        

f.quit()
