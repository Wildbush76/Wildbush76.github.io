import qrcode
import random
import os

import qrcode.image.svg


def createHtml(path: str, count):
    with open(path + "/index.html", "w") as file:
        file.write(f'<html><img src="QR.png"><h1>{count}</h1></html>')


def createQr(url: str, currentNumbers: list, i: int):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    number = random.choice(currentNumbers)
    currentNumbers.remove(number)
    os.mkdir(str(number))
    createHtml(str(number), i)
    name = f"{number}"
    img.save(name + "/QR.png")
    return name


# configurable
websiteURL = "https://wildbush76.github.io/"
endURL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&pp=0gcJCdgAo7VqN5tD"
layers = 1000


# end

numbers = [x for x in range(layers * 2)]
previousUrl = endURL
for i in range(1, layers + 1):
    if i % 10 == 0:
        print(f"Completed {i} layers")
    previousUrl = websiteURL + createQr(previousUrl, numbers, i)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(previousUrl)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white",
                    image_factory=qrcode.image.svg.SvgImage)
img.save("root.svg")


print("completed generation")
