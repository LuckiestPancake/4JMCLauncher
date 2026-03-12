import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtGui import QIcon 

app = QApplication(sys.argv)

username_path = "username.txt"
launch_path = "Minecraft.Client.exe"


if not os.path.exists(f"{username_path}"):
    with open(f"{username_path}", "w") as file:
        file.write("Player")
    print("file created")
else:
    print("exists, skipping creation")




with open(f"{username_path}", "r") as file:
    username_value = file.read().strip()


window = QWidget()
window.setWindowTitle("4JMC Launcher")
window.resize(300, 200)
window.setWindowIcon(QIcon("media/favicon.png"))

title = QLabel("4JMC Launcher - By LuckiestPancake")

username = QLineEdit()
username.setPlaceholderText("Enter username")
username.setText(username_value) 

status = QLabel("Status: Ready")

launch_button = QPushButton("Launch")

def launch():
    name = username.text().strip()
    if name == "":
        name = "TPlayer"
    status.setText(f"Launching as {name}")
    
    os.startfile(launch_path)
    
    

launch_button.clicked.connect(launch)

save_button = QPushButton("Save Username")

def save_username():
    name = username.text().strip()
    if name == "":
        name = "Player"
    
    with open(f"{username_path}", "w") as file:
        file.write(name)
    
    status.setText(f"Saved username: {name}")

save_button.clicked.connect(save_username)


layout = QVBoxLayout()
layout.addWidget(title)
layout.addWidget(username)
layout.addWidget(save_button)
layout.addWidget(launch_button)
layout.addWidget(status)

window.setLayout(layout)

window.show()
sys.exit(app.exec())