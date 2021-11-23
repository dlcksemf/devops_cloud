from random import randrange

def check_available(received_text: str) -> bool:
    return received_text.startswith("결정: ")

def make_response(received_text: str) -> str:
    options = received_text[4:].split(':')
    response_text = choose(options)

    return response_text

def choose(options: list) -> str:
    option_number = len(options)
    return options[randrange(0, option_number)]