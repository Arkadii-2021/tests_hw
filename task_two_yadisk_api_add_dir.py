import requests
from pprint import pprint

ya_disk_token = ''


def get_upload_link(dir_name):
    url = "https://cloud-api.yandex.net/v1/disk/resources/"
    headers = {"Accept": "application/json",
               "Authorization": "OAuth " + ya_disk_token}
    params = {
        'path': dir_name
    }
    r = requests.put(url=url, params=params, headers=headers)
    r.raise_for_status()
    return r.status_code


def get_dir_info(dir_name):
    files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
            'Accept': 'application/json',
            'Authorization': 'OAuth {}'.format(ya_disk_token)
        }
    params = {
        'path': dir_name
    }
    response = requests.get(files_url, params=params, headers=headers)
    res = response.json()
    return res['path']


if __name__ == '__main__':
    print(get_upload_link('2021'))
    pprint(get_dir_info('2021'))
