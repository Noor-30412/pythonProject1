# Import QRCode from pyqrcode
import pyqrcode

from pyqrcode import QRCode

# String which represents the QR code
s = '''Id=2100032420
        Name=Venky'''

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)