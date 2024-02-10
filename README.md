# evtx_to_json_parser
Convert windows event logs into readable json files
This file advances on the work of https://github.com/omerbenamram/evtx.
Specificaly
- Processes evtx files from folders
- makes results from his code a list of items. Making them readble by most other programs.

For instalation of the evtxd file, follow these intructions https://medium.com/@salim.y.salimov/a-hassle-free-evtx-to-json-converter-not-only-for-windows-but-linux-and-mac-os-too-82adc4d9d158

USAGE
--------------------------
python3 winlogs_parser.py [path_to_evtxd] [path_to_folder_wit_log_files]

Note.
1. You must install the evtxd from here https://github.com/omerbenamram/evtx/releases/download/v0.8.1/evtx_dump-v0.8.1-x86_64-unknown-linux-gnu
2. make it executable: chmod +x [file]

Happy hunting ...
