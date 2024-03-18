import os
import shutil
import sys

def copy_gitignore_to_project(project_path):
    # Check if the .gitignore file exists in the current directory
    gitignore_path = os.path.join(os.getcwd(), '.gitignore')
    if not os.path.isfile(gitignore_path):
        print("No .gitignore file found in the current directory to copy. Exiting...")
        sys.exit()

    # Ask the user whether to copy .gitignore to the given project path
    confirmation = input(f"Do you want to copy .gitignore to the directory {project_path}? [y/N] ")
    if confirmation == 'y':
        dest_gitignore = os.path.join(project_path, '.gitignore')
        try:
            shutil.copyfile(gitignore_path, dest_gitignore)
            print(f".gitignore has been successfully copied to {dest_gitignore}")
        except Exception as e:
            print(f"An error occurred while copying the file: {e}")
    else:
        print("Copy operation cancelled. Exiting...")
        sys.exit()

if __name__ == "__main__":
    # Check for argument presence
    if len(sys.argv) < 2:
        print("No path argument provided. Please provide the path as the first argument. Exiting...")
        sys.exit()
        
    # Store the project path from the first argument
    project_path = sys.argv[1]
    # Check if the project path exists
    if not os.path.exists(project_path):
        print("The specified path does not exist. Exiting...")
        sys.exit()

    # Function to handle the .gitignore copy logic
    copy_gitignore_to_project(project_path)
