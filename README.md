# Pricey

Pricey is a web application that uses web scraping to extract prices and details from top e-commerce platforms for users. Users can customize their shopping by setting price thresholds, and an email notification system alerts them when a selected product's price drops.

## Features

- Web scraping from top e-commerce platforms
- Customizable price thresholds
- Email notifications for price drops

## Technologies Used

- Python
- Django
- SQL

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip
- virtualenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/pricey.git
   cd pricey
   
2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  
   
3. **Install the dependencies:**

   ```bash 
   pip install -r requirements.txt

4. **Set up the .env file:**

   Create a .env file in the root directory of the project and add the following variables with your specific details:

   ```bash 
   SECRET_KEY=your_secret_key
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   DATABASE_HOST=your_database_host
   DATABASE_PORT=your_database_port
   EMAIL_HOST=your_email_host
   EMAIL_PORT=your_email_port
   EMAIL_HOST_USER=your_email_user
   EMAIL_HOST_PASSWORD=your_email_password
   
5. **Apply the migrations:**

   ```bash
   python manage.py migrate

6. **Create a superuser (optional, for accessing the Django admin interface):**

   ```bash
   python manage.py createsuperuser

7. **Run the development server:**

   ```bash
   python manage.py runserver

8. **Access the application:**
Open your web browser and go to http://127.0.0.1:8000/ to view the application.

## Usage

1.	Register an account or log in if you already have one.
2.	Add the URLs of the products you want to track.
3.	Set your desired price thresholds for the products.
4.	Wait for email notifications when the prices drop below your thresholds.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

1.	Fork the repository
2.	Create your feature branch (git checkout -b feature/your-feature)
3.	Commit your changes (git commit -am 'Add some feature')
4.	Push to the branch (git push origin feature/your-feature)
5.	Create a new Pull Request
	
## License   

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE file for details.
