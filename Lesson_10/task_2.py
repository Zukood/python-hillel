import datetime


def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        current_time = datetime.datetime.now()
        log_message = f"Function launched at {current_time} with result {result}\n"

        with open("log.txt", "a") as log_file:
            log_file.write(log_message)

        return result

    return wrapper

@log_result
def sum_args(*args):
    result = sum(args)
    return result

sum_args(1, 2, 3)
