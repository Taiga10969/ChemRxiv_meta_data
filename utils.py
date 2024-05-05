import os

def create_directory(save_pth):
    """
    Create a directory if it does not exist.

    Parameters:
    - save_pth (str): The path of the directory to be created.
    """
    if not os.path.exists(save_pth):
        os.makedirs(save_pth)
        print(f"Directory '{save_pth}' created successfully.")
    else:
        print(f"Directory '{save_pth}' already exists.")