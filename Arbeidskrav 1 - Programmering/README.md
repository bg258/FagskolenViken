# **Arbeidskrav 1 - Programmering**

For the following assignment the main focus was to make it easy to locate and read Bible verses without having to memorize each reference.

The assignment runs in the terminal and lets you:
- Look through a table which lists 8 suggested Bible verses.
- The main file lets you search for a verse. For that, you will need to enter a reference (for example John 3:16)
- Selects one random verse from the bible. 
- The main file will also let you use two different Bible APIs to compare the same verse.

## APIs used

My program gets data from two different API sources:

1. **[bible-api.com](https://bible-api.com/)** – gets the text of Bible verses. This API does not need a key.
2. **[API.Bible](https://api.bible/)** – gets a verse from another English Bible translation. This API needs an API key.

The API.Bible key is loaded from the local `.env` file instead of being written in the Python code. In this case, my repository is a private one, so I do not need to worry about leaking the private key.

## How can I run the following program?
For us to being able to run the following program, we will need:
* Python 3.10 or newer
* Internet connection
* Own API key from API.Bible (in this case, you dont need one since I have included my own private key)

**Steps**

1. Download the project from GitHub and open the folder in VS Code (or another editor).
2. Open a terminal in the project folder and run the following sequence. It will install the required packages needed:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. Go to [api.bible](https://api.bible/), create an account and get an API key.
4. Create a file called `.env` in the same folder as `main.py` and add this line:

   ```env
   API_BIBLE_KEY=OcmdrFRICnENxcWh3IjgD
   ```

5. Start the program:

   ```bash
   python3 main.py
   ```

**NB:** You only need to download the requirements and run the main file, since I have already included a private key.

****
When the program runs you will have the option to choose between different tasks from the menu. 

To check that **both APIs** work, you can try the option **(4)** and enter `John 3:16`. This option will compare one verse at a time. And Vuala! 

Try the different optiosn to learn more about jesus and the bible. 


## Project files

- `main.py` – the Python program, including the menu and API requests.
- `requirements.txt` – the packages needed to run the program.
- `.gitignore` – prevents the API key and temporary Python files from being added to GitHub.
- `README.md` – information about the project and how to run it.
