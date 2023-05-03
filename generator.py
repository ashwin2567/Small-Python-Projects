import pyqrcode
content = "https://weatherappapitest.azurewebsites.net/city/hyderabad";
url = pyqrcode.create(content);
url.png("myqr.png", scale = 5);
print("QR generated Successfully.")