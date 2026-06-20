# 🔎 IP Lookup + Port Scanner

Enter an IP address and the tool looks it up and scans its ports using public APIs.

## ✨ What it does

- **IP lookup** — geolocation / network info for an IP via public APIs (e.g. [iplocation.net](https://iplocation.net)).
- **Port scan** — checks which ports respond on the target IP.
- Coloured terminal output for easy reading.

## 🖼️ Example / Showcase

<img width="361" height="350" alt="example output" src="https://github.com/user-attachments/assets/d1828c63-b686-4205-b7a4-5acc2c417f86" />

## 📦 Requirements

- Python 3.9+
- Python packages (see `requirements.txt`):
  - `requests`
  - `colorama`

## 🚀 Installation

```bash
git clone https://github.com/sqlsnxw/IP-lookup-Port-Scanner.git
cd IP-lookup-Port-Scanner
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python "ip lookup + port scanner.py"
```

Then enter the IP address you want to look up and scan when prompted.

## ⚠️ Responsible use

Only scan hosts and networks **you own or have explicit permission to test**.
Unauthorized port scanning may be against the law in your jurisdiction and against
the acceptable-use policies of networks and cloud providers. This tool is for
learning and authorized testing only.

## 🔌 APIs used

- IP information: [iplocation.net](https://iplocation.net)
