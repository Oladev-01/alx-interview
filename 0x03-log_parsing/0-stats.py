#!/usr/bin/python3
"""log parsing"""
from signal import signal, SIGINT
import re
import sys

if __name__ == '__main__':
    log_pattern = re.compile(
        r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - "
        r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "
        r"\"(GET|POST|PUT|DELETE|PATCH) (/[\w/]+) HTTP/1\.1\" "
        r"(\d{3}) "
        r"(\d+)$"
    )

    line_count = 0
    file_size = 0
    stats_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }

    def print_logs():
        """print log to output"""
        print(f'File size: {file_size}')
        for code in stats_code:
            if stats_code[code] > 0:
                print(f"{code}: {stats_code[code]}")

    def handle_interupt(signal, frame):
        """handle ctrl c"""
        print_logs()
        return
    signal(SIGINT, handle_interupt)

    with open(sys.stdin.fileno(), 'r') as f:
        for line in f:
            if not line:
                continue
            if not log_pattern.match(line):
                continue
            parts = line.split()
            file_size += int(parts[-1])
            line_count += 1
            status_code = int(parts[-2])
            stats_code[status_code] += 1
            if line_count % 10 == 0:
                print_logs()
