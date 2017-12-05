from dulwich.repo import Repo
from dulwich import porcelain
from contextlib import redirect_stdout
from io import StringIO


def import_commits_as_string(file_path):

    # Constants
    NEW_OUTSTREAM = StringIO()

    commit_str = ""

    # Opens repo at this file
    path = file_path

    # sets repo to open from file_path
    repo = Repo(file_path)

    # porcelain handles the reading of the file at file_path
    print("Reading commit for: " + file_path + "\n\n")

    # Porcelain automatically writes to the terminal, to override this we must
    # redirect the stdout with our new outstream saved in NEW_OUTSTREAM.  
    # This allows us to save the log as a string so we can manipulate it.

    with redirect_stdout(NEW_OUTSTREAM):
        porcelain.log(repo)
		
    commit_str = NEW_OUTSTREAM.getvalue()
    return commit_str