def hms_to_seconds(t):
    parts = [int(i) for i in t.split(':')]
    if len(parts) == 3:
        h, m, s = parts
    elif len(parts) == 2:
        h = 0
        m, s = parts
    elif len(parts) == 1:
        h = 0
        m = 0
        s = parts[0]
    else:
        raise ValueError(f"Invalid time format '{t}', expected 'h:m:s', 'm:s', or 's'")
    return 3600 * h + 60 * m + s