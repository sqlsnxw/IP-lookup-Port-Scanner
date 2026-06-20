# IP Lookup + Port Scanner

You give it an IP address, it looks up info about that IP and scans its ports. It uses
public APIs (iplocation.net) for the lookup part.

## Example

<img width="361" height="350" alt="example output" src="https://github.com/user-attachments/assets/d1828c63-b686-4205-b7a4-5acc2c417f86" />

## Setup

```
pip install -r requirements.txt
```

## Running it

```
python "ip lookup + port scanner.py"
```

It'll ask you for an IP to look up and scan.

One thing: only scan hosts you actually own or have permission to test. Scanning random
machines on the internet can get you in real trouble, so keep it to your own stuff.
