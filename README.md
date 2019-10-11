# success_rate


## OBJECTIVE

Using servers.txt as a list of servers, get json from endpoints eg http://hostname/status, and aggregate the reported success rates grouped by Application and Version.


## REQUIREMENTS

servers.txt must exist as a file in the same directory

No special system requirements except python3 and the following python modules:

requests
pandas
os
sys
concurrent

The system must have free disk space and the directory writable by the running user.



## HOWTO

Just execute the file using python, ie "python3 success_rate.py"

## ASSUMPTION

It is assumed hostnames that do not resolve or respond are safe to be ignored

Python append() assumed to be thread safe due to GIL


## TUNABLES

WORKER_THREADS: Default 200 worker threads are spawned in parallel, may hit limits in heavily loaded systems, can be raised for lightly loaded system

REQUEST_TIMOUT: Default timeout set to 1 second, expecting response within 1 second for endpoints capable of responding
