method_response = 'auth.check'
code_response = 200


class Service:
    def __init__(self, request):
        self.request = request

    def check(self, request):
        if request == '25658545':
            return "Авторизцая разрешена"


s = Service


@s.check
def main(request):
    txt = "Отлично, доступ получени"
    res = request
    print(f'{txt}: {res}')


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

