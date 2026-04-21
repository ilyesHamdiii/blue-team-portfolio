import datetime

def _format_timestamp(ts):
    if not ts:
        return None, None
    try:
        # handle trailing Z (UTC) and offset-aware ISO strings
        if ts.endswith("Z"):
            dt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
        else:
            dt = datetime.datetime.fromisoformat(ts)
    except Exception:
        try:
            dt = datetime.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S")
        except Exception:
            return ts, ts  # return raw if parsing fails

    iso = dt.isoformat()
    # human readable, prefer explicit "UTC" when appropriate
    if dt.tzinfo is not None and dt.utcoffset() == datetime.timedelta(0):
        human = dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    else:
        human = dt.strftime("%Y-%m-%d %H:%M:%S")
    return iso, human

def normalize_event(event):
    ts_raw = event.get("timestamp")
    ts_iso, ts_human = _format_timestamp(ts_raw)

    command = event.get("command") or ""
    command_preview = command if len(command) <= 80 else command[:77] + "..."

    success_bool = bool(event.get("success"))
    status = "Success" if success_bool else "Failure"

    # Keep the original keys used by the DB (timestamp, ip, username, command, event_type, success)
    # and add readable/enriched fields to make each event easier to inspect.
    normalized = {
        "timestamp": ts_iso if ts_iso is not None else ts_raw,
        "timestamp_human": ts_human,
        "ip": event.get("ip") or "",
        "username": event.get("username") or "",
        "event_type": event.get("event_type") or "",
        "command": command,
        "command_preview": command_preview,
        "success": success_bool,
        "status": status,
        "summary": f"{ts_human or ts_raw} | {event.get('ip','-')} | {event.get('username','-')} | {status} | {command_preview}"
    }

    return normalized

def normalize_batch(events):
    return [normalize_event(e) for e in events]