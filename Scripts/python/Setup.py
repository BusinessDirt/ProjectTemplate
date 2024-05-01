import os
import subprocess
import platform

from SetupPython import PythonConfiguration as PythonRequirements
PythonRequirements.validate()

from SetupPremake import PremakeConfiguration as PremakeRequirements
os.chdir('../../') # change from scripts/python directory to root

premakeInstalled = PremakeRequirements.validate()

print("\nUpdating submodules...")
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

if (premakeInstalled):
    if platform.system() == "Windows":
        print("\nRunning premake...")
        subprocess.call([os.path.abspath("./scripts/windows/Win-GenProjects.bat"), "nopause"])

    if platform.system() == "Linux":
        print("\nRunning premake...")
        subprocess.call([os.path.abspath("./scripts/linux/Linux-GenProjects.sh")])

    if platform.system() == "Darwin":
        print("\nRunning premake...")
        subprocess.call([os.path.abspath("./scripts/macosx/MacOSX-GenProjects.sh")])

    print("\nSetup completed!")
else:
    print("Project requires Premake to generate project files.")