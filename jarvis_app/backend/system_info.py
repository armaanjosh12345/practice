import psutil
import platform

def get_system_stats():
    stats = {
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
        "platform": platform.system(),
        "platform_version": platform.version(),
    }

    battery = psutil.sensors_battery()
    if battery:
        stats["battery"] = f"{battery.percent}% {'(Charging)' if battery.power_plugged else '(Not Charging)'}"
    else:
        stats["battery"] = "N/A"

    return stats
