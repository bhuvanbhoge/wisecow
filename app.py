import psutil
import time

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

while True:

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: CPU usage is {cpu_usage}%")

    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        print(f"ALERT: Memory usage is {memory_info.percent}%")

    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        print(f"ALERT: Disk usage is {disk_info.percent}%")

    time.sleep(60)