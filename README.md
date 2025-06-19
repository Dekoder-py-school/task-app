# To Do App

This project was made during the Summer of Making 2025

## Installation
1. Clone this repo to your machine or download the zip file using the green clone button.
2. Open the terminal / command prompt and navigate to the project folder.
3. Ensure python3 is installed on your machine & available on the path.
4. (OPTIONAL) Create a virtual environment with python3 -m venv venv, and activate it according to your OS
5. Install the required packages by running pip3 install -r requirements.txt


## Usage
To run with the default database, run:
```bash
python3 main.py
```
To run with a custom task list, run:
```bash
  python3 main.py --list <name_of_database> # or -l <name_of_database>
  # for example: python3 main.py --list work_project
```

## Help
To see the help menu, run:
```bash
  python3 main.py --help
```

## AI DISCLAIMER
AI (GitHub Copilot) was used to help write the readme, some commit messages, and the menu prompt. It also helped with some debugging and with the displaying of the checkboxes ( [ ] or [X])

The rest of the code was written by me, including the logic for adding, removing, and displaying tasks, as well as accessing the database.
