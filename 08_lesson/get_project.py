import requests


class Get_project:

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url

    def test_positive_get_project(self, project_id):
        my_headers = {'Authorization': f'Bearer {self.key}'}
        req = requests.get(self.base_url + f'/{project_id}',
                           headers=my_headers)
        assert req.status_code == 200

    def test_negative_get_project(self, project_id):
        my_headers = {'Authorization': f'Bearer {self.key}'}
        req = requests.post(self.base_url + f'/{project_id}',
                            headers=my_headers)
        assert req.status_code == 404
