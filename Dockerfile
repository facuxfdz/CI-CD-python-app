FROM python:slim

WORKDIR /python-app

ADD . /python-app/

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME world

# Run app.py when the container launches
CMD [ "python", "app.py" ]