This takes a folder containing only Yaz0 encoded files, and nothing else, and replaces all mentions of a string in the files (and the filenames) with a new string.

Only confirmed to work on Windows.

Requires BotW Unpacker v1.9.2 or higher (https://github.com/Shadsterwolf/BotWUnpacker/releases)

`python yaz0_string_replace.py UNPACKER_PATH PATH_TO_TARGET_FOLDER FIND_STRING REPLACE_STRING` 

e.g.

`python yaz0_string_replace.py "C:\Users\Username\Tools\BotwUnpacker.exe" "C:\Users\Username\Mod\content\UI\StockItem" "001" "601"` 