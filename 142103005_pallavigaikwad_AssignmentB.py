ip_add=str(input("Please enter the IP Address : "))

flag=0
address=0
octet_ip = ip_add.split(".")
subnet_mask = []
network_ip = []
broadcast_address=[]

for i in range(len(octet_ip)):
    octet_ip[i] = int(octet_ip[i])

if(((len(octet_ip)== 4) and \
   octet_ip[0] >= 192 and \
       octet_ip[0] <= 223 and \
           octet_ip[1] <= 255 and \
               octet_ip[2] <= 255 and \
                   octet_ip[3] <= 255)):
    print("\nThe entered IP Address (",ip_add, ") is VALID\n")
    
else :
    flag=1
    print("\nGiven IP Address ",ip_add, "is NOT VALID.Please enter a valid IP Address.\n")

if (flag != 1):
    
    print("Network id And Broadcast Address:")
    
    for i in range(8):
        changed_bits = i+1
        #Address to decimal
        for j in range(changed_bits):
            address = address + 2**(8-j-1)
            
        #class c subnet mask = 255.255.255.- - 
        prefix = 24 + changed_bits
        
        subnet_mask = [255,255,255,address]
        network_ip = [subnet_mask[0]&octet_ip[0],subnet_mask[1]&octet_ip[1],subnet_mask[2]&octet_ip[2],subnet_mask[3]&octet_ip[3]]
        host_start = [network_ip[0],network_ip[1],network_ip[2],network_ip[3]+1]
        
        for k in range(len(octet_ip)):
            network_ip[k] = str(network_ip[k])
            host_start[k] = str(host_start[k])
        
        network_id = ".".join(network_ip)
        print("\nCharacteristics of subnet no.: ",changed_bits)
        
        print("Network Id: ",network_id)
        
        broadcast_address=[octet_ip[0],octet_ip[1],octet_ip[2],address]
        host_end=[broadcast_address[0],broadcast_address[1],broadcast_address[2],broadcast_address[3]-1]
        
        for m in range(len(broadcast_address)):
            broadcast_address[m] = str(broadcast_address[m])
            host_end[m] = str(host_end[m])
        
        broadcast_id = ".".join(broadcast_address)
        
        print("Broadcast Address:",broadcast_id)
        
        host_start_str = ".".join(host_start)
        host_end_str = ".".join(host_end)

        print("Range of valid Host Address: ",host_start_str," - ",host_end_str)
        
else:
    print("Fallacy!")
    exit()
        
    
    
    
    



