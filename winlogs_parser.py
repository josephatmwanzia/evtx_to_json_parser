#My first serious upload here.
#Builds on someones work but hey, baby steps

#imports
import subprocess, os, time, sys

#get important paths from arguments

print("\n[+] Performing initial checks ...\n")
time.sleep(1)
try:
    evtxd_path = sys.argv[1]
    path = sys.argv[2]
except:
    print("[-] Usage: python3 winlogs_parser.py [evtxd_path] [folder_path]")
    print("[-] The evtxd path on your system and folder with evtx files need to be provided")
    print("[-] Exiting ...")
    exit()


#Check if evtxd exists
if os.path.isfile(evtxd_path):
    print("[+] evtxd path okay.\n")
else:
    print("[-] Please install evtxd from https://github.com/omerbenamram/evtx/releases/download/v0.8.1/evtx_dump-v0.8.1-x86_64-unknown-linux-gnu and/or update path")
    print("[-] Install instructions here https://medium.com/@salim.y.salimov/a-hassle-free-evtx-to-json-converter-not-only-for-windows-but-linux-and-mac-os-too-82adc4d9d158")
    print("[-] Don't forget to make the evtxd executable in linux by chmod +x [file]")
    print("[-] Update the path in the this python file too")
    print("[!] Exiting ...")
    exit()

#Check if evtxd has correct permissions
if os.access(evtxd_path, os.X_OK):
    pass
else:
    print("[-] Please make evtxd executable by running: chmod x [path_to_evtxd]")
    print("[!] Exiting ...")
    exit()

#Check if folder exists
if os.path.isdir(path):
    print("[+] Folder path exists.\n")
else:
    print("[-] Please specify a valid folder where evtx files are stored.")
    print("[!] Exiting ...")
    exit()

print("[+] Initial checks Done.\n")
time.sleep(1)

#create new folder for converted files
def create_new_folder(old_folder_path):
    new_folder_path = os.path.join(old_folder_path, "converted_files")
    print("[+] Creating new folder for converted files.")
    try:
        os.makedirs(new_folder_path)
        print("[+] Folder created")
    except FileExistsError:
        print("[>] Folder exists")
        pass

    return new_folder_path

#Reads file names to be converted
def files_list(dir):
    return [i for i in os.listdir(dir) if i.endswith('.evtx')]

#Converts evt files to json files
def converter(file_path, evtx_file_name):
    print("\n\n[+] Converting " + evtx_file_name)

    #Use evtxd to convert to json
    convertion_result = subprocess.run([evtxd_path, "-o" "json", file_path, "--dont-show-record-number"], capture_output= True, text=True)

    #Check success
    if convertion_result.returncode == 0:
        print("[+] Converted.")        
    else:
        print("[-] Failed to convert " + file_path)
        print("[-] Exit code : " + str(convertion_result.returncode))
        return  #exits the function
    
    #surround results with [..]
    json_1 = "[" + convertion_result.stdout + "]"

    #separate items with comma -- code just produces results without comma!
    json_2 = json_1.replace("}\n{", "},\n{")

    return json_2


#write converted filed to new folder
def write_json_file(json, new_folder_path,evtx_file_name):
    print("[+] Writing json to new directory.")

    json_file_path = os.path.join(new_folder_path,evtx_file_name[:-4]) + "json"

    try:
        json_file = open(json_file_path, "x")
        json_file.write(json)
        json_file.close()
        print("[+] Written json file to new directory" + "\n")
    except:
        print("[-] json file exists, did not write. Please delete file and re-run\n")
        pass



  
#Read evtx files
evtx_files = files_list(path)
evtx_files_len = len(evtx_files)



#Bring it together
if evtx_files_len == 0:
    print("[-] No files found for Convertion.")
else:
    #create new folder
    new_folder_path = create_new_folder(path)

    for i, evtx_file in enumerate(evtx_files, start=1):
        full_path = os.path.join(path,evtx_file)

        json_string = converter(full_path, evtx_file)

        write_json_file(json_string,new_folder_path,evtx_file)

        print(f'\r[+] {i/evtx_files_len:.0%} [{"▓"*int(10*i/evtx_files_len)+" "*int(10*(evtx_files_len-i)/evtx_files_len)}]', end='')

        time.sleep(1)

print("\n\n[+] All done. Good luck")
