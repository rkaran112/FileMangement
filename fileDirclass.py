import os
import fnmatch as fn
import shutil as sh
import zipfile as zip
class FileManagement():   
    
    def open_file(self):
        Dir_path = dir_mn.check_dir()
        if Dir_path:
            F_name = input("Enter the name of the file: ")
            file_Path = os.path.join(Dir_path, F_name)
            
            try:
                with open(file_Path, "r") as f:
                    open_f = f.read()
                    print("File contents:")
                    print(open_f)
            except FileNotFoundError:
                print(f"File '{F_name}' not found.")
            except Exception as e:
                print("Error:", e)
    def create_File(self):
        Dir_path = dir_mn.check_dir()
        try:
            if Dir_path:
                F_name=input("Enter the name of the file")
                if not F_name:
                    print("file must have name")
                    return
                try:
                    file_path = os.path.join(Dir_path, F_name)
                    with open (file_path,'x') as new_file:
                        print(f"File '{F_name}' created Successfully")
                except FileExistsError:
                    print(f"File '{F_name}.txt' already Exists")
        except FileNotFoundError:
                print("Invalid Path ",Dir_path)
    
    def delete_File(self):
        Dir_path = dir_mn.check_dir()
        if Dir_path:
            try:
                F_name=input("Enter file name") 
                file_Path = os.path.join(Dir_path, F_name)
                if os.path.exists(file_Path):
                    os.remove(file_Path)
                    print("Removed file successfully")
            except FileNotFoundError as e:
                print("Invalid or missing directories",e)
 
    def search_File(self):
        Dir_path = dir_mn.check_dir()
        if Dir_path:
            F_pattern = input("Enter the pattern to search (e.g., *.txt): ")
            match_files = []

            try:
                for file_name in os.listdir(Dir_path):
                    if fn.fnmatch(file_name, F_pattern):
                        file_path = os.path.join(Dir_path, file_name)
                        match_files.append(file_path)
                        print(f"Matched file: {file_path}")

                if not match_files:
                    print("No files matched the pattern.")
                    
                return match_files
            except FileNotFoundError:
                print(f"Directory '{Dir_path}' does not exist.")
            except Exception as e:
                print("Error:", e)          
class DirectoryManagement():
    def check_dir(self):
        Dir_path = input("Enter the path of the directory")
        if not os.path.exists(Dir_path):
            try:
                Exit = int(input("Few directories missing do you want to create them \n1.Yes\n2.No?"))
            except ValueError:
                print("Invalid choice, please enter 1 or 2.")
                return False
            try:
                if Exit==1:
                    print("Created the directory and other missing directories")
                    os.makedirs(Dir_path)
                    return Dir_path
            except FileNotFoundError as e :
                print("File not fond", str(e))
                return False
        else:
            return Dir_path
    
    def remove_Path(self):
        Dir_path = self.check_dir()  # Assuming dir_mn is an instance of DirectoryManagement

        try:
            if Dir_path:
                sh.rmtree(Dir_path)
                print("Removed Directory successfully")
        except FileNotFoundError as e:
            print("Invalid or missing directories:", e)
    
    def list_Directories(self):
        Dir_path = self.check_dir()

        if Dir_path:
            try:
                directories = [d for d in os.listdir(Dir_path) if os.path.isdir(os.path.join(Dir_path, d))]
                if directories:
                    print("List of directories:")
                    for directory in directories:
                        print(directory)
                else:
                    print("No directories found.")
                return directories
            except FileNotFoundError as e:
                print(f"{Dir_path} is invalid:", e)
        else:
            print(f"{Dir_path} is invalid")
