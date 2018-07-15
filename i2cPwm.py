# I2C Pins
# GPIO2 -> SDA
# GPIO3 -> SCL

# Import the Library Requreid
import smbus
import time

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
# Slave Address 1
# address = 0x04

# Slave Address 2
address_2 = 0x05


# write 2 bytes number
def write_number(value):
    # bus.write_byte(address_2, value)
    bytes_for_send = int_to_bytes(value, 2)
    bus.write_block_data(address_2, 0x00, bytes_for_send)
    return -1

def bytes_to_int(byte_list):
    result = 0
    for b in byte_list:
        result = result * 256 + int(b)
    return result

def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    result.reverse()
    return result

def read_number():
    # number = bus.read_byte(address)
    number = bus.read_byte_data(address_2, 1)
    return number


while True:
    # Receives the data from the User
    data = input("Enter the data to be sent : ")
    data_list = [int(data)]
    for i in data_list:
        # Sends to the Slaves
        write_number(i)
        time.sleep(.1)

    # writeNumber(int(0x0A))
