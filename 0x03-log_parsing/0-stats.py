#!/usr/bin/python3
"""processing logs"""

import sys
import signal


if __name__ == '__main__':

    def print_stats():
        """printing the status codes and total file size"""
        print(f"Total file size: {total_file_size}")
        for code in sorted(get_status_code.keys()):
            if get_status_code[code] > 0:
                print(f"{code}: {get_status_code[code]}")

    def quit_ops(sig, frame):
        """handle signal interruption"""
        print_stats()
        sys.exit(0)

    signal.signal(signal.SIGINT, quit_ops)

    total_file_size = 0
    line_count = 0
    get_status_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0,
    }

    try:
        for line in sys.stdin:
            line_count += 1
            sp_log = line.split()
            if len(sp_log) < 7:
                continue
            try:
                status_code = int(sp_log[-2])
                file_size = int(sp_log[-1])
            except (ValueError, IndexError):
                continue
            if status_code in get_status_code:
                get_status_code[status_code] += 1
            total_file_size += file_size
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        # Print traceback information on keyboard interrupt
        print_stats()
        raise  # Re-raise the exception to print the traceback

    print_stats()
