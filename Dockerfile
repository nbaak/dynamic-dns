# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./src /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir dnslib aiohttp flask

# Make port 5000 available to the world outside this container
EXPOSE 5000
# Expose DNS port 53
EXPOSE 5300/udp

# Run app.py when the container launches
CMD ["python", "dnsserver.py"]
