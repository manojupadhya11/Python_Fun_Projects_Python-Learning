import qrcode as qr

#taking  value to convert that into QR code, taken youtube URL (Geeks for Geeks channel)
img = qr.make("https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ")

#qr code image name 
img.save("GFG_youtube.png")


