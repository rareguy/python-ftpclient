# Python FTP Client

Python code to manage files over FTP socket using ```ftplib ```. This code is using command line interfaces, for now.
Note: This is tested for Python 2.7. Have yet to test it on Python 3.x.
Before you can manage file, you need to specify the FTP IP address and login credentials.

## Changelog
```v0.1```
- Base project

```v0.1.1```
- Added PWD
- Making it usable for Python 3.x. As Python 2.7 will be deprecated on 2020.

## Features (shown on the interface)
### ```v0.1```

##### ```LIST```
This will list all the files on the FTP server.
```sh
>> LIST
List of directory:
...
```
##### ```DOWNLOAD```
This will download a file from the FTP server to the client.
```sh
>> DOWNLOAD
Enter file name: abc.txt
Download success.
...
```

##### ```UPLOAD```
This will upload a file from the client to the FTP server.
```sh
>> UPLOAD
Enter file name: abc.txt
Upload success.
...
```

##### ```CREATEDIR```
This will create a directory on the current working directory.
```sh
>> CREATEDIR
Enter directory name: rareguy
Create directory success
```

##### ```CHANGEDIR```
This will change the current working directory.
```sh
>> CREATEDIR
Select directory: rareguy
Current working directory: /rareguy
```

##### ```DELETE```
This will delete a file on the FTP server.
```sh
>> DELETE
Select a file to delete: abc.txt
Delete success.
```

##### ```UPTRACT```
This will upload a ```.zip``` file but instead of being a ```.zip``` file on the server, it will immediately be extracted from the zip. It works by extracting the zip on the local client, upload the full directory to the server, and then delete the extracted files on the client.
```sh
>> UPTRACT
Select file to upload & extract: test.zip
Extract success.
Upload success.
```

### ```v0.1.1```
##### ```PWD```
This will show where your current working directory.
```sh
>> PWD
Current working directory: /rareguy
```

Download Python:
[Python]

[Python]: <https://www.python.org/downloads/>
