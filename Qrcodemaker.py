import pyqrcode 
from pyqrcode import QRCode 

s=input()

url = pyqrcode.create(s) 

url.svg("myyoutube.svg", scale = 8) 