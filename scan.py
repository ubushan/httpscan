import requests


sites = ['https://ya.ru', 'https://mail.ru', 'https://rambler.ru', 'https://q.qq', ';']


def get_code(address):
    try:
        response = requests.get(address)
        getcode = response.status_code
        return [address, getcode]
    except requests.exceptions.HTTPError as err:
        return [address, err.response.content]
    except requests.exceptions.ConnectTimeout:
        return [address, 'Connection timeout occured']
    except requests.exceptions.ConnectionError:
        return [address, 'Connection Error']
    except requests.exceptions.MissingSchema:
        return [address, 'Invalid URL']


for i in sites:
    print(get_code(i))