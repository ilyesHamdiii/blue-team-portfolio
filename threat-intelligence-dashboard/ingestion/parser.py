def normalize_event(event):
    return {
        "timestamp": event.get("timestamp"),
        "ip": event.get("ip"),
        "username": event.get("username"),
        "command": event.get("command"),
        "event_type": event.get("event_type"),
        "success": bool(event.get("success"))
    }


def normalize_batch(events):
    return [normalize_event(e) for e in events]