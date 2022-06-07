import flask
from concurrent.futures import ProcessPoolExecutor, process
import json
import math

# 多进程池子,必须放在函数声名的最下面才能使用,还得放在main函数里面，不然会出现报错
# process_pool = ProcessPoolExecutor()
app = flask.Flask(__name__)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()
    app.run()
