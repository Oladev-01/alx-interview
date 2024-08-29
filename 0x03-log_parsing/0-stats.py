#!/usr/bin/env python3
"""log parsing"""
import sys
import signal

total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_statistics():
    """Prints the current statistics."""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C)"""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) < 7:
            continue
        
        try:
            ip = parts[0]
            date = parts[3][1:]
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        if status_code in status_code_count:
            status_code_count[status_code] += 1
        total_file_size += file_size

        if line_count % 10 == 0:
            print_statistics()

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
