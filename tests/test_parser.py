from unittest.mock import patch

from main import parse_email_to_event
from schemas import CalendarEvent


@patch("main.client.chat")
def test_parse_email_to_event_success(mock_chat):
    # Mocking a successful Ollama response
    mock_chat.return_value = {
        "message": {
            "content": '{"action_required": true, "event_title": "Marketing Kick-off", '
            '"date": "2026-06-25", "time": "14:00 PM", "location": "Google Meet", '
            '"participants": [{"name": "Sarah"}]}'
        }
    }

    result = parse_email_to_event("Meeting request...")
    assert isinstance(result, CalendarEvent)
    assert result.action_required is True
    assert result.event_title == "Marketing Kick-off"
    mock_chat.assert_called_once()
