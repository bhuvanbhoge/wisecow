# Step 1: Use the official Python image as the base image
# FROM python:3.9-slim

FROM python:3.10

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file to the container
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code to the container
COPY . .

# Step 6: Expose the port the app will run on (usually 5000 or 8000 for Python web apps)
EXPOSE 5000

# Step 7: Specify the command to run the app
CMD ["python", "app.py"]
