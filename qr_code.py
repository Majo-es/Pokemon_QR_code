import qrcode

website_link = 'https://www.pokemon.com/us'

qr = qrcode.QRCode(version = 5,
error_correction=qrcode.constants.ERROR_CORRECT_H, box_size = 10,  border = 5)
qr.add_data(website_link)
qr.make(fit = True)

img = qr.make_image(fill_color = 'darkred', back_color = 'white')

print(type(img))
print(img.size)

img.save('pokemon_qr.png')

