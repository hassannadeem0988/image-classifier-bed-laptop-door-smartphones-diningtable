#Base image
FROM python:3.10
#Set work dir
WORKDIR /app
#Copy requirements
COPY requirements.txt .
#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
#Copy the rest of the project
COPY . .
#Expose port
EXPOSE 5000
#Run command
CMD ["uvicorn", "api.FastApi:app", "--host", "0.0.0.0", "--port", "5000"]
