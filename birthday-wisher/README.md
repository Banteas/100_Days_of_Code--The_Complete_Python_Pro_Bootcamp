# 🎉 Birthday Wisher

A Python project that automatically sends personalized birthday emails to people listed in a CSV file.  

---

## 🧩 Features

- Reads a `birthdays.csv` file containing names, emails, and birthdays.
- Checks if anyone has a birthday today.
- Picks a random letter template and personalizes it with the person's name.
- Sends the email automatically via Gmail using an App Password.

---

## 📂 Project Structure

    birthday-wisher/
    ├── main.py # Main script to run the birthday wisher
    ├── birthdays.csv # CSV file with names, emails, and birthdays
    ├── letter_templates/ # Folder containing letter templates
    │ ├── letter_1.txt
    │ ├── letter_2.txt
    │ └── letter_3.txt
    └── .gitignore # Git ignore file

---

## ⚡ Setup Instructions

1. **Create Gmail App Password**  
   - Go to your Google Account → Security → App Passwords  
   - Generate a password for this project.  

2. **Add your credentials**  
   - In `main.py`, replace the placeholders with your email and App Password:  

```python
SENDER_EMAIL = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password_here"
```
3. Prepare your birthdays CSV

   - Example structure:

           | name | email                                       | year | month | day |
           | ---- | ------------------------------------------- | ---- | ----- | --- |
           | John | [john@example.com](mailto:john@example.com) | 1990 | 10    | 12  |
           | Jane | [jane@example.com](mailto:jane@example.com) | 1988 | 5     | 4   |

4. Add letter templates

- Create letter_templates/letter_1.txt, letter_2.txt, letter_3.txt

- Include [NAME] in your template where the recipient's name should appear.

5. Run the script
````
python main.py
````
The script will check if anyone has a birthday today and send the email automatically.


## 🚀 Future Improvements

- Automatically send emails to multiple people if several birthdays are on the same day.

- Integrate with GitHub Actions to run daily automatically.

- Add more templates or HTML email support.
