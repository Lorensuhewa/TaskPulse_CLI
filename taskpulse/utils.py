from datetime import datetime
from typing import Optional


def prompt_non_empty(prompt: str) -> str:
    """Prompt the user for input until a non-empty string is provided."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")

def prompt_priority(default: str = "Medium") -> str:
    valid = {"High", "Medium", "Low"}
    while True:
        value = input(f"Enter priority (High, Medium, Low) [{default}]: ").strip().capitalize()
        if not value:
            return default
        if value in valid:
            return value
        print("Invalid priority. Please enter High, Medium, or Low.")

def prompt_date(label: str, default: Optional[str] = None) -> str:
    prompt_str = f"{label} (YYYY-MM-DD)" + (f" [{default}]: " if default else ": ")
    while True:
        raw_val = input(prompt_str).strip()
        if not raw_val and default:
            return default
        try:
            parsed = datetime.strptime(raw_val, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            print("  [!] Invalid date format. Please use YYYY-MM-DD.")

def prompt_init(label: str) -> Optional[int]:
    raw_val = input(f"Enter {label}: ").strip()
    if raw_val.isdigit():
        return int(raw_val)
    return None

def truncate(text: str, max_length: int) -> str:
    """Truncate text to a maximum length, adding ellipsis if necessary."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."