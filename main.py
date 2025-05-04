import os
import zipfile
import shutil

from config import folder_path, range_start, range_end


counter = 0
c = 0 

def present_files_in_directory(directory, new_file):
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.svg']
    global c
    c+=1
    for filename in os.listdir(directory):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            if filename == new_file:
                return True        
    return False
    

def unpack_archieves():
    for archive_name in os.listdir(folder_path):
        source_folder = folder_path + "/" + archive_name[:-4]
        if archive_name.endswith('.zip'):
            try:
                with zipfile.ZipFile(folder_path + "/" + archive_name, 'r') as zip_ref:
                    
                    if os.path.exists(source_folder):
                        response = input("The file already exists. Do you want to overwrite it? (yes/no)")
                        if response.lower() == 'yes' or response.lower() == 'y':
                            shutil.rmtree(source_folder)
                            zip_ref.extractall(folder_path)
                            zip_ref.close()
                        else:
                            print(f"The file {archive_name} has been skipped")
                    else:
                        zip_ref.extractall(folder_path)
                        zip_ref.close()
                        for file in os.listdir(source_folder):
                                try:
                                    is_present = present_files_in_directory(folder_path, file)
                                    if not is_present:
                                        shutil.move(source_folder + "/" + file, folder_path)
                                        print(f"The file is successfully added: {file}")
                                        global counter
                                        counter+=1
                                except Exception as e:
                                    print(f"Error while processing {file}: {e}")                  
            except Exception as e:
                print(f"Error while processing {archive_name}: {e}")
            shutil.rmtree(source_folder)
    print(f"The amount of unpacked files: {counter}")

def package_integrity_check():
    counter = 0
    couter_exist = 0

    file_names = []

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_names.append(file_name[1:-4])
        counter+=1

    print(f"{counter}\n")

    for x in range(range_start, range_end):    
        if str(x) in file_names:
            couter_exist+=1
        else:
            print(x)
            
        if str(x)+"M01" in file_names:
            couter_exist+=1 
        else:
            print(str(x)+"M01")
        
    print(couter_exist)

if __name__ == "__main__":
    unpack_archieves()
    #package_integrity_check()

