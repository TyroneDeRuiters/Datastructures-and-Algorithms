"""
Checks whether a given address is IPv4, IPv6 or neither.
Time Complexity: Constant
Space Complexity: Constant
"""

def checkIP(address):
    if("." in address and ":" not in address):
        address = address.split(".")
    elif(":" in address and "." not in address):
        address = address.split(":")
    else:
        return "Neither"
    ip = "Neither"
    if(len(address) == 4):
        ip = checkHelp(address, 10, "IPv4", 32)
    if(len(address) <= 8 and ip != "IPv4"):
        ip = checkHelp(address, 16, "IPv6", 128)
    return ip

def checkHelp(address, base, ip_type, max_bits):
    bits = 0
    flag = True
    ip = "Neither"
    for field in address:
        try:
            if(field == "" and ip_type == "IPv6"):
                continue
            else:
                bits +=  len(bin(int(field, base))[2:])
        except ValueError:
            flag = False
    if(bits <= max_bits and flag):
        ip = ip_type
    return ip

print(checkIP("1200:0:ab00:1234:0:2552:7777:1313"))
            

        
        
