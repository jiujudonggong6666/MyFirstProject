FROM python
COPY . /home/lijunxing/my-project
RUN  pip install -r /home/lijunxing/my-project/requirements.txt
RUN  uwsgi --http :8001 --wsgi-file run.py
CMD ["python", "/home/lijunxing/my-project/MyprojectFlask.py"]
