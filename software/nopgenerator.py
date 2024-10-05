data = []
for x in range(0, 0x4000):
    data += [0xea]


data[0x3FFC] = 0x00
data[0x3FFD] = 0xc0

data_bytes = bytearray(data)

with open("blank.bin", "wb") as bin_file:
    bin_file.write(bytes(data_bytes))
