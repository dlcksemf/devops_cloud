from datetime import datetime

def check_available(received_text: str) -> bool:
    return received_text.startswith("남은 시간")

def make_response() -> str:
    futuredate = datetime.strptime('DEC 31 2021  23:59', '%b %d %Y %H:%M')
    nowdate = datetime.now()
    count = int((futuredate - nowdate).total_seconds())

    days = count // 86400
    hours = (count - days * 86400) // 3600
    mins = (count - days * 86400 - hours * 3600) // 60
    secs = count - days * 86400 - hours * 3600 - mins * 60
    response_text = str(days) + "days " + str(hours) + "hours " + str(mins) + "minutes " + str(secs) + "seconds left in 2021"

    return response_text
