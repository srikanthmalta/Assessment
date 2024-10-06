FROM python:alpine3.20

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements file to the working directory
COPY requirements.txt /app/requirements.txt

# Step 4: Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . /app

# Step 6: Expose the port Flask will run on
EXPOSE 5000

# Step 7: Set the environment variables using .env file
COPY .env /app/.env

# Step 8: Set the command to run the Flask app
CMD ["python", "app.py"]