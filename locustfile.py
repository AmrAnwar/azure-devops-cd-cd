from locust import HttpUser, task

class MLPredictUser(HttpUser):
    min_wait = 1000   
     
    @task
    def main_page(self):
        self.client.get("/")

    @task
    def predict(self):
        body = {
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":296.0
            },
            "PTRATIO":{
                "0":15.3
            },
            "B":{
                "0":396.9
            },
            "LSTAT":{
                "0":4.98
            }
        }
        self.client.post("/predict", body)