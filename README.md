# Sports Event Utils

A utility library for sports event management applications.

## Installation

```bash
pip install sports-event-utils
```

## Usage

```python
from sports_event_utils import generate_secret_hash, validate_event_data
```

Generate Cognito secret hash
```python
secret_hash = generate_secret_hash(username, client_id, client_secret)
```

Validate event data
```python
event_data = {
    "title": "Summer Sports Meet",
    "description": "Annual sports meeting",
    "date": "2024-06-15T10:00:00",
    "location": "Sports Complex",
    "max_participants": 100
}
is_valid, error = validate_event_data(event_data)
```


## License

MIT License