FROM python
WORKDIR /code/
COPY ./app /code/app
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["uvicorn", "app.main:app","--reload"]


