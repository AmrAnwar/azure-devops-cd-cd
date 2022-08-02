git clone https://github.com/AmrAnwar/azure-devops-cd-cd
cd azure-devops-cd-cd
make install
az webapp up --name my-flask-ml-service-96 --resource-group Azuredevops --runtime "PYTHON:3.7"