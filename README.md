# AWS Cloud Network Monitoring System

## Project Overview

This project monitors network connectivity to selected IP addresses and domain names using Python. It runs on an Amazon EC2 Linux instance and sends monitoring logs to Amazon CloudWatch for remote viewing.

## Technologies Used

- **Python** — monitoring logic and log generation
- **Amazon EC2** — runs the monitoring application
- **Amazon CloudWatch Logs** — stores and displays monitoring logs
- **AWS IAM Role** — grants the EC2 instance permission to interact with AWS services
- **Linux** — operating environment
- **Git and GitHub** — version control and project documentation

## Features

- Checks connectivity to `1.1.1.1`, `8.8.8.8`, and `google.com`
- Reports connection status
- Extracts ping latency when available
- Records timestamps, status, and latency in `network_log.txt`
- Repeats monitoring every five seconds
- Sends the log file to Amazon CloudWatch for centralized viewing

## Architecture

```text
Python Network Monitor
          |
          v
Amazon EC2 (Amazon Linux)
          |
          v
   network_log.txt
          |
          v
 Amazon CloudWatch Logs
```

## How It Works

1. Python sends ping requests to the configured targets.
2. The application checks the command result to determine connectivity.
3. It extracts latency when available.
4. Each result is displayed in the terminal and appended to `network_log.txt`.
5. The Amazon CloudWatch Agent collects the log file and sends events to CloudWatch Logs.

## AWS Configuration

- **Compute:** Amazon EC2
- **Operating system:** Amazon Linux 2023
- **Logging service:** Amazon CloudWatch Logs
- **Log group:** `/aws/ec2/network-monitor`
- **IAM:** EC2 role with `CloudWatchAgentServerPolicy`

## Run Locally

The current script uses Linux-compatible ping options. On a Linux system with Python 3 installed, run:

```bash
python3 network_monitor.py
```

Press `Ctrl + C` to stop monitoring.

## Learning Outcomes

Through this project, I practised Python subprocess execution, regular expressions, network connectivity troubleshooting, Linux commands, AWS EC2, IAM roles, CloudWatch Agent configuration, and centralized log monitoring.

## Limitations

Ping failures do not always mean the internet connection is down. Some hosts or networks may block ICMP requests. CloudWatch and other AWS resources may incur charges.

## Future Improvements

- Add network health statistics
- Configure CloudWatch alarms
- Improve error handling and log rotation
- Automate startup and recovery of the monitoring application

---

**Project status:** Implemented and tested on Amazon EC2 with logs visible in Amazon CloudWatch.
