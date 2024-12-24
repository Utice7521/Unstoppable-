import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["Asset/"]
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "MyGame",
    version = "0.1",
    description = "My Pygame Game!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("Unstoppable!.py", base=base, icon="myicon.ico")]
)