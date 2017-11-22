def writeBits (devAddr, regAddr, bitStart, length, data, bit_return_value):
    b = bit_return_value
    if b != 0:
        mask = ((1 << length) - 1) << (bitStart - length + 1)
        data <<= (bitStart - length + 1)  # shift data into correct position
        data &= mask  # zero all non-important bits in data
        b &= ~mask  # zero all important bits in existing byte
        b |= data  # combine data with existing byte

        print bin(b)

def main():

    writeBits(0x2C,0x1b,2,2,0b11,0b101010001)

if __name__ == "__main__":
    main()