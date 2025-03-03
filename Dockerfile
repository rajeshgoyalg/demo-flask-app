# Use Python 3.11 as base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 3000
EXPOSE 3000

# Run the Flask application
CMD ["python", "app.py"]
