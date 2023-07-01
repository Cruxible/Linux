import os
print(" ___  _   _ ____ ____\n |__]  \\_/  |__/ |__|\n |      |   |  \\ |  |\n _______________________\n pyra python auto compiler")
print(' _______________________')
print(' See files: list files\n Exit program: exit')
print(' _______________________')
while True:
    filename = input(' Enter a filename: ')
    if filename == 'list files':
        os.system('clear')
        exe_dir = os.listdir(os.path.join(os.path.expanduser("~"), "pyra_env", "pyra_exes"))
        for _ in exe_dir:
            print(f' {_}')
        for_dir = os.listdir(os.path.join(os.path.expanduser("~"), "pyra_env", "pyra_for_exe"))
        for _ in for_dir:
            print(f' {_}')
        print(' _______________________')
        continue
    if filename == 'exit':
        break
    else:
        found = False
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        try:
            for dirpath, dirnames, filenames in os.walk(desktop):
                if filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    found = True
                    os.chdir(dirpath)
                    break
            if not found:
                d_drive = os.path.join(os.path.expanduser("~"))
                for dirpath, dirnames, filenames in os.walk(d_drive):
                    if filename in filenames:
                        filepath = os.path.join(dirpath, filename)
                        found = True
                        os.chdir(dirpath)
                        break
            if not found:
                raise FileNotFoundError(f"{filename} not found in Desktop or pyra env")
            if filename.endswith('.c'):
                output_file = filename.replace('.c', '')
                os.system(f'gcc {filename} -o {output_file}')
                print(f' {filename} compilation complete.\n {filepath}')
                #status_label.config(text=f'{filename} compilation complete.\n{filepath}')
            
            elif filename.endswith('.cpp'):
                output_file = filename.replace('.cpp', '')
                os.system(f'g++ {filename} -o {output_file}')
                print(f' {filename} compilation complete.\n {filepath}')
            
            elif filename.endswith('.py'):
                os.system(f'python3 {filename}')
                print(f' {filename} execution/compilation complete.\n {filepath}')

            elif filename.endswith('.pyw'):
                os.system(f'python3 {filename}')
                print(f' {filename} execution/compilation complete.\n {filepath}')

            elif filename.endswith('.asm'):
                print(f'nasm -f win32 {filename}')
                os.system(f'nasm -f win32 {filename}')
                output_file = filename.replace('.asm', '.obj')
                output_file2 = output_file.replace('.obj', '.exe')
                time.sleep(3)
                print(f'gcc {output_file} -o {output_file2}')
                os.system(f'gcc {output_file} -o {output_file2}')
                print(f' {filename} compilation and execution complete.\n {filepath}')

            elif filename.endswith('.obj'):
                output_file = filename.replace('.obj', '')
                os.system(f'gcc {filename} -o {output_file}')
                print(f' {filename} compilation complete.\n {filepath}')

            elif filename.endswith(''):
                os.system(f'chmod +x {filename}')
                os.system(f'./{filename}')
                print(f' {filename} execution.\n {filepath}')

            elif filename.endswith('.pdf'):
                os.system(f'./{filename}')
                print(f' {filename} execution in\n {filepath}')

        except Exception as e:
            print(e)