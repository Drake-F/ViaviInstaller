import subprocess
import sys
import ctypes
from pathlib import Path

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
    requirements_path = Path(__file__).resolve().parent / "resources" / "requirements.txt"

    try:
        subprocess.run([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            str(requirements_path)
        ],
        check=True
        )

        print("Requirements installed successfully.")

    except subprocess.CalledProcessError as error:
        print(f"Requirements installation failed: {error}")

    except FileNotFoundError:
        print("Requirements file or Python executable not found.")

def zebraInstall():
    install_path = Path(__file__).resolve().parent / "resources" / "zebradesigner3-330104.exe"

    try:
        result = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            str(install_path),
            None,
            str(install_path.parent),
            1
        )

        if result <= 32:
            print(f"Failed to launch installer. Error code: {result}")
        else:
            print("Zebra Designer installer launched.")

    except FileNotFoundError:
        print("Zebra Designer installer not found.")

    except OSError as error:
        print(f"Failed to launch installer: {error}")

def viperInstall():
    install_path = Path(__file__).resolve().parent / "resources" / "Viper" / "setup.exe"

    try:
        result = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            str(install_path),
            None,
            str(install_path.parent),
            1
        )

        if result <= 32:
            print(f"Failed to launch installer. Error code: {result}")
        else:
            print("Viper Monitor installer launched.")

    except FileNotFoundError:
        print("Viper Monitor installer not found.")

    except OSError as error:
        print(f"Failed to launch installer: {error}")

def mstInstall():
    install_path = Path(__file__).resolve().parent / "resources" / "MST" / "setup.exe"

    try:
        result = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            str(install_path),
            None,
            str(install_path.parent),
            1
        )

        if result <= 32:
            print(f"Failed to launch installer. Error code: {result}")
        else:
            print("MST installer launched.")

    except FileNotFoundError:
        print("MST installer not found.")

    except OSError as error:
        print(f"Failed to launch installer: {error}")

def ms_cipInstall():
    install_path = Path(__file__).resolve().parent / "resources" / "MS-CIP" / "setup.exe"

    try:
        result = ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            str(install_path),
            None,
            str(install_path.parent),
            1
        )

        if result <= 32:
            print(f"Failed to launch installer. Error code: {result}")
        else:
            print("MS-CIP installer launched.")

    except FileNotFoundError:
        print("MS-CIP installer not found.")

    except OSError as error:
        print(f"Failed to launch installer: {error}")