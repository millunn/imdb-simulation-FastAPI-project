# imdb simulation FastAPI project

FastAPI based movies&tv shows database application.

## Features

- Get titles
- Get actors and actresses by name, awards
- Get tv shows and movies by genre
- Get top 5 movies by ratings and reviews
- Get episode information
- Get all reviews

and many more features, have a look at it!

## Installation

### Create virtual environment
#### PyCharm
```bash
venv ./venv
```
#### Windows
Open Command Prompt or PowerShell, navigate to project folder and run
```bash
python -m venv ./venv
```
#### Linux/MacOS
Open terminal, navigate to project directory and run
```bash
python -m venv ./venv
```
In case that previous command didn't work, install virtualenv
```bash
pip install virtualenv
```
Run command in project directory to create virtual env
```bash
virtualenv venv
```
### Activate Virtual environment
Open terminal and navigate to project directory, than run

| Platform | Shell      | Command to activate virtual environment |
|----------|------------|-----------------------------------------|
| POSIX    | bash/zsh   | $ source venv/bin/activate              |
|          | fish       | $ source venv/bin/activate.fish         |
|          | csh/tcsh   | $ source venv/bin/activate.csh          |
|          | PowerShell | $ venv/bin/Activate.ps1                 |
| Windows  | cmd.exe    | C:\> venv\Scripts\activate.bat          |
|          | PowerShell | PS C:\> venv\Scripts\Activate.ps1       |

### Dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt
```
### Database
Start MySQL server and execute all commands in **_init_db/init_db.sql_**

### Environment variables
Create new file **_.env_**

## Run server
From terminal
```bash
python -m uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```
From PyCharm
```bash
uvicorn app.main:app --reload --reload-delay 5 --host localhost --port 8000
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)
