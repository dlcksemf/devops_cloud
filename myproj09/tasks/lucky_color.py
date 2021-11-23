from random import sample

def check_available(received_text: str) -> bool:
    return received_text.startswith("행운의 색상")

def make_response() -> str:
    color_code = lucky_color()
    response_text = "Your lucky color is " + color_code
    return response_text

def lucky_color():
    rgb_int_list = sample(range(0,256), 3)
    rgb_str_list = [str(int) for int in rgb_int_list]
    rgb_str = ",".join(rgb_str_list)
    return rgb_str