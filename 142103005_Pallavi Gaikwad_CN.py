import math

datasize = 0
while True:
    try:
        datasize = int(input("Please enter the datasize - "))
    except ValueError:
        print("Please, enter a valid integer")
        continue
    else:
        break
mtu = 0
while True:
    try:
        mtu = int(input("Please enter MTU size - "))
    except ValueError:
        print("Please, enter a valid integer\n")
        continue
    else:
        break
n = math.ceil((datasize - 20) / (mtu - 20))
if (datasize >= mtu):
    print("\nResult-")
    print("\nTotal no. of generated Fragments : ", n)
    print("\n******************************")
    for i in range(1, n):
        length = mtu
        flags = 1
        offset = math.ceil(((mtu - 20) * (i - 1)) / 8)
        print("Fragment number : ", i)
        print("Flag : ", flags)
        print("Length : ", length)
        print("Offset : ", offset)
        print("******************************")

final_length = (datasize - (mtu - 20) * (n - 1))
final_flags = 0
final_offset = ((mtu - 20) * (n - 1)) / 8
print("Final length : ", final_length)
print("Final flag : ", final_flags)
print("Final offset : ", final_offset)


if (datasize < mtu):
    print("\nIn this case the MTU size is greater than DATA size, therefore packet moves on to the next encapsulation phase without fragmentation:")