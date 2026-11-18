import subprocess

def pyInstall():
    try:
        result = subprocess.run(
            ["winget", "install", "--id", "Python.Python.3.12", "-e",
             "--accept-package-agreements", "--accept-source-agreements"],
             check=True,
             capture_output=True,
             text=True
        )

        print(result.stdout)

    except subprocess.CalledProcessError as error:
        print(f"Installation failed: {error.stderr}")

    except FileNotFoundError:
        print("Winget is not installed or unavailable.")

    installPyRequirements()

def installPyRequirements():
    pass