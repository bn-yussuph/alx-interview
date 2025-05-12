#!/usr/bin/python3
"""log parsing
"""
import re
import sys


def print_stats(file_size: int, status_code: dict) -> None:
    """"
    helper function to print stats
    """
    print("File size: {}".format(file_size))
    sorted_codes = sorted(status_code.keys())
    for code in sorted_codes:
        if status_code[code] > 0:
            print("{}: {}".format(code, status_code[code]))

if __name__ == "__main__":
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')
    #line = '63.95.183.69 - [2025-05-08 21:13:41.922170] "GET /projects/260 HTTP/1.1" 401 871'

    code_freq = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0
    file_size_total = 0
    try:
        for line in sys.stdin:
            match = regex.match(line)
            if match:
                try:
                    line_count += 1
                    ln = line.split()
                    code = ln[-2]
                    size = int(ln[-1])
                    file_size_total += size
                    if code in code_freq.keys():
                        code_freq[code] += 1
                except Exception:
                    pass
                if line_count == 10:
                    print_stats(file_size_total, code_freq)
                    line_count = 0
        print_stats(file_size_total, code_freq)
    except KeyboardInterrupt:
        print_stats(file_size_total, code_freq)
        raise

