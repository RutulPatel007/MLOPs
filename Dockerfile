# Use an official base image with Python
FROM python:3.13-slim

# Set environment variables to prevent Python from writing bytecode and buffering
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose port for serving the model (if using Flask/FastAPI)
# EXPOSE 5000

# Command to run the application (modify as needed)
CMD ["python", "app.py"]