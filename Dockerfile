FROM python:3.9.12
WORKDIR /app
# Install the application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY keras_model.h5 .
COPY labels.txt .
COPY main.py .
EXPOSE 5000
# ENTRYPOINT [ "main.py" ]
CMD [ "python","./main.py" ]