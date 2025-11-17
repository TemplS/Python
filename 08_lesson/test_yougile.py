import requests
from create_projects import Create_Project
from change_projects import Change_Project
from get_project import Get_project


base_url = "https://ru.yougile.com/api-v2/projects"
key =
worker_id =

def test_yougile():
    create = Create_Project(key,base_url)
    create.test_positive_create_project("GosUslugi", worker_id, "admin")
    create.test_negative_create_project("Mistake", worker_id, "worker")

    change = Change_Project(key, base_url)
    project_id = create.test_positive_create_project("GosUslugi", worker_id, "admin")
    change.test_positive_change_project("Ловушка", project_id)
    change.test_negative_change_project("Ошибка 404")

    get = Get_project(key, base_url)
    project_id = create.test_positive_create_project("Печенька", worker_id, "admin")
    get.test_positive_get_project(project_id)
    get.test_negative_get_project(project_id)

def test_get_list_of_projects():
    my_headers = {'Authorization': f'Bearer {key}'}
    req = requests.get(base_url, headers=my_headers)
    print(req.json())

