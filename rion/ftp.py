"""
simple FTP Handler
"""
import ftplib
import os
import urllib

class FTPHandler:
    """
    simple FTP Handler
    """

    def __int__(self, server: str, port: int, protocoll: str, user: str, pwd: str) -> None:
        """
        Konstruktor
        @param server:
        @param port:
        @param protocoll:
        @param user:
        @param pwd:
        @return:
        """
        self.server = server
        self.protocoll = protocoll
        self.user = user
        self.pwd = pwd
        self.port = str(port)

    def upload(self, file: str) -> None:
        """
        Upload an File to a FTP Server
        @param file:
        @return:
        """
        session = ftplib.FTP(self.server, self.user, self.pwd)
        file = open(self.file, 'rb')  #
        session.storbinary(f"STOR {self.file}", file)
        file.close()
        session.quit()

    def download(self, file: str, folder: str) -> None:
        """
        Download an File from a FTP Server
        @param file:
        @param folder:
        @return:
        """
        path = os.getcwd()
        os.chdir(folder)
        urllib.urlretrieve(f"ftp://{self.user}:{self.pwd}@{self.server}:{self.port}", file)
        os.chdir(path)
