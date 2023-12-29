def url_filter(url, allowed_urls):
    if any(allowed_url in url for allowed_url in allowed_urls):
        # Allow the URL
        print(f"Allowed URL: {url}")
        return True
    else:
        # Drop or log the URL
        print(f"Blocked URL: {url}")
        return False

# Example usage
allowed_urls = ['http://example.com', 'https://trusteddomain.com']
url = 'http://example.com/path/to/resource'
url_filter(url, allowed_urls)
