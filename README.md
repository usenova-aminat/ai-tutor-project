\# AI Tutor Telegram Bot



Educational backend project: a Telegram bot with persistent user data stored in PostgreSQL.



This project was developed as part of an academic assignment to demonstrate:

\- interaction with the Telegram Bot API

\- asynchronous Python backend development

\- database integration using PostgreSQL

\- basic backend architecture and project structure

\- usage of Git and GitHub

\- secure configuration management using environment variables



---



\## ✅ Current Features



\- user registration via the `/start` command

\- storing Telegram user ID, username, and level in the database

\- automatic database table creation on startup

\- asynchronous database access using SQLAlchemy

\- isolated virtual environment (`venv`)

\- secure handling of secrets using `.env` file



---



\## 🛠️ Technology Stack



\- Python 3.11

\- aiogram 3.x

\- PostgreSQL

\- SQLAlchemy (async)

\- asyncpg

\- python-dotenv

\- Git / GitHub



---



\## 📂 Project Structure



```text

ai\_tutor\_project/

├── server/

│   ├── main.py         # main bot entry point

│   ├── models\_db.py    # database models

│   ├── db\_test.py      # database connection test

│   ├── venv/           # virtual environment (not tracked by Git)

│   └── .env            # environment variables (not tracked by Git)

├── docs/

├── media/

├── models/

└── README.md



⚙️ Installation and Running



1\. Clone the repository

&nbsp;

git clone https://github.com/usenova-aminat/ai-tutor-project.git

cd ai-tutor-project



2\. Create and activate virtual environment



python -m venv venv

venv\\Scripts\\activate



3\. Install dependencies



pip install -r requirements.txt



4\. Create .env file inside server/ directory

env

BOT\_TOKEN=your\_telegram\_bot\_token

DATABASE\_URL=postgresql+asyncpg://user:password@localhost:5433/tutor\_db



5\. Run the bot



python server/main.py





🗄️ Database



PostgreSQL is used as the main database.

All required tables are created automatically when the bot starts.

