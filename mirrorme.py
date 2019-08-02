
#!pip install pywebcopy

from pywebcopy import save_website

print("Which website you want to mirror?:\n")
_url = input()

print("And where do you want to save it? Insert the path to the folder:\n")
_project_folder = input()

save_website(
	
	url = _url,
	
	project_folder = _project_folder
)

