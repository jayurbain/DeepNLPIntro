# Use an official Python runtime as a parent image
FROM tensorflow/tensorflow

LABEL maintainer="Jay Urbain <jayurbain@gmail.com>"

# Set the working directory to /app
WORKDIR /notebooks

# Copy the current directory contents into the container at /app
ADD . /notebooks

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
        graphviz 

# Make port 80 available to the world outside this container
EXPOSE 8888
EXPOSE 6006

CMD ["/run_jupyter.sh", "--allow-root"]
