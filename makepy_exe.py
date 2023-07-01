import os
import shutil

def search_file():
	found = False
	pyra_for_exe = str(os.path.join(os.path.expanduser("~"), 'pyra_env', 'pyra_for_exe'))
	exe_make = str(os.path.join(os.path.expanduser("~"), 'pyra_env', 'exe_make'))
	try:
		folder = exe_make
		for filename in os.listdir(folder):
		    if filename.endswith('.ico'):
		        continue
		    else:
		        file_path = os.path.join(folder, filename)
		        try:
		            if os.path.isfile(file_path) or os.path.islink(file_path):
		                os.unlink(file_path)
		            elif os.path.isdir(file_path):
		                shutil.rmtree(file_path)
		        except Exception as e:
		            print(f'Failed to delete {file_path}. Reason: {e}')
		print(" Old Files Deleted from exe_make directory.\n Starting fresh...\n __________________________")
		os.chdir(pyra_for_exe)
		files = os.listdir()
		for i in files:
			if i.endswith(('.py', 'pyw')):
				print(f" {i}")
		print(" __________________________")
		filename = str(input(' Enter a filename: '))
		src = f'{pyra_for_exe}//{filename}'
		dst = f'{exe_make}//{filename}'
		shutil.copyfile(src, dst)
		print(f' {filename} has been copied to exe_make dir.')
		os.chdir(exe_make)
		picname = str(input(' Enter a icon filename: '))
		print(f' {filename} and {picname} found in exe_make.')
		os.system(f'pyinstaller --clean --onefile -i "{exe_make}/{picname}" "{exe_make}/{filename}"')
		print(f' {filename} exe created successfully.')
		dist = str(os.path.join(os.path.expanduser("~"), 'pyra_env', 'exe_make', 'dist'))
		os.chdir(dist)
		exe_file = os.listdir(dist)
		for i in exe_file:
			if i.endswith(('')):
				file_name = i
				pyra_exe_dir = str(os.path.join(os.path.expanduser("~"), 'pyra_env', 'pyra_exes'))
				from_exe_make = f'{exe_make}//dist//{i}'
				to_pyra_exes = f'{pyra_exe_dir}//{i}'
				shutil.copyfile(from_exe_make, to_pyra_exes)
				os.chdir(pyra_exe_dir)
				os.system(f'chmod +x {i}')
				print(" ---file copied to pyra_exes directory---")

	except Exception as e:
			print(e)

print(" ___  _   _ ____ ____    ___ ____    ____ _  _ ____\n |__]  \\_/  |__/ |__|     |  |  |    |___  \\/  |___\n |      |   |  \\ |  |     |  |__|    |___ _/\\_ |___\n ___________________________________________________")
search_file()