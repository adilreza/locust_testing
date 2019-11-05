from locust import HttpLocust, TaskSet, task


def link_test(link):
    link.client.get("/dashboard/")

class WebsiteTasks(TaskSet):
    def on_start(self):
        link_test(self)

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
    host = 'http://34.223.233.165:8060'