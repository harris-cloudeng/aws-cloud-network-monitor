# AWS Linux Server Setup

## Project
AWS Cloud Network Monitoring System

## Environment
- Cloud provider: Amazon Web Services (AWS)
- Compute service: Amazon EC2
- Operating system: Amazon Linux 2023
- Programming language: Python 3
- Logging service: Amazon CloudWatch Logs

## Setup Steps

### 1. Launch an EC2 Instance
- Launch an Amazon Linux 2023 instance.
- Connect using EC2 Instance Connect.
- Verify Python is installed:

```bash
python3 --version
```

### 2. Clone the GitHub Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd aws-cloud-network-monitor
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of this project's repository.

### 3. Run the Network Monitor

```bash
python3 network_monitor.py
```

The script checks connectivity to configured IP addresses and domain names, reports status and latency, and appends results to `network_log.txt`.

Press `Ctrl + C` to stop the monitoring loop.

### 4. Configure IAM Permissions
- Create an IAM role trusted by the EC2 service.
- Attach `CloudWatchAgentServerPolicy`.
- Associate the role with the EC2 instance.

### 5. Install the CloudWatch Agent

```bash
sudo yum install amazon-cloudwatch-agent -y
```

### 6. Configure CloudWatch Logging

Create the CloudWatch Agent configuration file at:

`/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json`

Configure the agent to collect the `network_log.txt` file and send its contents to the log group:

`/aws/ec2/network-monitor`

### 7. Start the CloudWatch Agent

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config \
  -m ec2 \
  -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json \
  -s
```

Verify its status:

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a status
```

## Skills Demonstrated
- Linux command-line operations
- Python subprocess execution
- Network connectivity troubleshooting
- AWS EC2 deployment
- IAM roles and permissions
- CloudWatch Agent configuration
- Centralized log collection

## Security Notes
- Never upload private keys, AWS access keys, passwords, or other credentials.
- Review AWS billing and stop resources when they are not needed.
- Ping failures may reflect ICMP filtering rather than a complete internet outage.

## Project Status
Successfully tested on Amazon EC2, with monitoring logs visible in Amazon CloudWatch Logs.
