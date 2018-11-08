FROM python
COPY . /home/lijunxing/my-project
RUN  pip install -r /home/lijunxing/my-project/requirements.txt
CMD ["python", "/home/lijunxing/my-project/MyprojectFlask.py"]
