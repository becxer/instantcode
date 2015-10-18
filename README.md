# instantcode
Run the code which is in the clipboard and put result into clipboard


### 1. how to use this

after setting keyboard shortcut for run, 
you can just convert code instantly like below.

        [ ctrl+c ]  #put your code to clipboard 
        [ (your shorcut) ]  # convert your code to result
        [ ctrl+v ]  #paste your code result  

try these sample code : https://wiki.python.org/moin/SimplePrograms

### 2. how to pre-setting OS environment

#### window

        if want to use python
        1) install python2.7.x (https://www.python.org/downloads/)
        2) append python.exe's path into environment path
        
        if want to use win-c & win-cpp
        1) install visual_studio (https://www.visualstudio.com/)
        2) append cl.exe's path into environment path
        
        if want to use nodejs
        5) install nodejs (https://nodejs.org/en/download/)
        
        if want to use ruby
        6) install ruby (https://www.ruby-lang.org/)

### 3. how to install shortcut

#### window

        1) clone this project or download.zip ( & unzip)
        2) right click instantcode.py
        3) make shortcut of instantcode.py on desktop
        4) right click shortcut of instantcode.py
        5) set keyboard shortcut to '(your shortcut)' & hide icon also

### 4. how to change language

Just fix instantcode.ini with supported option below

        python
        win-cpp
        win-c
        nodejs
        ruby
