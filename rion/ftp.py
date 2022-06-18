# pylint: disable-all
# pylint: skip-file
"""
simple FTP Handler
"""
import ftplib


class FTPHandler:
    """
    simple FTP Handler
    """

    def __init__(self, server: str, port: str, user: str, pwd: str):
        """
        Konstruktor
        """
        self.server = server
        self.port = port
        self.user = user
        self.pwd = pwd

    def download(self, file: str) -> None:
        """
        Download an File from a FTP Server
        @param file:
        @return:
        """
        server = ftplib.FTP()
        server.connect(self.server, int(self.port))
        server.login(self.user, self.pwd)
        server.retrbinary("RETR " + file, open(file, "wb").write)
