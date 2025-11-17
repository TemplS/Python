import requests


class Create_Project:

    def __init__(self, key, base_url):
        self.key = key
        self.base_url = base_url

    def test_positive_create_project(self, title, personal_id, post):
        my_headers = {'Authorization': f'Bearer {self.key}'}
        body = {
            "title": f"{title}",
            "users": {
                f"{personal_id}": f"{post}"
            }
        }
        req = requests.post(self.base_url, headers=my_headers, json=body)
        assert req.status_code == 201
        project_id = req.json()["id"]
        return project_id

    def test_negative_create_project(self, title, personal_id, post):
        my_headers = {}
        body = {
            "title": f"{title}",
            "users": {
                f"{personal_id}": f"{post}"
            }
        }
        req = requests.post(self.base_url, headers=my_headers, json=body)
        assert req.status_code == 401