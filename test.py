
# from django.core.serializers.json import DjangoJSONEncoder
# from django.http import HttpRequest, HttpResponse
# import json


# def main():
#     url = "https://slb.medv.ru/api/v2/"
#     headers = {'content-type': 'application/json'}
#
#     # Example echo method
#     payload = {
#         "method": "questions",
#         "params": {"page":1},
#         "jsonrpc": "2.0",
#         "id": 0,
#     }
#     response = requests.post(
#         url, data=json.dumps(payload), headers=headers).json()
#
#     print( response["result"] )
#
# if __name__ == "__main__":
#     main()
