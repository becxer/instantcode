# instantcode
Run the code which is in the clipboard and put result into clipboard


### 1. How to use this

After setting keyboard shortcut for run, 
you can just convert code instantly like below.

        [ ctrl+c ]  #Put your code to clipboard 
        [ (your shorcut) ]  #Convert your code to result
        [ ctrl+v ]  #Paste your code result  

Try these sample code : https://wiki.python.org/moin/SimplePrograms

### 2. How to pre-setting OS environment

        If want to use python
        1) install python2.7.x (https://www.python.org/downloads/)
        2) (window) append python.exe's path into environment path
        
        If want to use win-c & win-cpp
        1) install visual_studio (https://www.visualstudio.com/)
        2) append cl.exe's path into environment path
        
        If want to use nodejs
        5) install nodejs (https://nodejs.org/en/download/)
        
        If want to use ruby
        6) install ruby (https://www.ruby-lang.org/)

### 3. How to install shortcut

#### Window

        1) Clone this project or download.zip ( & unzip)
        2) Right click instantcode.py
        3) Make shortcut of instantcode.py on desktop (Must to be in desktop)
        4) Right click shortcut of instantcode.py
        5) Set keyboard shortcut to '(your shortcut)' & hide icon also
        
#### MacOSX

        1) Clone this project or download.zip ( & unzip)
        2) Launch automator and select service -> library -> "shell script"
        3) Write shell code "python (path to instantcode)/instantcode.py"
        4) Save automator service name "instantcode"
        4) Go to system-preference -> keyboard -> shortcut -> service
        5) Select "instantcode" & set keyboard shortcut to '(your shorcut)'
        6) reboot 

### 4. How to change language

Just fix instantcode.ini with supported option below

        python
        win-cpp
        win-c
        nodejs
        ruby
