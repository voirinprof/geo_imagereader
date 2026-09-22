import base64

filename = "data/raw/image_spuk.grd"
key = b"datcha"

def xor_data(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def read_grid(filename):
    with open(filename, "rb") as f:
        encoded_text = f.read()
    encrypted_data = base64.b64decode(encoded_text)
    decrypted_data = xor_data(encrypted_data, key)
    lines = decrypted_data.decode('utf-8', errors='ignore').splitlines()
    return lines

lines = read_grid(filename)
for line in lines[:13]:
    print(line)
