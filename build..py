from PyInstaller import __main__

if __name__ == '__main__':
    __main__.run([
        'A:\\pythonProjects\\final_yr\\riyalllll_cpp\\main.py',
        '--onefile',            # Create a single executable file
        '--windowed',           # Don't show the console window
        '--name', 'BILL GENERATION'     # Name of the output executable
    ])