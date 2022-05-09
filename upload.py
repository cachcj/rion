from ftplib import FTP
import sys
import os

# Load Data
USER = os.getenv('user')
PASSWORD = os.getenv('key')
SERVER = os.getenv('server')

# Load File
content = sys.argv[1]
print(content)

# Kill Switch
#sys.exit(0)

# Upload Settings
ftp = FTP(SERVER, USER, PASSWORD)
try:
    ftp.delete(sys.argv[1])
except Exception as e:
    print("Cannot delete")
file = open(sys.argv[1], 'rb')
ftp.storbinary('STOR ' + sys.argv[1], file)
ftp.quit()
