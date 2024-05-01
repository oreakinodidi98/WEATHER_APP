# python_OOP

## create a Virtual enviroment

- python -m venv venv
- activate the virtual enviroment: . .\venv\Scripts\Activate
- install dependencies
  - pip install django
  - pip install flake8
    - check code: flake8 crud_example.py

- Deactivate the virtual environment: venv\Scripts\deactivate.bat
- or : deactivate

## generating a requirements file

- Here's how you can create a requirements.txt
- activate virtual nviroment: . .\venv\Scripts\Activate
- run command: pip freeze > requirements.txt
  - This command creates a requirements.txt file containing the names and versions of all installed packages
  - to include only the packages needed for your project (excluding development dependencies), you can use the:
  - pip freeze --exclude-editable > requirements.txt
