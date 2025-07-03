import os

def get_files_info(working_directory, directory=None):
    # Get absolute path of the working directory and the target directory
    absolute_working_directory = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(absolute_working_directory, directory or ""))

    # Check if the target directory is within the working directory
    if not (target_dir == absolute_working_directory or target_dir.startswith(absolute_working_directory + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    # Check if the target directory exists and is a directory
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        directory_contents = sorted(os.listdir(target_dir))
        files_info = []
        for content in directory_contents:
            path = os.path.join(target_dir, content)
            file_size = os.path.getsize(path)
            is_dir = os.path.isdir(path)
            files_info.append(f"- {content}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"
