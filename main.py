from PIL import Image

def encode():
    img = Image.open("sample.png")
    pesan = input("Masukkan pesan: ") + "###"

    binary = ''.join(format(ord(i), '08b') for i in pesan)

    data = list(img.getdata())
    new_data = []
    index = 0

    for pixel in data:
        r, g, b = pixel

        if index < len(binary):
            r = (r & ~1) | int(binary[index])
            index += 1
        if index < len(binary):
            g = (g & ~1) | int(binary[index])
            index += 1
        if index < len(binary):
            b = (b & ~1) | int(binary[index])
            index += 1

        new_data.append((r, g, b))

    img.putdata(new_data)
    img.save("output.png")
    print("Berhasil! output.png dibuat")

def decode():
    img = Image.open("output.png")
    data = list(img.getdata())

    binary = ""
    for pixel in data:
        for val in pixel[:3]:
            binary += str(val & 1)

    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    pesan = ""

    for c in chars:
        pesan += chr(int(c, 2))
        if pesan.endswith("###"):
            break

    print("Pesan:", pesan.replace("###", ""))

print("1. Encode")
print("2. Decode")

pilih = input("Pilih: ")

if pilih == "1":
    encode()
else:
    decode()
