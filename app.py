import pyqrcode 
from pyqrcode import QRCode 
  

string = input("Enter the link: ")  
url = pyqrcode.create(string) 
url.png("qr.png", scale = 8) 
