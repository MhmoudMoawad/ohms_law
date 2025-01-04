### Setup:
1. From visual studio code click on **"Terminal"** and select **"New Terminal"**
2. select "Git Bash" and type following commands

```
        // upgrade pip
        python.exe -m pip install --upgrade pip
        
        // Create virtual enviornment
        py -m venv .venv

        // Activate .venv environment
        source .venv/Scripts/activate .env

        // Install require packages
        pip install customtkinter

        // create requirements text file
        pip freeze > requirements.txt

        // install required packages
        pip install -r ./requirements.txt
```