# 🔐 Password Manager (Tkinter)

A simple and user-friendly **Password Manager** built with Python and Tkinter.
This app allows you to generate secure random passwords, copy them automatically to your clipboard, and save your credentials locally for easy access.

---

## 🚀 Features

* **Random Password Generator**
  Creates strong passwords with random letters, numbers, and symbols.

* **Clipboard Copy**
  Each generated password is automatically copied to your clipboard for quick use.

* **Credential Storage**
  Saves website, email, and password entries in a local `password.txt` file.

* **Input Validation**
  Alerts you if required fields (website or password) are missing.

* **Simple GUI**
  Built using Tkinter, with a clean and minimal interface.

---

## 🧩 How It Works

1. Enter the **website** name and your **email/username**.
2. Click **Generate Password** to create a secure password.
3. The password will appear in the entry box and be copied to your clipboard automatically.
4. Click **Add** to save your credentials to `password.txt`.

---

## 🛠️ Technologies Used

* Python 3.x
* Tkinter (GUI framework)
* `random` module (for password generation)
* `pyperclip` (for clipboard functionality)

---

## 📂 File Structure

```
password-manager/
├── logo.png          # App logo displayed in the GUI
├── password.txt      # Stored credentials file
├── main.py           # Main program file
└── README.md         # This file
```

---

## 🧠 Future Improvements

* Add a **search function** to look up saved credentials.
* Save data in **JSON format** instead of plain text.
* Implement **password update/delete** features.
* Add **encryption** for stored data.

---

## 💡 Example Output

```
Website: github.com
Email: banteas@hotmail.com
Password: &gL9$AqF12#n
```

