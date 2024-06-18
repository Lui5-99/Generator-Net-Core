import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def select_path():
  path = filedialog.askdirectory()
  entry_path.delete(0, tk.END)
  entry_path.insert(0, path)

def generate_project(path, name_project):

  # name project to lower case
  name_project = name_project.lower()

  # if name project contains spaces, replace them with underscores
  name_project = name_project.replace(' ', '_')

  # if name is only one point (.), (-), (/), asign name to folder path
  if name_project in ['.', '-', '/']:
    name_project = os.path.basename(path)


  os.chdir(path)
  # Create the folder for the project  
  os.makedirs(name_project, exist_ok=True)
  os.chdir(name_project)

  # Create the command to generate the project
  command_create = f'dotnet new sln -n {name_project}' 
  # Create command for webapi
  command_webapi = f'dotnet new webapi -n {name_project}.WebApi'
  command_webapi_sln = f'dotnet sln {name_project}.sln add {name_project}.WebApi/{name_project}.WebApi.csproj'
  # Create domain layer
  command_domain = f'dotnet new classlib -n {name_project}.Domain' 
  command_domain_sln = f'dotnet sln {name_project}.sln add {name_project}.Domain/{name_project}.Domain.csproj' 
  # Create application layer
  command_application = f'dotnet new classlib -n {name_project}.Application'
  command_application_sln = f'dotnet sln {name_project}.sln add {name_project}.Application/{name_project}.Application.csproj'
  # Create Persistence layer
  command_persistence = f'dotnet new classlib -n {name_project}.Persistence'
  command_persistence_sln = f'dotnet sln {name_project}.sln add {name_project}.Persistence/{name_project}.Persistence.csproj'
  # Create reference between projects
  command_reference_domain_to_application = f"dotnet add {name_project}.Application/{name_project}.Application.csproj reference {name_project}.Domain/{name_project}.Domain.csproj"
  command_reference_persistence_to_application = f"dotnet add {name_project}.Application/{name_project}.Application.csproj reference {name_project}.Persistence/{name_project}.Persistence.csproj"
  command_reference_domain_to_persistence = f"dotnet add {name_project}.Persistence/{name_project}.Persistence.csproj reference {name_project}.Domain/{name_project}.Domain.csproj"
  command_reference_application_to_webapi = f"dotnet add {name_project}.WebApi/{name_project}.WebApi.csproj reference {name_project}.Application/{name_project}.Application.csproj"
  command_reference_persistence_to_webapi = f"dotnet add {name_project}.WebApi/{name_project}.WebApi.csproj reference {name_project}.Persistence/{name_project}.Persistence.csproj"
  # Install Packages
  # Entity Framework Core
  command_efcore_persistence = f"dotnet add {name_project}.Persistence/{name_project}.Persistence.csproj package Microsoft.EntityFrameworkCore"
  command_efcore_webapi = f"dotnet add {name_project}.WebApi/{name_project}.WebApi.csproj package Microsoft.EntityFrameworkCore"
  command_efcoretools_persistence = f"dotnet add {name_project}.Persistence/{name_project}.Persistence.csproj package Microsoft.EntityFrameworkCore.Tools"
  command_efcoretools_webapi = f"dotnet add {name_project}.WebApi/{name_project}.WebApi.csproj package Microsoft.EntityFrameworkCore.Tools"

  try:
    #Ejecutar commands
    # - Crear proyecto
    subprocess.run(command_create, shell=True, check=True)
    # - Crear webapi
    subprocess.run(command_webapi, shell=True, check=True)
    subprocess.run(command_webapi_sln, shell=True, check=True)
    # - Crear domain
    subprocess.run(command_domain, shell=True, check=True)
    subprocess.run(command_domain_sln, shell=True, check=True)
    # - Crear application
    subprocess.run(command_application, shell=True, check=True)
    subprocess.run(command_application_sln, shell=True, check=True)
    # - Crear persistence
    subprocess.run(command_persistence, shell=True, check=True)
    subprocess.run(command_persistence_sln, shell=True, check=True)
    # - Referencias
    subprocess.run(command_reference_domain_to_application, shell=True, check=True)
    subprocess.run(command_reference_persistence_to_application, shell=True, check=True)
    subprocess.run(command_reference_domain_to_persistence, shell=True, check=True)
    subprocess.run(command_reference_application_to_webapi, shell=True, check=True)
    subprocess.run(command_reference_persistence_to_webapi, shell=True, check=True)
    # - Instalar paquetes
    subprocess.run(command_efcore_persistence, shell=True, check=True)
    subprocess.run(command_efcore_webapi, shell=True, check=True)
    subprocess.run(command_efcoretools_persistence, shell=True, check=True)
    subprocess.run(command_efcoretools_webapi, shell=True, check=True)

    # Open Visual Studio Code if is installed and the environment variable is set
    if os.environ.get('code'):
      subprocess.run(f'code .', shell=True, check=True)
    else:
      print('Visual Studio Code is not installed or the environment variable is not set')
      messagebox.showwarning('Warning', 'Visual Studio Code is not installed or the environment variable is not set')

    print(f"Proyecto {name_project} creado correctamente")
    messagebox.showinfo('Info', f'Project {name_project} created successfully')

  except subprocess.CalledProcessError as e:
    print(f"Error al crear el proyecto: {e}")
    messagebox.showerror('Error', f'Error creating the project: {e}')

# Function to generate the project
def create_project():
  path = entry_path.get()
  # Check if the path is empty
  if path == '':
    messagebox.showerror('Error', 'Select a path')
    return
  name_project = entry_name.get()
  # Check if the name is empty
  if name_project == '':
    messagebox.showerror('Error', 'Enter a project name')
    return
  generate_project(path, name_project)


# Create a main window
winndow = tk.Tk()
winndow.title('Generator .NET Core Project')
winndow.geometry('400x400')

# Label and Entry for path
label_path = tk.Label(winndow, text='Path:')
label_path.pack(pady=5)
entry_path = tk.Entry(winndow)
entry_path.pack(pady=5)
button_path = tk.Button(winndow, text='Select path', command=select_path)
button_path.pack(pady=5)

# Label and Entry for project name
label_name = tk.Label(winndow, text='Project name:')
label_name.pack(pady=5)
entry_name = tk.Entry(winndow)
entry_name.pack(pady=5)

# Button to generate project
button_create = tk.Button(winndow, text='Generate project', command=create_project)
button_create.pack(pady=20)

# Show windows where appear the messages
winndow.withdraw()

# show window where indicate thats working in the background
winndow.deiconify()

# Run the main loop
winndow.mainloop()

