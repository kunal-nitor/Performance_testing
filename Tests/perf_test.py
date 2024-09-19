from locust import User, HttpUser, task, constant


class WebsiteUser(HttpUser):

    wait_time = constant(1)
    host = "https://reqres.in"

    @task
    def get_request_users_list(self):
        get_users_list_req =  self.client.get(url='/api/users?page=2')
        print(f"status code: {get_users_list_req.status_code}")
        print(f"response : {get_users_list_req.text}")

    @task
    def get_single_user(self):
        get_single_user_req = self.client.get(url='/api/users/2')
        print(f"status code : {get_single_user_req.status_code}")
        print(f"response : {get_single_user_req.text}")

    @task
    def create_user(self):
        create_user_req = self.client.post(url='/api/users',
                         data=
                         """{
                                "name": "morpheus",
                                "job": "leader"
                         }""")
        print(f"response : {create_user_req.text}")
        print(f"status code: {create_user_req.status_code}")
