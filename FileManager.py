from time import sleep
import os

def main():
    while True:
        print("Welcome to File Manager!")
        options = input("(1)Make File\n(2)Read File\n(3)Remove File\n(4)Rename File\nType 'Exit' to leave.\nOption: ")

        if options == "1":
            file_name = input("File Name: ")
            file_type = input("File Type: ")
            a = open(file_name + file_type, "a+")
            print("- Created file " + file_name + file_type + "!")
            sleep(2)

        if options == "2":
            file_name = input("File Name: ")
            file_type = input("File Type: ")
            f = open(file_name + file_type, "r")
            message = f.read()
            print(message)
            f.close()
            sleep(2)
    
        if options == "3":
            file_name = input("File Name: ")
            file_type = input("File Type: ")
            os.remove(file_name + file_type)
            print("- Removed" + file_name + file_type + "!")
            sleep(2)

        if options == "4":
            old_file_name = input("Current File Name: ")
            old_file_type = input("Current File Type: ")
            new_file_name = input("New File Name: ")
            new_file_type = input("New File Type: ")
            os.rename(old_file_name + old_file_type, new_file_name + new_file_type)

        if options == "Exit":
            sleep(1)
            break
        
if __name__ == "__main__":
    main()
        
