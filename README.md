# SQLite Chat Assistant

## Overview
This project is a simple chat assistant that interacts with an SQLite database to process user queries and provide relevant responses. The assistant translates natural language queries into SQL queries and fetches data from an SQLite database.

## Features
- Accepts user queries in natural language.
- Converts queries into SQL commands.
- Fetches data from an SQLite database.
- Handles errors and invalid inputs gracefully.
- Web interface for easy interaction.

## Technologies Used
- Python
- Flask (Web Framework)
- SQLite (Database)
- HTML, CSS, JavaScript (Frontend)
- Railway (Deployment)

## Database Schema
The SQLite database consists of two tables:

### Employees Table
| ID | Name  | Department  | Salary | Hire_Date  |
|----|-------|------------|--------|------------|
| 1  | Alice | Sales      | 50000  | 2021-01-15 |
| 2  | Bob   | Engineering| 70000  | 2020-06-10 |
| 3  | Charlie | Marketing | 60000  | 2022-03-20 |

### Departments Table
| ID | Name        | Manager  |
|----|------------|---------|
| 1  | Sales      | Alice   |
| 2  | Engineering| Bob     |
| 3  | Marketing  | Charlie |

## Supported Queries
The assistant can respond to queries like:
- "Show me all employees in the [department] department."
- "Who is the manager of the [department] department?"
- "List all employees hired after [date]."
- "What is the total salary expense for the [department] department?"
- "Who was hired after [date]?"

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000/` in a browser.

## Deployment
The application is deployed on Railway. You can access the live version here:
[Live Deployment](https://web-production-32cc3.up.railway.app/)

## Known Limitations
- The assistant currently supports only a fixed set of query patterns.
- Error handling can be improved for more complex queries.
- The database schema is simple and can be extended with more details.

## Future Improvements
- Enhance natural language processing capabilities for more flexible queries.
- Improve UI/UX of the web interface.
- Add user authentication and session management.

## License
This project is licensed under the MIT License.

## Author
Santhosh D

