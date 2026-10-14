
import subprocess
import time
import re
from datetime import datetime

targets = ["1.1.1.1", "8.8.8.8", "google.com"]

def check_status():
    for target in targets:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = subprocess.run(
            ["ping", "-n", "1", "-w", "2000", target],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            status = "CONNECTION OK"

            match = re.search(
                r"time[=<](\d+)ms",
                result.stdout,
                re.IGNORECASE
            )

            if match:
                latency = match.group(1) + " ms"
            else:
                latency = "Unavailable"
        else:
            status = "CONNECTION DOWN"
            latency = "Unavailable"

        print(f"Check time: {current_time}")
        print(f"Target: {target}")
        print(f"Status: {status}")
        print(f"Latency: {latency}")

        with open("network_log.txt", "a") as file:
            file.write(
                f"{current_time} | {target} | "
                f"{status} | Latency: {latency}\n"
            )

        print("Monitoring result saved to network_log.txt")
        print("-" * 40)

while True:
    check_status()
    time.sleep(5)
