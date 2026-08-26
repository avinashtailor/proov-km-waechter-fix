# log_util.py
# Homemade logger for KM-Waechter.
# Written 2013. Style modernised 2025.

import time

LOG_LINES: list[str] = []               # module-level buffer; flushed by flush_log after each report


def log(message: str) -> None:
    """Append a timestamped line to the in-memory log buffer and print it."""
    stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    LOG_LINES.append(line)
    print(line)


def flush_log(path: str) -> None:
    """Write the buffered log lines to a file and clear the buffer."""
    with open(path, "a") as f:
        for line in LOG_LINES:
            f.write(line + "\n")
    LOG_LINES.clear()
