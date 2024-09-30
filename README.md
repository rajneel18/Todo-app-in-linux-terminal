
To-Do List Terminal App

This is a simple and advanced terminal-based To-Do List application built using Python. It allows users to add, update, remove, and view tasks directly from the terminal.

Features

- Add tasks
- Remove tasks
- Update tasks
- View tasks
- Interactive commands

Requirements

- Python 3.x

Installation

1. Clone or download the app to your preferred location:
   git clone https://github.com/rajneel18/Todo-app-in-linux-terminal.git
2. Navigate to the app directory:
   cd /path/to/your/todo_app

3. Run the app:
   python3 tudu.py

Usage

Once the app is running, you can use the following commands:

- add/ - Add a new task
- evoke/ - Remove a task
- updt/ - Update an existing task
- show/ - View all tasks
- need/ - Show available commands

Run on Startup

Linux (Ubuntu) Startup

To make the app run on startup:

1. Create a startup script:

   nano ~/todo_app/start_todo.sh

2. Add the following code to the script:

   #!/bin/bash
   gnome-terminal -- bash -c "python3 /path/to/your/todo_app/tudu.py; exec bash"

3. Save and close the file. Then make it executable:

   chmod +x ~/todo_app/start_todo.sh

4. Add the script to Startup Applications:

   - Open Startup Applications via the terminal:
     gnome-session-properties
   - Click Add, and set the command to:
     /home/username/todo_app/start_todo.sh

5. Save and restart your computer. The app will now run on startup.

License

This project is licensed under the MIT License - see the LICENSE file for details.
