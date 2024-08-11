import redis
r_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)
#
#
# def factorial(num):
#     if r_cache.exists(num):
#         print(f'cache used for {num}')
#         return r_cache.get(num)
#     else:
#         print(f'calculating for {num}')
#     if num == 0:
#         return 1
#     else:
#         result = num * factorial(num - 1)
#         r_cache.set(num, result, ex=20)  # expiration
#         return result


def cache_deco(func):
    def wrapper(num, *args, **kwargs):
        if r_cache.exists(num):
            print(f'cache for {num} exists')
            return int(r_cache.get(num))

        print(f'calculating for {num}')
        result = func(num, *args, **kwargs)
        r_cache.set(num, result, ex=11)
        return result

    return wrapper


# @cache_deco
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)


@cache_deco
def fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == '__main__':
    # print(factorial(4))
    print(fibonacci(8))