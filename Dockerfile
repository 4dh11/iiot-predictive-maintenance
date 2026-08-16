# Step 1: Base Python Lightweight Image
FROM python:3.10-slim

# Step 2: Set working directory in container
WORKDIR /app

# Step 3: Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application code
COPY . .

# Step 5: Expose port 5000
EXPOSE 5000

# Step 6: Define execution command
CMD ["python", "app.py"]