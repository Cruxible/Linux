import os
import time
import platform
import getpass
from datetime import datetime
from rich.tree import Tree
from rich import print
from rich.console import Console

def main():
    class MySexyVariables:
        user = getpass.getuser()
        curdir = os.getcwd()
        x = os.listdir()
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        home_dir = os.path.join(os.path.expanduser("~"))

    class main_logo:
        def logo():
            print(" [red1]___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |[/red1]\n")

    class Input:
        @staticmethod
        def get_string_input():
            console = Console()
            return console.input(" [bright_black]_____________________________________[/bright_black]" + "[bright_black]\n  __[/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (__[/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black]__: [/bright_black]")
            #filename = Input.get_string_input()

        @staticmethod
        def get_integer_input():
            console = Console()
            return int(console.input(" [bright_black]_____________________________________[/bright_black]" + "[bright_black]\n  __[/bright_black]" + "[red1]" + MySexyVariables.curdir + " [/red1]" + "[bright_black]\n (__[/bright_black]" + "[purple]" + MySexyVariables.user + "[/purple]" + "[bright_black]__: [/bright_black]"))
            #time_interval = Input.get_integer_input()

    class calls:
        @staticmethod
        def dir_list():
            os.system('clear')
            exe_dir = os.listdir(os.path.join(os.path.expanduser("~"), "pyra_env", "finished_programs"))
            for _ in exe_dir:
                print(f' [red1]{_}[/red1]')
    
    class compile_file:
        @staticmethod
        def compile_c_lang():
            end_time = datetime.now()
            output_file = filename.replace('.c', '')
            os.system(f'gcc {filename} -o {output_file}')
            print(f' {filename} compilation complete.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_c_plusplus():
            end_time = datetime.now()
            output_file = filename.replace('.cpp', '')
            os.system(f'g++ {filename} -o {output_file}')
            print(f' {filename} compilation complete.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_py():
            end_time = datetime.now()
            os.system(f'python3 {filename}')
            print(f' {filename} execution/compilation complete.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_pyw():
            end_time = datetime.now()
            os.system(f'python3 {filename}')
            print(f' {filename} execution/compilation complete.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_assembly():
            end_time = datetime.now()
            print(f'nasm -f win32 {filename}')
            os.system(f'nasm -f win32 {filename}')
            output_file = filename.replace('.asm', '.obj')
            output_file2 = output_file.replace('.obj', '.exe')
            time.sleep(3)
            print(f'gcc {output_file} -o {output_file2}')
            os.system(f'gcc {output_file} -o {output_file2}')
            print(f' {filename} compilation and execution complete.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_object_file():
            end_time = datetime.now()
            output_file = filename.replace('.obj', '')
            os.system(f'gcc {filename} -o {output_file}')
            print(f' {filename} compilation complete.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_executable():
            end_time = datetime.now()
            os.system(f'chmod +x {filename}')
            os.system(f'./{filename}')
            print(f' {filename} execution.\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

        def compile_pdf():
            end_time = datetime.now()
            os.system(f'./{filename}')
            print(f' {filename} execution in\n {filepath}')
            print(' Search Duration: {}'.format(end_time - start_time))

    main_logo.logo()
    print(' [bright_black]_______________________[/bright_black]')
    print(' [bright_black]See files: list files\n Exit program: exit[/bright_black]')
    while True:
        filename = Input.get_string_input()
        if filename == 'list files':
            calls.dir_list()
            continue
        if filename == 'exit':
            break
        else:
            start_time = datetime.now()
            found = False
            try:
                for dirpath, dirnames, filenames in os.walk(MySexyVariables.desktop):
                    if filename in filenames:
                        filepath = os.path.join(dirpath, filename)
                        found = True
                        os.chdir(dirpath)
                        break
                if not found:
                    for dirpath, dirnames, filenames in os.walk(MySexyVariables.home_dir):
                        if filename in filenames:
                            filepath = os.path.join(dirpath, filename)
                            found = True
                            os.chdir(dirpath)
                            break
                if not found:
                    raise FileNotFoundError(f"{filename} not found in Desktop or pyra env")
                if filename.endswith('.c'):
                    compile_file.compile_c_lang()
                elif filename.endswith('.cpp'):
                    compile_file.compile_c_plusplus()
                elif filename.endswith('.py'):
                    compile_file.compile_py()
                elif filename.endswith('.pyw'):
                    compile_file.compile_pyw()
                elif filename.endswith('.asm'):
                    compile_file.compile_assembly()
                elif filename.endswith('.obj'):
                    compile_object_file()
                elif filename.endswith(''):
                    compile_file.compile_executable()
                elif filename.endswith('.pdf'):
                    compile_file.compile_pdf()

            except Exception as e:
                print(e)

if __name__ == '__main__':
    print(f" System: {platform.system()}\n Node Name: {platform.node()}\n Release: {platform.release()}")
    print(f" Version: {platform.version()}\n Machine: {platform.machine()}\n Python version: {platform.python_version()}")
    time.sleep(2)
    os.system('clear')
    main()
