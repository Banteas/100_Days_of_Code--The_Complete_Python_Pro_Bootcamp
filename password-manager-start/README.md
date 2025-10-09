# 🔐 Password Manager (Tkinter)

A simple and user-friendly **Password Manager** built with Python and Tkinter.
This app allows you to generate secure random passwords, copy them automatically to your clipboard, and save or search your credentials locally using a JSON file.

---

## 🚀 Features

* **Random Password Generator**
  Creates strong passwords with random letters, numbers, and symbols.

* **Clipboard Copy**
  Each generated password is automatically copied to your clipboard for quick use.

* **Credential Storage (JSON)**  
  Saves website, email, and password entries in a local `passwords.json` file.  
  Automatically creates the file if it doesn’t exist.

* **Search Function**  
  Instantly retrieves your saved credentials by website name.

* **Input Validation & Error Handling**
  Alerts you if required fields are missing, if the file doesn’t exist, or if a website isn’t found.


* **Simple GUI**
  Clean and intuitive interface built using Tkinter.

---

## 🧩 How It Works

1. Enter the **website** name and your **email/username**.  
2. Click **Generate Password** to create a strong random password.  
3. The password will appear in the field and be automatically copied to your clipboard.  
4. Click **Add** to save your credentials securely in `passwords.json`.  
5. Use **Search** to quickly retrieve stored credentials for a website.

---

## 🛠️ Technologies Used

* Python 3.x  
* Tkinter (for GUI)  
* `random` (for password generation)  
* `pyperclip` (for clipboard functionality)  
* `json` (for structured local data storage)

---

## 📂 File Structure

```
password-manager/
├── logo.png # App logo displayed in the GUI
├── passwords.json # Saved credentials file (auto-created)
├── main.py # Main program file
└── README.md # This file
```

---

## 🧠 Future Improvements

* Add a **delete or edit** feature for credentials  
* Add a **master password** for encryption and security  
* Improve UI design using `ttk` for themed widgets  
* Add a **password strength indicator**  
* Enable **multiple accounts per website**

---

## 💡 Example Output

```
Website: github.com
Email: banteas@hotmail.com
Password: &gL9$AqF12#n
```


