# import qrcode library
import pyqrcode

''' import png 
import png'''

''' import QRCode  
from pyqrcode import QRCode'''

# string which responce the qr code
v = "WEBSITE LINK"

# generate qrcode
url= pyqrcode.create(v)

# create and save svg file name =  "myqr.svg"
url.svg("myqr.svg",scale=8)

''' create png file and name = "myqr.png" '''
url.png("myqr.png",scale=6)
