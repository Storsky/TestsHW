import pytest
import requests
url = 'https://cloud-api.yandex.net/v1/disk'
ya_token = 'AQAAAAAd3W3qAADLW3FA3E4Lc0hkuYnPtSfuZ9s'
responses = ['<Response [201]>', '<Response [200]>']

headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(ya_token)
        }

class TestYandexAPI:
    def test_API_response(self):
        assert str(requests.get(url, headers=headers)) == responses[1]

    def test_make_folder(self):
        res = str(requests.put(url = url + '/resources?path=new_folder', headers = headers))
        if res not in responses:
            raise AssertionError(f'Ошибка доступа {res}')
        else:
            assert res == responses[0]