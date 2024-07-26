#!/usr/bin/env python3

import subprocess

def run_nmap_scan(target):
    try:
        # Run the nmap scan with basic options
        result = subprocess.run(['nmap', '-sV', '-O', target], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print(f"Nmap scan results for {target}:\n")
            print(result.stdout)
        else:
            print(f"Error running nmap scan on {target}: {result.stderr}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter the target IP or hostname: ")
    run_nmap_scan(target)
