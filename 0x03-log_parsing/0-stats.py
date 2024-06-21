#!/usr/bin/python3
import sys
import signal


total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the collected statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def process_line(line):
    """Processes a line and updates statistics."""
    global total_size
    try:
        parts = line.split()
        if len(parts) != 7:
            return


        ip_address, dash, date, request, http_version, status_code, file_size = parts
        status_code = int(status_code)
        file_size = int(file_size)


        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        total_size += file_size


    except ValueError:
        # If convertion fails or line is in wrong format, skip the line
        return


def handle_interrupt(signal, frame):
    """Handles a keyboard interrupt (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)


try:
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except EOFError:
    # Handle end of file (EOF) gracefully
    pass
finally:
    print_stats()

