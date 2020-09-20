method_response = {'method': 'auth.check', 'code_response': 200}


def decorator_function(method):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            print(*args, **kwargs)
            print('Выполняем обёрнутую функцию...')
            func(*args, **kwargs)
            print('Выходим из обёртки')

        return wrapper
    if method == method_response['method']:
        print(f'ок: this method  is {method}')
        return actual_decorator
    else:
        print("Неправильный метод")


class Decorator_class:
    def __init__(self, func):
        print(type(func))
        self.func = func

    def check(self, method, func):
        print(f'ок: this method  is {method}')
        if method == method_response['method']:
            return func
        else:
            return 'Неправильный метод'


s = Decorator_class

# @s.check(method='auth.check')
@decorator_function(method='auth.chec')
def main(request):
    txt = "Отлично, доступ получен"
    print(f'{txt}: {request}')


if __name__ == '__main__':
    main('25658545')

########################################

# def decorator_function(func):
#     def wrapper():
#         print('Функция-обёртка!')
#         print('Оборачиваемая функция: {}'.format(func))
#         print('Выполняем обёрнутую функцию...')
#         func()
#         print('Выходим из обёртки')
#
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')
#
