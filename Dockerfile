#use the official python image as the baseimage
from python:3.8-slim

#set the working directory in the container
WORKDIR /numbers_strings

#copy the python file to container at /numbers_strings
COPY numbers_strings.py /numbers_strings

#run the python script when the container launches
ENTRYPOINT ["python", "numbers_strings.py"]
