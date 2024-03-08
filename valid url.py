def is_valid_url(url):

    pattern = r'^https?://[a-z0-9.-]+\.[a-z]{2,}/?$'
    return bool(re.match(pattern, url, re.IGNORECASE))

is_valid_url

