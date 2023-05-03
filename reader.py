from pyzbar.pyzbar import decode
from PIL import Image
#read image
img = Image.open("myqr.png");
content = decode(img);
print(content[0].data.decode());
