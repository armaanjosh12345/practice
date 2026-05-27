import psutil
import platform

# Optimization: Cache static platform information to avoid redundant system calls
PLATFORM_SYSTEM = platform.system()
PLATFORM_VERSION = platform.version()

def get_system_stats():
    stats = {
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "platform": PLATFORM_SYSTEM,
        "platform_version": PLATFORM_VERSION,
    }

    battery = psutil.sensors_battery()
    if battery:
        stats["battery"] = f"{battery.percent}% {'(Charging)' if battery.power_plugged else '(Not Charging)'}"
    else:
        stats["battery"] = "N/A"

    return stats
