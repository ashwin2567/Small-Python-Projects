import pyqrcode
content = "https://weatherappapitest.azurewebsites.net/";
url = pyqrcode.create(content);
url.png("myqr.png", scale = 5);
print("QR generated Successfully.")