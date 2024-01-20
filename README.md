# Crypto Donation
## Project Description
I was  tasked with creating a web/mobile application that enables users to donate Cryptocurrency to
various charitable organisations around the world. To ensure transparency and trust, these transactions
will be recorded on a blockchain network.

## How to RUN
- Clone the repository: git clone [https://github.com/Churanta/Blockchain-based-Charity-Donation-Platform.git](https://github.com/eman3asem/donatecrypto.git)
- Open main.py
- Create a virtual network 'python -m venv venv'
- Install all dependencies using 'pip install -r requirements.txt'
- Install the database server 'pip install Flask SQLAlchemy'
- To run the server type './run.sh'
- Open http://localhost:5000 and display the webpage

## Application Architecture:
### Frontend:

The frontend is built using HTML, CSS, and JavaScript.
JavaScript libraries/frameworks such as Web3.js are used for interacting with the Ethereum blockchain.

### Backend:

The backend is powered by Flask, a lightweight Python web framework.
Flask is used for handling HTTP requests, rendering HTML templates, and interacting with a SQLite database.

### Database:

SQLite is used as the database for simplicity. It's a lightweight, serverless database that is easy to set up and suitable for small to medium-sized applications.
SQLAlchemy is used as an Object-Relational Mapping (ORM) tool to interact with the database.

## Technologies Used:
### Frontend:
- HTML, CSS
- JavaScript
- Web3.js for interacting with the Ethereum blockchain

### Backend:
- Flask (Python web framework)
- SQLAlchemy (Python SQL toolkit and ORM)
- SQLite (Database)

## Assumptions Made:
### Web3.js and Ethereum:

The application assumes the use of Web3.js for Ethereum integration, implying that users have a browser with Web3 support (e.g., with MetaMask extension).
Assumed familiarity with Ethereum and the ability to send transactions.
Wallet Connection:

Users are expected to have a crypto wallet (e.g., MetaMask) installed and connected to the application.

### Single Page Application (SPA):
The provided code suggests a Single Page Application (SPA) approach where interactions happen on a single HTML page, and JavaScript handles dynamic updates.

### Security:
Assumes basic security practices such as validating user inputs on the server side.
Assumes the use of MetaMask for secure wallet interactions.

## Decision-Making Process:
### Flask as the Backend:
- Flask was chosen as the backend framework for its simplicity and ease of use.
- Suitable for small to medium-sized applications, making it a good fit for a donation platform.

### SQLite as the Database:
- SQLite was chosen for its simplicity and ease of setup, suitable for a small-scale application.
- May be replaced with a more robust database (e.g., PostgreSQL) for scalability in larger deployments.

### Web3.js for Ethereum Interaction:
- Web3.js is commonly used for Ethereum integration in JavaScript applications.
- Assumes that users have Ethereum wallets with Web3 support (e.g., MetaMask).

### Fetch API for Data Transmission:
Utilizes the Fetch API for making asynchronous requests from the frontend to the backend, facilitating data transmission.

### Popup for Transaction Details:
A popup is used to display transaction details after a successful funds transfer, providing a clean user experience.

### Form Validation:
Assumes basic form validation on the client side to ensure required fields are filled before submitting the form.

### Error Handling:
Basic error handling is implemented to display error messages to users in case of issues during funds transfer or data saving.

### Separation of Concerns:
The code attempts to follow a separation of concerns by having clear functions for different responsibilities (e.g., transferFunds, closePopup, etc.).

### Event Listeners:
Event listeners are used to trigger functions based on user interactions, providing a responsive and interactive user interface.
