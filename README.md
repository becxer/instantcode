# instantcode
Run the code which is in the clipboard and put result into clipboard


### 0. How to use this

After setting keyboard shortcut for run, 
you can just convert code instantly like below.

        [ ctrl+c ]  #Put your code to clipboard 
        [ (your shorcut) ]  #Convert your code to result
        [ ctrl+v ]  #Paste your code result  

Try these sample code : https://wiki.python.org/moin/SimplePrograms

### 1. How to pre-setting OS environment

        If want to use python
        0) install python2.7.x (https://www.python.org/downloads/)
        1) (window) append python.exe's path into environment path
        
        If want to use win-c & win-cpp
        0) install visual_studio (https://www.visualstudio.com/)
        1) append cl.exe's path into environment path
        
        If want to use nodejs
        0) install nodejs (https://nodejs.org/en/download/)
        
        If want to use ruby
        0) install ruby (https://www.ruby-lang.org/)

### 2. How to install shortcut

#### Window

        0) Clone this project or download.zip ( & unzip)
        1) Right click instantcode.py
        2) Make shortcut of instantcode.py on desktop (Must to be in desktop)
        3) Right click shortcut of instantcode.py
        4) Set keyboard shortcut to '(your shortcut)' & hide icon also
        
#### MacOSX

        0) Clone this project or download.zip ( & unzip)
        1) Launch automator and select service -> library -> "shell script"
        2) Write shell code "python (path to instantcode)/instantcode.py"
        3) Save automator service name "instantcode"
        4) Go to system-preference -> keyboard -> shortcut -> service
        5) Select "instantcode" & set keyboard shortcut to '(your shorcut)'
        6) reboot 

### 3. How to change language

Just fix instantcode.ini with supported option below

        python
        win-cpp
        win-c
        nodejs
        ruby
