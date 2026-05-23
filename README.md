# 📁 Automated Smart File Organizer

A lightning-fast, zero-setup Python script that automatically scans a messy directory (like your Desktop or Downloads folder) and instantly sorts files into neat, structured categories based on their extensions.

![Python Version](https://shields.io)
![License](https://shields.io)

---

## ✨ Features

- **Instant Automation:** Sorts hundreds of cluttered files in less than a second.
- **Pure Python:** Uses 100% built-in libraries (`pathlib` and `shutil`). **No `pip install` required!**
- **Smart Categorization:** Automatically detects and moves:
  - 🖼️ **Images:** `.jpg`, `.png`, `.gif`, `.svg`
  - 📄 **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
  - 🎬 **Videos:** `.mp4`, `.mkv`, `.mov`
  - 🎵 **Audio:** `.mp3`, `.wav`
  - 📦 **Archives:** `.zip`, `.rar`, `.7z`

---

## 🚀 How To Run It

### 1. Clone the repository
```bash
git clone https://github.com
cd python-desktop-file-organizer
```

### 2. Run the script
```bash
python file_organizer.py
```

### 3. Enter the path
Simply paste the full path of the messy folder you want to clean up when prompted!

---

## 🛠️ Customization

Want to add your own categories? Open `file_organizer.py` and easily update the `FILE_CATEGORIES` dictionary:

```python
FILE_CATEGORIES = {
    "Coding_Projects": [".py", ".js", ".html", ".css"],
    "Design_Files": [".psd", ".ai", ".fig"]
}
```

---

## 🤝 Contributing

Feel free to fork this project, open issues, or submit pull requests with improvements (like adding a graphical interface!). 

*If this script saved you time, please drop a ⭐ on this repository!*
