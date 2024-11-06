# Use Python as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files to the container
COPY index.html app.py /app/

# Install Flask and MySQL connector
RUN pip install flask mysql-connector-python

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
