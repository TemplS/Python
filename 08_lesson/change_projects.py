import requests


class Change_Project:

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url

    def test_positive_change_project(self, title, project_id, body=None):
        my_headers = {'Authorization': f'Bearer {self.key}'}
        body = {
            "title": f"{title}"
        }
        req = requests.put(self.base_url+f'/{project_id}', headers=my_headers, json=body)
        assert req.status_code == 200

    def test_negative_change_project(self, title):
        my_headers = {'Authorization': f'Bearer {self.key}'}
        body = {
            "title": f"{title}"
        }
        req = requests.put(self.base_url, headers=my_headers, json=body)
        assert req.status_code == 404
