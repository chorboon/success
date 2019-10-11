#!/user/bin/env python3

import requests
import pandas as pd
import os,sys
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 200
REQUEST_TIMEOUT = 1

def main():
    resp_list = []

    # Check if the file exist


    if not os.path.isfile("servers.txt"):
        print("servers.txt file does not exist")
        sys.exit()
    
    # Open servers.txt file and read contents as input for endpoints

    with open("servers.txt","r") as endpoint_servers:
        processes = []
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            for server in endpoint_servers:
                url = 'http://{0}/status'.format(server.rstrip())
                processes.append(executor.submit(get_endpoint,url))
        for task in as_completed(processes):
            resp = task.result()
            if 'error' not in resp:
                resp_list.append(resp.json())
        df = pd.DataFrame(resp_list)
        df1 = df.groupby(["Application","Version"]).sum()
            
        # Calcuate new column Success_Rate using existing columns Success_Count/Request_Count 

        df1['Success_Rate'] = df1['Success_Count']/df1['Request_Count']
        print(df1)
        df1.to_json(r'Success_Rate.json')

def get_endpoint(url):
    try:
        resp = requests.get(url,timeout=REQUEST_TIMEOUT)
    except:
        return 'error'
    return resp


if __name__ == "__main__":
    main()

