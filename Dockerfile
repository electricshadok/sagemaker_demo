# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the aws pipeline
COPY aws_pipeline /usr/src/app/aws_pipeline

# Copy the pipeline
COPY ml_pipeline /usr/src/app/ml_pipeline

# Set PYTHONPATH to include the directory where ai_pipe is located
ENV PYTHONPATH="${PYTHONPATH}:/usr/src/app/ai_pipe"

# Run preprocess.py when the container launches
#ENTRYPOINT ["python", "preprocess.py"]