class FileOperations():

    def write_File(self):
        Dir_path = dir_mn.check_dir()
        if not Dir_path:
            print("Invalid directory.")
            return
        F_name=input("Enter the name of the file")
        try:
            file_Path = os.path.join(Dir_path,F_name)
            with open(file_Path,"a") as Uappend:
                    changes =input("Enter data to change")
                    Uappend.write(changes)
        except FileNotFoundError as e:
               print("No such file exists!!",e)

    def copy_File(self):
        F_name = input("Enter the name File to be copied ")
        file_Path= dir_mn.check_dir()
        if not file_Path:
            print("Invalid source directory.")
            return
        src = os.path.join(file_Path,F_name)
        print("Enter the File where it has to be copied")
        dst= dir_mn.check_dir()
        if not dst:
            print("Invalid destination directory.")
            return
        try:
            sh.copy(src,dst)
            print(f"File '{src}' copied to '{dst}' successfully.")
        except PermissionError:
            print("Error: Insufficient permissions to copy the file.")
        except sh.SameFileError:
            print("Error: Source and destination paths point to the same file.")
        except IOError as e:
            print(f"IO Error: {e}")

    def move_File(self):
        F_name = input("Enter the name File to be Moved ")
        file_Path= dir_mn.check_dir()
        if not file_Path:
            print("Invalid source directory.")
            return
        src = os.path.join(file_Path,F_name)
        print("Enter the File where it has to be Moved")
        dst= dir_mn.check_dir()
        if not dst:
            print("Invalid destination directory.")
            return
        try:
            sh.move(src,dst)
            print(f"File '{src}' Moved to '{dst}' successfully.")
        except PermissionError:
            print("Error: Insufficient permissions to copy the file.")
        except sh.SameFileError:
            print("Error: Source and destination paths point to the same file.")
        except IOError as e:
            print(f"IO Error: {e}")
class AddFunction():
    def create_Zip(self):
        Dir_path = dir_mn.check_dir()
        print("Directory Path:", Dir_path)  # Debugging output
        if not Dir_path:
            print("Error: Directory path is invalid.")
            return

        try:
            zip_Archive = [d for d in os.listdir(Dir_path) if os.path.join(Dir_path, d)]
            if not zip_Archive:
                print("No files found in the directory to zip.")
                return

            zip_Name = input("Enter the Name of the Archive: ")
            # password = input("Enter the password for the archive: ")

            with zip.ZipFile(f"{zip_Name}.zip", 'w') as zip_File:
                for file in zip_Archive:
                    file_path = os.path.join(Dir_path, file)
                    zip_File.write(file_path, os.path.basename(file))
                # zip.set_password(password.encode())
                print(f"Archive '{zip_Name}.zip' created successfully with password.")

        except FileNotFoundError:
            print("Error: Directory not found.")
        except zip.BadZipFile:
            print("Error: File is corrupt.")
        except PermissionError:
            print("Error: Permission denied. Check if you have the necessary permissions to access the directory.")

    def extract_Zip(self):
        Dir_path = dir_mn.check_dir()  # Assuming dir_mn is an instance of DirectoryManagement

        if Dir_path:
            try:
                Zip_path = input("Enter file path: ")
                file_Path = os.path.join(Dir_path, Zip_path)

                if not os.path.exists(file_Path):
                    raise FileNotFoundError("File not found in the location")

                dir_Extract = input("Enter directory to extract to: ")

                with zip.ZipFile(file_Path, 'r') as zip_File:
                    zip_File.extractall(dir_Extract)
                    print("Extraction completed successfully.")
            except FileNotFoundError as e:
                print("Error:", e)
            except Exception as e:
                print("Error:", e)

def main_menu():
    print("1. Open File")
    print("2. Create File")
    print("3. Delete File")
    print("4. Search File")
    print("5. Write File")
    print("6. Copy File")
    print("7. Move File")
    print("8. Create Zip Archive")
    print("9. Extract Zip Archive")
    print("10. List Directories")
    print("11. Remove Directory")
    print("12. Exit")

    choice = input("Enter your choice: ")
    return choice
add_function = AddFunction()
dir_mn = DirectoryManagement()
file_management = FileManagement()
file_operation  = FileOperations()

while True:
    choice = main_menu()

    if choice == '1':
        file_management.open_file()
    elif choice == '2':
        file_management.create_File()
    elif choice == '3':
        file_management.delete_File()
    elif choice == '4':
        file_management.search_File()
    elif choice == '5':
        file_operation.write_File()
    elif choice == '6':
        file_operation.copy_File()
    elif choice == '7':
        file_operation.move_File()
    elif choice == '8':
        add_function.create_Zip()
    elif choice == '9':
        add_function.extract_Zip()
    elif choice == '10':
        dir_mn.list_Directories()
    elif choice == '11':
        dir_mn.remove_Path()
    elif choice == '12':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
