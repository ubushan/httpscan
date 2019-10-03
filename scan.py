import requests
import csv

path_to_csv = 'sites.csv'
path_to_res = 'result.csv'


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


def get_list():
    with open(path_to_csv, 'r') as obj:
        data = csv.reader(obj, delimiter=',')
        for line in data:
            print(get_code(''.join(line)))


print(get_list())