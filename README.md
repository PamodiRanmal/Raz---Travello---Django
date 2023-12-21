# Raz Travello Django

## Project Overview
Raz---Travello is a Django-based web application designed to showcase various travel destinations. The application allows users to view details about different destinations, including names, images, descriptions, prices, and special offers.

## Features
- Display of multiple travel destinations with engaging descriptions and images.
- Dynamic content management through Django's models and views.
- Intuitive and user-friendly interface.

## Installation and Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup Instructions

#### For Windows
1. **Clone the Repository**: Clone the project repository from GitHub to your local machine.
2. **Create a Virtual Environment**: Navigate to the cloned directory and create a virtual environment by running `python -m venv venv`.
3. **Activate Virtual Environment**: Activate the virtual environment by running `.\venv\Scripts\activate`.
4. **Install Dependencies**: Install the required dependencies by running `pip install -r requirements.txt`.

#### For macOS/Linux
1. **Clone the Repository**: Use the `git clone` command to clone the project repository.
2. **Create a Virtual Environment**: In the project directory, create a virtual environment using `python3 -m venv venv`.
3. **Activate Virtual Environment**: Activate it by running `source venv/bin/activate`.
4. **Install Dependencies**: Install necessary packages with `pip install -r requirements.txt`.

### Running the Application
After installation, run the Django server with `python manage.py runserver`. Navigate to `http://localhost:8000` in your web browser to view the application.

## Project Structure

### Views
The `views.py` file in the project contains the logic for rendering travel destinations. Each destination is created as an instance of the `Destination` model, with properties like `name`, `image`, `description`, `price`, and `offer`.

### Templates
HTML templates are used to render the information in a structured and styled format. The `index.html` file is the main template displaying the list of destinations.

### Models
Models are defined in the `models.py` file. Currently, the `Destination` model is used for managing travel destination data.

---
