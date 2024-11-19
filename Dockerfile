# Use the official Apache Spark PySpark image as base
FROM apache/spark-py:v3.4.0

# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .

# Set root user
USER root

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat and curl
RUN apt-get update && \
    apt-get install -y netcat curl && \
    rm -rf /var/lib/apt/lists/*

# Copy the main python script
COPY demo.py .

# Copy the bloom filter pickle
COPY bloom_filter.pkl .

# Copy the start script into the container
COPY entrypoint.sh .

# Make sure it's executable
RUN chmod +x entrypoint.sh

# Run the start script
CMD ["/app/entrypoint.sh"]

