from locust import HttpUser, task, between


class WebsiteUser(HttpUser):

    wait_time = between(1, 5)

    @task
    def home(self):
        self.client.get("/")

    @task
    def post(self):
        self.client.get("/posts")

    @task
    def albums(self):
        self.client.get("/albums")

    @task
    def photos(self):
        self.client.get(f"/albums/photos/1")
