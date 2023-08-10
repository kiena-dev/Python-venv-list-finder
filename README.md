# Python-venv-list-finder
This tool helps you list and find virtual environments (venv) created within your Python projects. It scans your specified directory and identifies folders containing pyvenv.cfg files, providing you with a convenient list of venvs along with activation commands.

## Prerequisites
* Python3.xx
* Linux OS (tested using Debian 12)
  
## Usage
* Clone the repository to your local machine.
* Navigate to the repository directory.
```
$ git clone https://github.com/kiena-dev/Python-venv-list-finder.git
$ cd Python-venv-list-finder
```
* Run the script:
```
$ python3 find_python_env.py
```
* Enter the folder path you want to search for venvs. Press Enter to use the current directory as the default.
* he script will display a list of venvs along with activation commands.

## Example Output
![Overview](/images/python_env_list.png)

## Inspiration
* [Stackoverflow](https://stackoverflow.com/questions/60873454/how-can-i-list-all-the-virtual-environments-created-with-venv)
