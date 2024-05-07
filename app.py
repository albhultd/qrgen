import pyqrcode 
from pyqrcode import QRCode 
  
# Prompt the user to enter the link
string = input("Enter the link: ")
  
# Generate QR code 
url = pyqrcode.create(string) 
  
# Create and save the png file naming "myqr.png" 
url.svg("myyoutube.svg", scale = 8) 
