import qrcode
import random
import os


def createHtml(path: str, count):
    with open(path + "/index.html", "w") as file:
        file.write(f'<html><img src="QR.png"><h1>{count}</h1></html>')


def createQr(url: str, currentNumbers, i):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    number = random.randint(0, 10000)
    while number in currentNumbers:
        number = random.randint(0, 10000)
    currentNumbers.add(number)
    os.mkdir(str(number))
    createHtml(str(number), i)
    name = f"{number}/QR.png"
    img.save(name)
    return name


# configurable
websiteURL = "https://wildbush76.github.io/"
endURL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=0gcJCdgAo7VqN5tD"
layers = 5


# end

numbers = set()
previousUrl = endURL
for i in range(1, layers + 1):
    previousUrl = websiteURL + createQr(previousUrl, numbers, i)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(previousUrl)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("root.png")
