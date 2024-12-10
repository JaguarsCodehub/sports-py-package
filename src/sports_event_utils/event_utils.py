from datetime import datetime
from typing import Dict, Any, Optional

def validate_event_data(event_data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
    """
    Validate event data before creation.
    
    Args:
        event_data: Dictionary containing event details
        
    Returns:
        tuple: (is_valid, error_message)
    """
    required_fields = ['title', 'description', 'date', 'location', 'max_participants']
    
    # Check required fields
    for field in required_fields:
        if field not in event_data:
            return False, f"Missing required field: {field}"
    
    # Validate date format
    try:
        if isinstance(event_data['date'], str):
            datetime.fromisoformat(event_data['date'])
    except ValueError:
        return False, "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"
    
    # Validate max_participants
    try:
        max_participants = int(event_data['max_participants'])
        if max_participants <= 0:
            return False, "max_participants must be greater than 0"
    except ValueError:
        return False, "max_participants must be a valid integer"
    
    return True, None

def format_event_response(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Format event data for API response.
    
    Args:
        event: Raw event data dictionary
        
    Returns:
        dict: Formatted event data
    """
    formatted = event.copy()
    
    # Ensure date is in ISO format
    if isinstance(formatted.get('date'), datetime):
        formatted['date'] = formatted['date'].isoformat()
    
    # Add registration status if participants exist
    if 'participants' in formatted:
        formatted['registered_count'] = len(formatted['participants'])
        formatted['available_spots'] = formatted['max_participants'] - formatted['registered_count']
    
    return formatted