# 📝 Enhanced Note-Taking App by DevKay

![Python](https://img.shields.io/badge/Python-3.7+-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) [![CC BY-NC 4.0](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)

**Enhanced Note-Taking App** is a feature-rich, tab-based, cross-platform GUI note manager built with Python’s `tkinter` library. Designed for writers, students, coders, and anyone who loves organized note-taking, this application brings powerful formatting tools, a live sidebar, color and font customization, and multi-tab editing all in one place.

---

## ✨ Key Features

1. **Tabbed Note Editing**

   * Create and manage multiple notes in independent tabs.
   * Autosave reminders for unsaved changes.

2. **Sidebar Note Explorer**

   * Browse and open existing `.txt` notes stored locally.
   * Search bar to filter notes by filename or keyword.

3. **Rich Text Toolbar**

   * Toggle **bold**, *italic*, and **underline** styles.
   * Select font family, size, text color, and background color.

4. **File Management**

   * Save, Save As (sanitized, timestamped filenames), Open, and Exit options.
   * Warns of unsaved changes to prevent data loss.

5. **Search & Highlight**

   * In-note content search with yellow highlighting of matches.

6. **Live Word Count**

   * Dynamic word and character count displayed in the status bar.

7. **Customizable UI**

   * Toggle visibility of sidebar, toolbar, and status bar.

8. **Safe Filename Handling**

   * Prevents invalid characters and naming collisions in filenames.

---

## 🛠️ Technologies & Dependencies

* **Language:** Python 3.7+
* **GUI Framework:** `tkinter`
* **Standard Libraries:**

  * `os`, `datetime`, `string`
  * `tkinter`, `tkinter.ttk`, `tkinter.filedialog`, `tkinter.messagebox`
  * `tkinter.simpledialog`, `tkinter.colorchooser`, `tkinter.font`

> No external packages required. Works out-of-the-box with a standard Python installation.

---

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/DharminJoshi/Enhanced-Note-Taking-App-By-DevKay.git
   ```
2. **Navigate to the project directory**

   ```bash
   cd Enhanced-Note-Taking-App-By-DevKay
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**

   ```bash
   python app.py
   ```

> You can rename `app.py` to match your main script file if needed.

---

## ▶️ Usage

* Use **File > New** to create a new note.
* Use **File > Open** to browse and open existing `.txt` files.
* Click toolbar buttons to apply formatting or change styling.
* Use **File > Save As** to save notes with a timestamped filename.
* Search within notes via the sidebar search bar.
* Toggle UI components from the **View** menu.

---

## 📂 Project Structure

```
Enhanced-Note-Taking-App-By-DevKay/
├── app.py                # Main application script
├── Notes/                # Auto-generated folder storing all notes
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── LICENSE               # License information
```

---

## 🤝 Contributing

Contributions are welcome! To suggest improvements or add features:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add <feature description>"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request describing your changes.

---

## 💼 License

This project, **Enhanced-Note-Taking-App-By-DevKay**, is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**. You are free to share, adapt, and modify the project for non-commercial purposes, provided that you give appropriate credit to the original creator (Dharmin Joshi/DevKay). Commercial use of this project is not permitted.

For more details, see the full license: [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

---

## © Copyright Disclaimer:

This project, **Enhanced-Note-Taking-App-By-DevKay**, is intended for educational and personal use only. All content, including code, images, and resources, are used under the principle of fair use. The project is a non-commercial, open-source endeavor created for learning purposes and is not associated with any official or commercial entity.

All trademarks, logos, and brand names mentioned or used in this project are the property of their respective owners. This project does not claim ownership of any of these trademarks, logos, or brand names.

The project is provided "as is" without any warranties, express or implied. The creator of this project is not responsible for any direct or indirect consequences arising from its use.

This project belongs to **DharminJoshi/DevKay** and is hosted on GitHub.

---

## ⚠️ Disclaimer

This application is provided "as is" for educational and personal use. The developer assumes no responsibility for data loss or misuse. Always back up important notes before use.

---

## 📬 Contact

For any queries, suggestions, or feedback, feel free to reach out:

- **Developer:** Dharmin Joshi / DevKay
- **Email:** info.dharmin@gmail.com
- **LinkedIn:** [https://www.linkedin.com/in/dharmin-joshi-3bab42232/](https://www.linkedin.com/in/dharmin-joshi-3bab42232/)
- **GitHub:** [https://github.com/DharminJoshi](https://github.com/DharminJoshi)

---

Thank you for using the Enhanced Note-Taking App! If you enjoy it, consider ⭐ starring the repo!
