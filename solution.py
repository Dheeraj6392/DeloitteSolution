from datetime import datetime
import time

def iso_to_unix_ms(iso_str):
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)
