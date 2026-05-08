ERROR_MESSAGE_MAP = {
    "not available": "invalid_email",
    "Please enter password": "empty_password",
    "Please enter Email": "empty_email",
    "incorrect": "invalid_credentials" # Certified fail case
}

def parse_error_message(text):
    if not text:
        return "unknown_error"

    text = text.lower().strip().replace(".", "")

    for keyword, reason in ERROR_MESSAGE_MAP.items():
        keyword = keyword.lower().strip()

        if keyword in text:
            print(f"MATCH: {reason}")
            return reason

    print("NO MATCH")
    return "unknown_error"