FROM python:3.10-slim

# Set working dir
WORKDIR /app

# Copy source code and data to app directory
COPY src /app
COPY data /app/data
COPY requirements.txt /app

# Install packages
RUN apt-get update 
RUN apt-get -y install build-essential && apt-get autoremove -y
RUN pip3 install -r /app/requirements.txt

# Run Streamlit
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
