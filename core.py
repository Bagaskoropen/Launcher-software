import os
from pathlib import Path
import subprocess



def Directory_folder(project_code):
    Root_folder = 'D:\workspace-local\Launcher-software\project' 
    project_folder = os.path.join(Root_folder,project_code)
    hosts_folder = os.path.join(project_folder,'Hosts')

    return hosts_folder


 # Software launching 
def launch_DCC(DCC_name):
    DCC_folder =  Directory_folder(project_code)
    batch_folder = os.path.join(DCC_folder, DCC_name,'batch')
    batch_file = os.path.join(batch_folder,f'{DCC_name}_launch.bat')

    if DCC_name == "3dsMax":
        subprocess.Popen(fr"{batch_file}", shell=True)

    elif DCC_name == "Katana":
        subprocess.Popen(fr"{batch_file}", shell=True)

    elif DCC_name == "Nuke":
        subprocess.Popen(fr"{batch_file}", shell=True)

    elif DCC_name == "Maya":
        subprocess.Popen(fr"{batch_file}", shell=True)
    

    else:
        print(f"software {DCC_name} tidak tersedia")










