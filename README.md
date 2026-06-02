# Mini Project Collection

A collection of small projects and learning notes created while learning programming fundamentals, PostgreSQL, GUI development, APIs, automation, data visualization and application structure.

## 🚀 Table of Contents
  - [🐍 Python - Mini Projects](#-python---mini-projects)
    - [🖥️ Console Applications](#️-console-applications)
    - [🪟 Desktop GUI Applications](#-desktop-gui-applications)
    - [📊 Data Visualization](#-data-visualization)
    - [🌐 Web Automation](#-web-automation)
    - [🎮 Games](#-games)
  - [📝 Python - Notes](#-python---notes)
    - [🗄️ SQLAlchemy ORM](#️-sqlalchemy-orm)
  - [🐘 PostgreSQL - Notes](#-postgresql---notes)
  - [▶️ Running projects](#️-running-projects)
  - [⚙️ Installation](#️-installation)
      - [💻 Windows PowerShell](#-windows-powershell)

## 🐍 Python - Mini Projects

### 🖥️ Console Applications
|Project|Location|Technologies|Description|
|---|---|---|---|
|Sorting Algorithm|[folder](content/Python/mini-projects/console/01_sorting_algorithm)|`time`, `random`|A custom sorting algorithm created as an early programming experiment.|
|NBP Exchange Rates API|[folder](content/Python/mini-projects/console/02_currencies_nbp_api)|`requests`, NBP API|Fetches currency exchange rates from the Polish NBP API and prints them in the terminal.|
|Shopping Cart|[folder](content/Python/mini-projects/console/03_shopping_cart)|`random`|A simple shopping cart model with products, product subclasses and cart value calculation.|
|**Quiz** ⭐|[folder](content/Python/mini-projects/console/04_quiz)|`requests`, `html`, `random`, Open Trivia DB API|Downloads quiz questions from an external API, displays them in the terminal and calculates the score. This app later evolved into a larger project: [Quiz App](https://github.com/Glover012/quiz-app).|
|**Multi-threaded Website Availability Checker** ⭐|[folder](content/Python/mini-projects/console/05_multi_thread_website_availability_checker)|`requests`, `validators`, `threading`|Checks multiple websites using worker threads and saves a status report.|
|Website Downloader|[folder](content/Python/mini-projects/console/06_website_downloader)|`requests`, `validators`, `urllib.parse`|Downloads the HTML content of a given website and saves it to a local file.|

### 🪟 Desktop GUI Applications
|Project|Interface|Location|Technologies|Description|
|---|---|---|---|---|
|Calculator|PySide6|[folder](content/Python/mini-projects/pyside6_gui/01_calculator)|`PySide6`|A desktop calculator built with PySide6, using button input and keyboard shortcuts.|
|Calendar|PySide6|[folder](content/Python/mini-projects/pyside6_gui/02_calendar)|`PySide6`|A simple calendar app with month navigation and highlighted current day.|
|Simple Text Editor|PySide6|[folder](content/Python/mini-projects/pyside6_gui/03_simple_text_editor)|`PySide6`, file dialogs|A basic desktop text editor with open and save functionality.|
|Calculator|Tkinter|[folder](content/Python/mini-projects/tkinter_gui/01_calculator)|`tkinter`|A simple calculator built with Tkinter.|
|Currency Converter|Tkinter|[folder](content/Python/mini-projects/tkinter_gui/02_currency_converter_nbp_api)|`tkinter`, `requests`, NBP API|A Tkinter app that converts PLN values using exchange rates from the NBP API.|
|**Website Checker** ⭐|Tkinter|[folder](content/Python/mini-projects/tkinter_gui/03_website_checker)|`tkinter`, `requests`, `threading`|A Tkinter app that periodically checks website availability and updates the interface.|
|**To-Do App** ⭐|Tkinter|[folder](content/Python/mini-projects/tkinter_gui/04_to_do_app)|`tkinter`, `psycopg2`, PostgreSQL|A to-do application backed by a local PostgreSQL database.|
|Stock Info|Tkinter|[folder](content/Python/mini-projects/tkinter_gui/05_stock_info_yfinance)|`tkinter`, `yfinance`|An app that fetches and displays stock information and recent price history.|
|**Random Quote** ⭐|Tkinter|[folder](content/Python/mini-projects/tkinter_gui/06_random_quote)|`tkinter`, `SQLAlchemy`, PostgreSQL|A small Tkinter app that stores quotes in a PostgreSQL database and displays a random quote.|

### 📊 Data Visualization
|Project|Interface|Location|Technologies|Description|
|---|---|---|---|---|
|**Stock Info Chart** ⭐|Plotly chart|[folder](content/Python/mini-projects/data_visualization/01_stock_info_yfinance_plotly)|`yfinance`, `plotly`|Downloads historical stock data and displays it as a candlestick chart.|

### 🌐 Web Automation
|Project|Interface|Location|Technologies|Description|
|---|---|---|---|---|
|**Full Page Screenshot Downloader** ⭐|Headless browser|[folder](content/Python/mini-projects/web_automation/01_full_page_screenshot_downloader)|`selenium`, `webdriver-manager`, Chrome WebDriver|Uses Selenium to open a webpage, interact with it and save screenshots including a full-page capture.|

### 🎮 Games
|Project|Interface|Location|Technologies|Description|
|---|---|---|---|---|
|Snake Game|Turtle GUI|[folder](content/Python/mini-projects/turtle/01_snake_game)|`turtle`, `random`, `time`|A simple Snake game built with Turtle graphics.|

## 📝 Python - Notes

### 🗄️ SQLAlchemy ORM
|Folder|Location|Operation type|Description|
|---|---|---|---|
|Setup|[folder](content/Python/notes/sqlalchemy_orm/01_setup)|SQLAlchemy setup|Basic SQLAlchemy configuration with PostgreSQL connection, engine creation, declarative base and a simple table model.|
|CRUD operations|[folder](content/Python/notes/sqlalchemy_orm/02_crud_operations)|CRUD|Examples of creating, reading, updating and deleting records with SQLAlchemy sessions.|
|Data validation|[folder](content/Python/notes/sqlalchemy_orm/03_data_validation)|validation|Examples of validating model fields before saving records to the database.|
|Relationships|[folder](content/Python/notes/sqlalchemy_orm/04_relationships)|relationships|Examples of one-to-one, one-to-many and many-to-many relationships between ORM models.|

## 🐘 PostgreSQL - Notes
|Folder|Location|SQL|Description|
|---|---|---|---|
|Tables and Data Types|[folder](content/PostgreSQL/notes/01_tables_and_data_types)|`CREATE TABLE`, `ALTER TABLE`, `ALTER COLUMN`, `TRUNCATE`, `DROP TABLE`, `ENUM`|Snippets for creating and modifying tables and defining custom data types.|
|Basic Queries|[folder](content/PostgreSQL/notes/02_basic_queries)|`SELECT`, `DISTINCT`, `IS NULL`, `AS`, `CONCAT`|Basic query examples for selecting data, removing duplicates, handling null values and using aliases.|
|Filtering, Sorting and Limits|[folder](content/PostgreSQL/notes/03_filtering_sorting_limits)|`WHERE`, `ORDER BY`, `AND`, `OR`, `IN`, `LIKE`, `BETWEEN`, `LIMIT`, `OFFSET`, `FETCH`|Query filtering, sorting and pagination snippets using common SQL conditions and result-limiting clauses.|
|Data Modification|[folder](content/PostgreSQL/notes/04_data_modification)|`INSERT INTO`, `UPDATE`, `DELETE`, `RETURNING`|Examples of inserting, updating and deleting rows, including returning newly created record ids.|
|Aggregates and Grouping|[folder](content/PostgreSQL/notes/05_aggregates_and_grouping)|`COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, `GROUP BY`, `HAVING`, `UNION`, subqueries|Snippets for aggregate calculations, grouped results, combined queries and simple subqueries.|
|Joins|[folder](content/PostgreSQL/notes/06_joins)|`JOIN`, `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, `CROSS JOIN`|Examples of combining data from related tables using different join types.|
|Transactions|[folder](content/PostgreSQL/notes/07_transactions)|`BEGIN`, `COMMIT`, `ROLLBACK`|Transaction snippet showing how to group database operations and apply them safely.|
|Functions|[folder](content/PostgreSQL/notes/08_functions)|`CREATE FUNCTION`, `RETURNS`, `RETURNS TABLE`, `OUT`, `RETURN QUERY`, `RETURN NEXT`|Function examples covering parameters, return values, local variables and reusable database logic.|
|Control Flow|[folder](content/PostgreSQL/notes/09_control_flow)|`IF`, `ELSEIF`, `CASE`, `LOOP`, `FOREACH`, `CONTINUE`, `EXIT`, `RANDOM`|Control-flow examples for conditional logic, loops, arrays and random value handling.|
|Triggers|[folder](content/PostgreSQL/notes/10_triggers)|`CREATE TRIGGER`, `RETURNS TRIGGER`, `NEW`, `BEFORE INSERT`, `BEFORE UPDATE`|Trigger examples for automatically validating or updating rows during insert and update operations.|

## ▶️ Running projects
Most projects are standalone Python scripts. To run one of them, open its folder and execute the main script:

```powershell
cd content/Python/mini-projects/console/04_quiz
python quiz.py
```

For `PostgreSQL` projects, make sure you have a local PostgreSQL server running. pgAdmin can be useful for managing the database.

## ⚙️ Installation
Clone the repository and install the required dependencies in a virtual environment.

#### 💻 Windows PowerShell
```powershell
git clone https://github.com/Glover012/mini-project-collection.git
cd mini-project-collection
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
