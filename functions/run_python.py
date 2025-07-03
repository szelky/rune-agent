import os
import subprocess

def run_python_file(working_directory, file_path):
    absolute_working_directory = os.path.abspath(working_directory)
    absolute_file_path = os.path.abspath(os.path.join(absolute_working_directory, file_path))

    if not absolute_file_path.startswith(absolute_working_directory + os.sep):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python3', absolute_file_path], cwd=absolute_working_directory, timeout=30, capture_output=True, text=True)
        output_parts = []
        # Check for stdout
        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout}")
        # Check for stderr
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr}")
        # Check for return code
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        # Check for any output
        if output_parts:
            return "\n".join(output_parts)
        else:
            return "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"