# My Band

Welcome to the The Electric Serenades Website! This is a Django-based web application that allows users to explore the band's music and upcoming events.

## Prerequisites

- Git
- Python 3.8 or higher
- pip
- Docker

## Installation

To install the application, follow these steps:

1. Clone the repository:

    `git clone https://github.com/Kaaribu/my-band.git`

2. Create a virtual environment and activate it:

    - `python3 -m venv venv`
    - `source venv/bin/activate` *(for Windows)* **or** `source ~/.bash_profile` *(for Linux and MacOS)*

3. Install the dependencies:

    `pip install -r requirements.txt`

## Using Docker

If you prefer to use Docker, you can also run the application using a pre-built image from Docker Hub.

1. Pull the image from Docker Hub:

    `docker pull kaaribu/my-band`

2. Run the container:

    `docker run -p 8000:8000 kaaribu/my-band`

3. Open your browser and navigate to `http://localhost:8000` to access the application.

Note: Ensure that the container has the correct environment variables set and the correct ports exposed.

## Built With
- Python/Django 
- HTML 
- CSS

## Credits

- Author: Karabo Masalesa - [My Github link](https://github.com/Kaaribu)

## Repository

https://github.com/Kaaribu/my-band


