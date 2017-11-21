# import MPU_9150_lib as MPU

# MPU.initialise()

bit_buffer = [0b01000011, 0b11001100, 0b01110101, 0b00001100, 0b11111100]
bit_buffer1 = 0b1100
bit_buffer2 = 0b1010

#print bin(bit_buffer)
temp_bit = (bit_buffer[1] << 8) | bit_buffer[0]
temp_bit = (bit_buffer[3] << 8) | bit_buffer[2]

print bin(temp_bit)

# ax = (((int16_t)bit_buffer[0]) << 8) | bit_buffer[1]

