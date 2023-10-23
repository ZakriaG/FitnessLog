# FitnessLog

A Django web application designed to log and track workout progress. 
It is specifically tailored for a 5-day workout plan and provides detailed 
descriptions of each exercise. In the near future a performance dashboard will be 
used to monitor progress over time, an AI-based reps counter through webcam, 
and the ability to transfer activity data from other fitness devices.

## Features

- **Workout Logging**: Log your workout sets, including the exercise, weight lifted,
  number of reps, and additional notes.

- **5-Day Workout Plan**: The app comes with a pre-defined 5-day workout plan that you can 
  follow as is or customize to meet your specific fitness goals.

- **Performance Tracking (Coming Soon)**: Track progress over time in upcoming performance
  dashboard. Visualizing improvements and set new fitness goals.

- **AI Reps Counter (Coming Soon)**: Using AI to count reps through webcam.

- **Fitness Device Integration (Coming Soon)**: Seamlessly transfer activity data from 
  other fitness devices to the FitnessLog web-app, making it a central hub for all fitness data.

## Getting Started

To get started with the FitnessLog web-app, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/ZakriaG/FitnessLog.git
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate your project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**: Install the required packages from the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**: Apply the database migrations to set up the database.

   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**: Start the Django development server.

   ```bash
   python manage.py runserver
   ```

7. **Access the App**: Open your web browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 
   to access the FitnessLog web app.