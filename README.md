# GatorGauge

A tool for Professors to use to download and analyze the information in student
repositories. This tool can be used to allow students to find when their peers
had issues or triumphs within projects.

## Config.ini

Default Variables. Do not place the variables inside of "".
Since the config.ini file contains sensitive information due to the token,
it is not supplied in this repository. Before running the program the user must
create a new file in their local root directory called config.ini

Paste the following into this new file:

```
[Token]
token =
; github access token keep secret!!!!

[Project]
project =
; project to pull

[Keywords]
keywords =
; keyword list, filters down repositories exclusively

[Out]
out = repos
; default: repos/
```

Once done, paste the token in Token section. Must specify a project but keywords
is optional, and out defaults to a directory named 'repos' which will be created
upon running the get command.

### Token

Github token allows the program to pull the repositories.

### Project

Name of the project to be pulled down.

### Keywords

Keywords used to filter for only repositories with the keywords in the name of
the repository.

### Out

Folder to place all of the downloaded repositories inside of. Defaults to
a directory named 'repos' which will be created upon running the get command.

## Execution

### Requirements

To get requirements, use the command:

```
pip3 install --user -r requirements.txt
```

### Execution

Type ```python3 gatorGauge.py``` into the terminal

### commands

Download the project(named in Config.ini or given with the config command).

```
get
```

Edit the values in the config file or temporarily change the config values.

```
config
```

List all repositories if no arguments are given or all files in a given repository.

```
list
```
```
list <repo name>
```

Perform sentiment analysis and gensim on the given target (source, comments, commits,
reflection).

```
analyze <target>
```

Quit the program.
```
quit
```
## Usage

GatorGage analyzes Computer Science 111 - Introduction to Computer Science I -
students' labs and practicals, gaining information on what was most difficult,
how long it took, and so on. Natural language processing is used in order to
create visual displays for professors and future students to gain information
on the work.

## Testing

### Functions Tested

### Running the Test Suite

To run the test suite, run the following commands in the rood directory of GatorGauge:

```
pytest tests
```

Or, depending on the operating system:

```
python3 -m pytest tests
```

### Automatic Linting

The linting automatically checks to ensure code is up to pep8 standards. If
linting errors occur, run the following command to perform automatic linting. If
there are errors that the tool cannot fix, the test suite will tell you where
and what the errors are so that you may go to the location and fix them.

```
autopep8 --in-place --aggressive *.py
```

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it can
evaluate the coverage of the test suite.

### Activating Travis-CI

Travis can only be implamented by admin accounts. Admin users can activate Travis
by creating a travis.yml in the project's root
directory.

## Questions or Comments

Any problems or suggestions regarding GatorGauge can be written in the issue
link at the top of the site.
