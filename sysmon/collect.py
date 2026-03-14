"""Read basic stats straight from /proc and the filesystem (Linux only)."""
import os
import shutil
import time


def cpu_percent(interval=0.5):
    def snap():
        with open("/proc/stat") as f:
            parts = [int(x) for x in f.readline().split()[1:]]
        idle = parts[3] + parts[4]
        return idle, sum(parts)

    idle1, total1 = snap()
    time.sleep(interval)
    idle2, total2 = snap()
    dt = total2 - total1
    return round(100.0 * (1 - (idle2 - idle1) / dt), 1) if dt else 0.0


def mem_percent():
    info = {}
    with open("/proc/meminfo") as f:
        for line in f:
            key, val = line.split(":", 1)
            info[key] = int(val.split()[0])
    total = info["MemTotal"]
    avail = info.get("MemAvailable", info["MemFree"])
    return round(100.0 * (total - avail) / total, 1)


def disk_percent(path="/"):
    usage = shutil.disk_usage(path)
    return round(100.0 * usage.used / usage.total, 1)


def snapshot():
    return {
        "host": os.uname().nodename,
        "cpu": cpu_percent(),
        "mem": mem_percent(),
        "disk": disk_percent(),
        "ts": int(time.time()),
    }
