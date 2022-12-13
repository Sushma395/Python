import requests

def test_api_get():
    resp = requests.get("https://reqres.in/api/users?page=2")
    print(resp.status_code)
    assert (resp.status_code == 200), "Status code is not 200. Rather found : " + str(resp.status_code)
    for record in resp.json()['data']:
        if record['id'] == 7:
            assert record['first_name'] == "Michael", \
                "Data not matched! Expected : Michael, but found : " + str(record['first_name'])
            assert record['last_name'] == "Lawson", \
                "Data not matched! Expected : Lawson, but found : " + str(record['last_name'])

def test_api_post():
    data = {'name': 'Johnny',
            'job': 'QA_Automation'}
    resp = requests.post(url="https://reqres.in/api/users", data=data)
    print(resp.status_code)
    data = resp.json()
    assert (resp.status_code == 201), "Status code is not 201. Rather found : "\
        + str(resp.status_code)
    assert data['name'] == "Johnny", "User created with wrong name. \
        Expected : Johnny, but found : " + str(data['name'])
    assert data['job'] == "QA_Automation", "User created with wrong job. \
        Expected : QA_Automation, but found : " + str(data['name'])
    print(resp.content)

