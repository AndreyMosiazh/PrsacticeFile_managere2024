import os
import sys

class FileManagerApp:
    def __init__(self, args):
        self.directory = 'files'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        if args:
            self.handle_args(args)
        else:
            self.run()

    def handle_args(self, args):
        if len(args) > 1:
            command = args[0]
            if command == 'create':
                self.create_text_file_from_args(args[1], args[2] if len(args) > 2 else "")
            else:
                print("Unknown command")
        else:
            self.run()

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter choice: ").strip()
            if choice == '1':
                self.create_text_file()
            elif choice == '2':
                self.create_file_with_docker()
            elif choice == '3':
                self.edit_file()
            elif choice == '4':
                self.delete_file()
            elif choice == '5':
                self.upload_file()
            elif choice == '6':
                self.list_files()
            elif choice == '7':
                self.show_file_content()
            elif choice == '8':
                break
            else:
                print("Invalid choice. Please try again.")

    def print_menu(self):
        print("\nFile Manager")
        print("1. Create Text File")
        print("2. Create File with Docker")
        print("3. Edit File")
        print("4. Delete File")
        print("5. Upload File")
        print("6. List Files")
        print("7. Show File Content")
        print("8. Exit")

    def create_text_file(self):
        filename = input("Enter filename: ").strip()
        content = input("Enter content: ").strip()
        if filename:
            path = os.path.join(self.directory, filename)
            with open(path, 'w') as file:
                file.write(content)
            print(f"File {filename} created successfully.")

    def create_text_file_from_args(self, filename, content):
        if filename:
            path = os.path.join(self.directory, filename)
            with open(path, 'w') as file:
                file.write(content)
            print(f"File {filename} created successfully.")

    def create_file_with_docker(self):
        filename = input("Enter filename: ").strip()
        content = input("Enter content: ").strip()
        if filename:
            cmd = f'docker run --rm -v $(pwd)/{self.directory}:/files alpine sh -c "echo \\"{content}\\" > /files/{filename}"'
            os.system(cmd)
            print(f"File {filename} created with Docker successfully.")

    def list_files(self):
        files = os.listdir(self.directory)
        print("\nFiles:")
        for file in files:
            print(file)

    def show_file_content(self):
        filename = input("Enter filename to view content: ").strip()
        path = os.path.join(self.directory, filename)
        self.show_text_content(path)

    def show_text_content(self, path):
        with open(path, 'r') as file:
            content = file.read()
        print("\nFile Content:")
        print(content)

    def edit_file(self):
        filename = input("Enter filename to edit: ").strip()
        path = os.path.join(self.directory, filename)
        self.edit_text_file(path)

    def edit_text_file(self, path):
        with open(path, 'r') as file:
            content = file.read()
        print("\nCurrent Content:")
        print(content)
        new_content = input("\nEnter new content: ").strip()
        with open(path, 'w') as file:
            file.write(new_content)
        print("File updated successfully.")

    def delete_file(self):
        filename = input("Enter filename to delete: ").strip()
        path = os.path.join(self.directory, filename)
        os.remove(path)
        print(f"File {filename} deleted successfully.")

    def upload_file(self):
        file_path = input("Enter the full path of the file to upload: ").strip()
        if os.path.exists(file_path):
            filename = os.path.basename(file_path)
            destination = os.path.join(self.directory, filename)
            with open(file_path, 'rb') as src_file:
                with open(destination, 'wb') as dst_file:
                    dst_file.write(src_file.read())
            print(f"File {filename} uploaded successfully.")
        else:
            print("File does not exist.")

if __name__ == "__main__":
    args = sys.argv[1:]
    FileManagerApp(args)
