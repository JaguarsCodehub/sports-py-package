import hmac
import base64
import hashlib
from typing import Optional

def generate_secret_hash(username: str, client_id: str, client_secret: str) -> str:
    """
    Generate a secret hash for AWS Cognito authentication.
    
    Args:
        username: The user's username/email
        client_id: Cognito app client ID
        client_secret: Cognito app client secret
        
    Returns:
        str: The generated secret hash
    """
    msg = username + client_id
    dig = hmac.new(
        str(client_secret).encode('utf-8'),
        msg=msg.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

def validate_token_format(token: str) -> bool:
    """
    Basic validation of JWT token format.
    
    Args:
        token: JWT token string
        
    Returns:
        bool: True if token format is valid
    """
    try:
        parts = token.split('.')
        return len(parts) == 3 and all(
            bool(base64.b64decode(part + '=' * (-len(part) % 4)))
            for part in parts
        )
    except Exception:
        return False