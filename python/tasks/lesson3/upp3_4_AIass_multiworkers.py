### This sol skips the file creation on ip_addresses
### and utilizes the list straight forward
### It also uses subprocess.run instead of os.popen()

import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

ip_addresses = [f'10.2.10.{i}' for i in range(256)]

## The -W 100 flag is system dependent, change as seeing fit

def ping_ip(ip_address):
  try:
    result = subprocess.run(['ping', '-c', '1', '-W', '100', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


## Change the if clause when other checks than TTL are sought for

    if "TTL" in result.stdout or "ttl" in result.stdout:
      return f'{ip_address} is available'
    else:
      return f'{ip_address} is unavailable'

  except subprocess.SubprocessError as e:
    return f'{ip_address} ping failed with error: {e}'

print("Starting concurrent pinging...")

results = []

## Assess the amount of process workers - more for faster execution

"""
executor.submit(ping_ip, ip) schedules the function ping_ip(ip) to run in one of the threads.
This line of code uses a dictionary comprehension to create a dictionary (future_to_ip) that maps each Future object to its corresponding IP address.
A Future represents the result of an asynchronous computation. Here, each Future represents the task of pinging an IP address.
{executor.submit(ping_ip, ip): ip for ip in ip_addresses} means that for each IP address in ip_addresses, a task is submitted to executor, 
and the resulting Future is stored as the key, with the IP as the value.
This allows you to easily track which IP corresponds to which task.

"""

"""
as_completed(future_to_ip) is a utility that returns an iterator that yields Futures as they complete.
This means that instead of waiting for all tasks to finish, you get each completed Future as soon as it's done.
This is particularly useful for getting immediate feedback on each completed task, rather than waiting for all of them to finish.

"""

with ThreadPoolExecutor(max_workers=4) as executor:

  future_to_ip = {executor.submit(ping_ip, ip): ip for ip in ip_addresses}

  for future in as_completed(future_to_ip):
    ip = future_to_ip[future]

    try:
      result = future.result()
      results.append(result)
      print(result)
    except Exeption as exc:
      print(f'{ip} generated as an exception: {exc}')
      result.append(f'{ip} generated an exception: {exc}')

with open("tailscale_ippings.txt", "w") as writefile1:
  for result in results:
    writefile1.write(result + "\n") 

print("Pinging completed.")