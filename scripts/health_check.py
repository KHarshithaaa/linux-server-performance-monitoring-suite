import os
import shutil
import psutil

def run_health_check():
    print("=" * 45)
    print("      L1 AUTOMATED SYSTEM HEALTH AUDIT       ")
    print("=" * 45)

    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU Load: " + str(cpu_usage) + "%")
    if cpu_usage > 85:
        print("  ALERT: High CPU utilization detected!")

    mem = psutil.virtual_memory()
    print("Memory Usage: " + str(mem.percent) + "% (Used: " + str(mem.used // (1024**2)) + " MB / Total: " + str(mem.total // (1024**2)) + " MB)")
    if mem.percent > 80:
        print("  ALERT: High Memory utilization detected!")

    disk = shutil.disk_usage("/")
    disk_percent = round((disk.used / disk.total) * 100, 2)
    print("Root Disk Usage: " + str(disk_percent) + "% (Free: " + str(disk.free // (1024**3)) + " GB)")
    if disk_percent > 90:
        print("  ALERT: Low Disk Space detected!")

    try:
        with open("/proc/sys/fs/file-nr", "r") as f:
            parts = f.read().split()
            print("Open File Descriptors: " + parts[0] + " / " + parts[2])
    except Exception as err:
        print("Could not inspect file descriptors: " + str(err))

    print("=" * 45)

if __name__ == "__main__":
    run_health_check()
