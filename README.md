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
; Github access token, KEEP SECRET!!!!
TOKEN =
[Project]
; Project to pull
PROJECT =
[Prefix]
; Prefix to look for to narrow
PREFIX =
[Out]
; default: current directory
OUT = .
```

Once done, paste the token in token section. Must specify a project but PREFIX
is optional, and out defaults to current directory.

### Token

Github token allows the program to pull the repositories.

### Project

Name of the project to be pulled down.

### Prefix

Gets every repository in the project that starts with the prefix.

### Out

Folder to place all of the downloaded repositories inside of. Defaults to
current directory and names the repository the project name.

## Execution

### Requirements

To get requirements, use the command

```
pip3 install --user -r requirements.txt
```

### Basic Execution

Type ```python3 gator_gauge.py```, will cause errors if there are no values in
config.ini for Token and Project or if they are not supplied with the command
line arguments.

### Execution Flags

Download the project(named in Config.ini or supplied with the ```--project``` flag)

```
--get
```

List all files or files with the specified .extension

```
--list
```

Read the information in the inputed file name or files with the inputed .extension

```
--read
```

Project to download

```
--project
```

Prefix of the repository to download

```
--prefix
```

Token to allow for the program to download the repositories

```
--token
```

Location to place downloaded repositories

```
--out
```

## Usage

GatorGauge analyzes Computer Science 111 - Introduction to Computer Science I -
students' labs and practicals, gaining information on what was most difficult
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
