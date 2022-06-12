# pylint: disable-all
# pylint: skip-file
"""
simple FTP Handler
"""
import urllib3
import os


class Conmanager:
    """
    simple FTP Handler
    """

    def __int__(
        self, server: str, port: str, protocol: str, user: str, pwd: str
    ) -> None:
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
        self.protocoll = protocol
        self.user = user
        self.pwd = pwd
        self.port = port

    def download(self, file: str, folder: str) -> None:
        """
        Download an File from a FTP Server
        @param file:
        @param folder:
        @return:
        """
        path = os.getcwd()
        os.chdir(folder)
        urllib3.urlretrieve(
            f"ftp://{self.user}:{self.pwd}@{self.server}:{self.port}", file
        )
        os.chdir(path)
