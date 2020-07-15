FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

# Install GDAL dependencies
RUN apt-get install -y libgdal-dev g++ --no-install-recommends && \
    apt-get clean -y



# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN cat /code/hosts >> /etc/hosts
EXPOSE 8000
CMD python /code/manage.py runserver 0.0.0.0:8000