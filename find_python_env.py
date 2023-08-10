import os

def find_folders_with_file(folder, filename):
    folders_with_file = []
    
    for root, dirs, files in os.walk(folder):
        if filename in files:
            folder_name = os.path.basename(root)
            folder_path = os.path.abspath(root)
            usage_env = os.path.join(folder_path, "bin", "activate")
            folders_with_file.append((folder_name, folder_path, usage_env))
    
    return folders_with_file

def main():
    folder_place = input("Input folder you want (. is default): ")
    if not folder_place:
        folder_place = "."

    filename = "pyvenv.cfg"
    
    print("===============================")
    print("List semua venv yang anda buat:")
    print("===============================")
    print("{:<4} {:<10} {:<40} {}".format("No", "Venv", "Path", "Usage"))
    
    folders_with_file = find_folders_with_file(folder_place, filename)
    for i, (folder_name, folder_path, usage_env) in enumerate(folders_with_file, start=1):
        print("{:<4} {:<10} {:<40} {}".format(i, folder_name, folder_path, "source " + usage_env))

if __name__ == "__main__":
    main()
