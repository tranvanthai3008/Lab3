import bdfparser as bdf
import struct

data_file = bdf.Font('rainyhearts.bdf') 

def write_bitmap(bitmap, width):

    for strip in bitmap:
        bin_string = bin(int(strip, 16))[2:]
        if len(bin_string) < width:
            bin_string = (width-len(bin_string)) * '0' + bin_string
        bin_string = bin_string[:width]
        for pixel in bin_string:

            if pixel == '1':
                image.write(struct.pack('>B', 0))
                image.write(struct.pack('>B', 0))
                image.write(struct.pack('>B', 0))

            else:
                image.write(struct.pack('>B', 255))
                image.write(struct.pack('>B', 255))
                image.write(struct.pack('>B', 255))


def hex2byte(line):

    while line != '':
        num = int(line[0:4], 16)
        image.write(struct.pack('>H', num))
        line = line[4:]


with open('your_word.tiff', 'wb') as image:
    data_sign = data_file.glyphs

    while True:
        letter = input()
        if len(letter) == 1:
            break
        print("Only enter 1 letter!!!")

    width = data_sign[ord(letter)][2]
    height = data_sign[ord(letter)][3]

    header = '4d4d002a0000' + hex(width * height * 3 + 8)[2:]
    hex2byte(header)

    bitmap = data_sign[ord(letter)][-1]
    write_bitmap(bitmap, width)

    tag_0100 = '000e0100000300000001' + hex(width)[2:]
    hex2byte(tag_0100)
    hex2byte('0000')

    tag_0101 = '0101000300000001' + hex(height)[2:]
    hex2byte(tag_0101)
    hex2byte('0000')

    tag_0102 = '01020003000000030000' + hex(width * height * 3 + 182)[2:]
    hex2byte(tag_0102)

    tag_0103 = '010300030000000100010000'
    hex2byte(tag_0103)

    tag_0106 = '010600030000000100020000'
    hex2byte(tag_0106)

    tag_0111 = '011100040000000100000008'
    hex2byte(tag_0111)

    tag_0112 = '011200030000000100010000'
    hex2byte(tag_0112)

    tag_0115 = '011500030000000100030000'
    hex2byte(tag_0115)

    tag_0116 = '0116000300000001' + hex(height)[2:]
    hex2byte(tag_0116)
    hex2byte('0000')

    tag_0117 = '01170004000000010000' + hex(width * height * 3)[2:]
    hex2byte(tag_0117)

    tag_0118 = '01180003000000030000' + hex(width * height * 3 + 188)[2:]
    hex2byte(tag_0118)

    tag_0119 = '01190003000000030000' + hex(width * height * 3 + 194)[2:]
    hex2byte(tag_0119)

    tag_011c = '011c00030000000100010000'
    hex2byte(tag_011c)

    tag_0153 = '01530003000000030000' + hex(width * height * 3 + 200)[2:]
    hex2byte(tag_0153)

    end = '0000000000080008000800000000000000ff00ff00ff000100010001'
    hex2byte(end)

    print("Successfully create!")