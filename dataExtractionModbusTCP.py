# Import necessary modules
import struct
from pyModbusTCP.client import ModbusClient

# Create a Modbus TCP client and automatically connect to the specified host and port
client = ModbusClient(host="MACHINE_IP_ADDRESS", port=502, unit_id=1, auto_open=True)

# Read 8 input registers starting from address 1
registers = client.read_input_registers(1, 8)

# Check if the read was successful
if registers:
    print(registers)  # Print the read values
else:
    print("read error")

# Loop through the read values and print each one with its index
for i, register in enumerate(registers):
    print(f"REGISTER {i}: {register}")

# Combine the 16-bit values of the 4th and 5th registers into a 32-bit integer
third_register_bits = registers[4] << 16
fourth_register_bits = registers[5] << 16

# Combine the 16-bit values of the 6th and 7th registers into a 32-bit integer
last_two_registers_bits = (registers[6] << 16) + registers[7]

# Pack the 32-bit integer into a binary string and unpack it as a 32-bit floating-point number (IEEE 754)
packed_third_register = struct.pack('>L', third_register_bits)
final_third_register = struct.unpack('>f', packed_third_register)[0]

# Print the unpacked floating-point number
print(final_third_register)

# Pack the 32-bit integer into a binary string and unpack it as a 32-bit floating-point number (IEEE 754)
packed_fourth_register = struct.pack('>L', fourth_register_bits)
final_fourth_register = struct.unpack('>f', packed_fourth_register)[0]

# Print the unpacked floating-point number
print(final_fourth_register)

# Pack the 32-bit integer into a binary string and unpack it as a 32-bit floating-point number (IEEE 754)
packed_last_two_registers = struct.pack('>L', last_two_registers_bits)
final_last_two_registers = struct.unpack('>f', packed_last_two_registers)[0]

# Print the unpacked floating-point number
print(final_last_two_registers)
