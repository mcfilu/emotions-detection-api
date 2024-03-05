# 
FROM python:3.10

# 
WORKDIR /face-detection-blur-api

# 
COPY ./requirements.txt /face-detection-blur-api/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /face-detection-blur-api/requirements.txt

# 
COPY ./app /face-detection-blur-apip/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]