# Django Band Website

Welcome to the Django Band Website! This is a Django-based web application that allows users to explore the band's music and upcoming events.

## Prerequisites

1. Git
2. Python 3.8 or higher
3. pip
4. Docker

## Installation

To install the application, follow these steps:

1. Clone the repository:

git clone https://github.com/YOUR_USERNAME/django-band-website.git

2. Create a virtual environment and activate it:

python3 -m venv venv

source venv/bin/activate (for Windows) **or** source ~/.bash_profile (for Linux and MacOS)

3. Install the dependencies:

pip install -r requirements.txt

## Using Docker

If you prefer to use Docker, you can also run the application using a pre-built image from Docker Hub.

1. Pull the image from Docker Hub:

docker pull YOUR_USERNAME/myband-django

2. Run the container:

docker run -p 8000:8000 YOUR_USERNAME/myband-django

3. Open your browser and navigate to http://localhost:8000 to access the application.

Note: Ensure that the container has the correct environment variables set and the correct ports exposed.

