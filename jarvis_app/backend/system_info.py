import psutil
import platform

# Optimization: Cache static system info to avoid redundant system calls on every request.
SYSTEM = platform.system()
SYSTEM_VERSION = platform.version()

def get_system_stats():
    stats = {
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "platform": SYSTEM,
        "platform_version": SYSTEM_VERSION,
    }

    battery = psutil.sensors_battery()
    if battery:
        stats["battery"] = f"{battery.percent}% {'(Charging)' if battery.power_plugged else '(Not Charging)'}"
    else:
        stats["battery"] = "N/A"

    return stats
