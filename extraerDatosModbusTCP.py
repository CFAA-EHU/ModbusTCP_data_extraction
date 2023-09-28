# Import necessary modules
import struct
from pyModbusTCP.client import ModbusClient

# Create a Modbus TCP client and automatically connect to the specified host and port
c = ModbusClient(host="MACHINE_IP_ADDRESS", port=502, unit_id=1, auto_open=True)

# Read 8 input registers starting from address 1
regs = c.read_input_registers(1, 8)

# Check if the read was successful
if regs:
    print(regs)  # Print the read values
else:
    print("read error")

# Loop through the read values and print each one with its index
for i in range(len(regs)):
    print("REGISTER " + str(i) + ": " + str(regs[i]))

# Combine the 16-bit values of the 4th and 5th registers into a 32-bit integer
bitsTERCERREGISTRO = (regs[4] << 16)
bitsCUARTOREGISTRO = (regs[5] << 16)

# Combine the 16-bit values of the 6th and 7th registers into a 32-bit integer
bitsJUNTOSDOSULTIMOSREGISTROS = (regs[6] << 16) + regs[7]

# Pack the 32-bit integer into a binary string and unpack it as a 32-bit floating-point number (IEEE 754)
s3 = struct.pack('>L', bitsTERCERREGISTRO)
final3registro = struct.unpack('>f', s3)[0]

# Print the unpacked floating-point number
print(final3registro)

# Pack the 32-bit integer into a binary string and unpack it as a 32-bit floating-point number (IEEE 754)
s4 = struct.pack('>L', bitsCUARTOREGISTRO)
final4registro = struct.unpack('>f', s4)[0]

# Print the unpacked floating-point number
print(bitsJUNTOSDOSULTIMOSREGISTROS)

# Pack the 32-bit integer into a binary string and unpack it as a 32-bit floating-point number (IEEE 754)
s2ultimos = struct.pack('>L', bitsJUNTOSDOSULTIMOSREGISTROS)
final2ultimos = struct.unpack('>f', s2ultimos)[0]
