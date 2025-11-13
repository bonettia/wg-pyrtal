import urllib.parse

class APIError(Exception):
    def __init__(self, status, message):
        super().__init__(f"API Error {status}: {message}")

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0 : 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f} {power_labels[n]}"

def urlparse(url):
    return urllib.parse.quote_plus(url)