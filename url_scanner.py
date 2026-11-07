import requests
import tldextract

def is_phishing_url(url):
    try:
        # Extract domain information
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"

        # Simple heuristic: suspicious keywords in the domain
        suspicious_keywords = ["login", "secure", "update", "bank", "verify", "account"]
        if any(keyword in domain.lower() for keyword in suspicious_keywords):
            return True

        # Check if URL responds correctly
        response = requests.head(url, timeout=5)
        if response.status_code >= 400:
            return True  # Possible phishing if URL gives errors
    except Exception as e:
        return True  # Consider unknown errors as phishing

    return False

# Example usage
if __name__ == "__main__":
    test_urls = [
        "https://secure-login.bankofxyz.com",
        "https://www.google.com",
        "http://update-your-details.xyz",
        "http://com-sa.pm?"
    ]

    for url in test_urls:
        result = is_phishing_url(url)
        print(f"URL: {url} - {'Phishing' if result else 'Legitimate'}")
