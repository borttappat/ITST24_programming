import os

with open("ipaddresses.txt", "w") as writefile1:
  for i in range(256): 
    fileline = f'10.2.10.{i}\n'
    writefile1.write(fileline)

print("List of ipaddresses written to ipaddresses.txt")
print("Starting single pinging...")

ip_addresses = []

with open("ipaddresses.txt", "r") as readfile1:
  for line in readfile1:
     ip_addresses.append(line.rstrip()) 

ping_results = []

## The -W 100 flag is system dependent, change as seeing fit  

for ip_address in ip_addresses:
  single_ping = os.popen(f"ping -c 1 -W 100 {ip_address}")  
  ping_response = single_ping.read()

## Change the if clause when other checks than TTL are sought for

  if "TTL" in ping_response or "ttl" in ping_response:
    ping_result = f"{ip_address} is available"
  else:
    ping_result = f"{ip_address} is unavailable"

  print(ping_result)
  ping_results.append(ping_result)

print("Pinging completed")

with open("tailscale_ippings.txt", "w") as writefile1:
  for result in ping_results:
    writefile1.write(result + "\n")

print("Writing to file completed")