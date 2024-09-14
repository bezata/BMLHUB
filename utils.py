import os

def get_api_key():
    """Retrieve the API key from an environment variable."""
    api_key = os.environ.get('BLOCKCHAINML_API_KEY')
    if not api_key:
        raise ValueError("BLOCKCHAINML_API_KEY environment variable not set")
    return api_key