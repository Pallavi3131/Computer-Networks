notation = int(input("Please enter the / notation from /24 to /30 :"))
changed_bits = notation - 24
address = 0

for i in range(changed_bits):
    address = address + 2**(8-i-1)

print("Result-")
print("Subnet mask for entered / notation is: 255.255.255.{}".format(address))
maximum_subnets = 2**(changed_bits)
print("The max no. of subnets:",maximum_subnets)

valid_hosts = ((2**(8 - changed_bits))-2)
print("The valid hosts address are:",valid_hosts)

print("The Subnet Range : 0 to ",address-1)

print("\n Here, Valid hosts addresses are all addresses except 255.255.255.",address-address," and 255.255.255.",address)




