
# Jarvis: Your Personal AI Assistant

  The project aims to develop a personal assistant system inspired by the fictional AI assistant depicted in the Iron Man series, named "Jarvis." This implementation utilizes Python programming language to create an interactive and versatile assistant capable of assisting users with a wide range of tasks.




## Key Objectives

1. **User Interaction**: The primary focus of the project is to enable users to interact with the assistant through both voice commands and a graphical user interface (GUI). This enhances user experience and accessibility.

2. **Task Automation**: "Jarvis" assists users by automating routine tasks, such as opening applications, playing music, sending emails, setting alarms, retrieving news updates, and more. These automated tasks aim to simplify the user's daily activities and increase productivity.

3. **Information Retrieval**: The assistant utilizes various APIs and web scraping techniques to fetch real-time information from the internet, including weather updates, news headlines, Wikipedia articles, and more. This functionality provides users with up-to-date and relevant information.

4. **System Integration**: "Jarvis" integrates with the user's system to perform system-related tasks like opening applications, controlling the camera, reading PDF files, hiding files, taking screenshots, and more. This deep system integration enhances the assistant's utility and versatility.

5. **Customization and Expansion**: The project allows for customization and expansion of the assistant's functionalities according to the user's preferences and requirements. Users can extend the assistant's capabilities by integrating additional APIs or adding new features based on their needs.

## Interface

![Alt text](https://github.com/VinayManda2/Jarvis/blob/main/images/demo.png)

## Installation

To run this project,First you need to generate "variables.txt" file by running "set_variables.py" file.

```bash
  python set_variables.py
```

Install required packages with 

```bash
  pip install -r requirements.txt
```
Now you can run main file by 

```bash
  python jarvis_Main.py
```




    
## Note

- For Windows users, it is recommended to install the **pyAudio** library



## Tasks Implemented

- Voice recognition and speech synthesis for natural language interaction.
- GUI integration using PyQt5 for enhanced user experience.
- Opening applications such as Notepad, Adobe Reader, Command Prompt, etc.
- Playing music from the user's directory.
- Fetching IP address and weather details based on the user's location.
- Retrieving news headlines from various sources.
- Reading PDF files and extracting text.
- Sending WhatsApp messages to specified contacts.
- Setting alarms and reminders for the user.
- Performing system actions like shutdown, restart, sleep, etc.
- Fetching information from Wikipedia and searching the web using web browser integration.
- Taking screenshots and hiding files for privacy and security.
- Providing entertainment by telling jokes fetched from an API.
