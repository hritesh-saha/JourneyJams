FROM python:3.12-slim

# Update the package list and install Python 3.12 and pip prerequisites
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /JourneyJams

# Copy files into the container
COPY downloader.py . 
COPY requirements.txt .

# Install Python packages using pip
RUN pip install -r requirements.txt

# Default command to keep container running
CMD ["bash"]