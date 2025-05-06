import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, simpledialog, colorchooser, font
import os
from datetime import datetime
import string

class EnhancedNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Note-Taking App by DevKay")
        self.root.geometry("1000x700")

        # Directory to store notes
        self.notes_directory = os.path.join(os.path.dirname(__file__), "Notes")
        self.ensure_notes_directory()

        # Initialize filename as None
        self.filename = None

        # Initialize font settings
        self.current_font_family = "Arial"
        self.current_font_size = 12

        # Create the main UI components
        self.create_menu()
        self.create_toolbar()
        self.create_sidebar()
        self.create_tabs()
        self.create_status_bar()

    def ensure_notes_directory(self):
        """Ensure that the notes directory exists; create it if it doesn't."""
        if not os.path.exists(self.notes_directory):
            try:
                os.makedirs(self.notes_directory)
                print(f"Created notes directory at {self.notes_directory}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not create notes directory: {e}")

    def create_menu(self):
        """Create the menu bar with File, Edit, View, and Help menus."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q", command=self.exit_app)

        # Edit Menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=lambda: self.current_text_widget.event_generate("<<Undo>>"))
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=lambda: self.current_text_widget.event_generate("<<Redo>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: self.current_text_widget.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: self.current_text_widget.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: self.current_text_widget.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=lambda: self.current_text_widget.tag_add("sel", "1.0", "end"))

        # View Menu
        view_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="View", menu=view_menu)

        view_menu.add_command(label="Toggle Sidebar", command=self.toggle_sidebar)
        view_menu.add_command(label="Toggle Toolbar", command=self.toggle_toolbar)
        view_menu.add_command(label="Toggle Status Bar", command=self.toggle_status_bar)

        # Help Menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        help_menu.add_command(label="About", command=self.show_about)

        # Bind shortcuts
        self.bind_shortcuts()

    def create_toolbar(self):
        """Create a toolbar with buttons for common actions and formatting."""
        self.toolbar_visible = True
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # New Button
        new_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        new_btn = tk.Button(toolbar, text="New", image=new_icon, compound=tk.LEFT, command=self.new_file)
        new_btn.image = new_icon
        new_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Open Button
        open_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        open_btn = tk.Button(toolbar, text="Open", image=open_icon, compound=tk.LEFT, command=self.open_file)
        open_btn.image = open_icon
        open_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Save Button
        save_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        save_btn = tk.Button(toolbar, text="Save", image=save_icon, compound=tk.LEFT, command=self.save_file)
        save_btn.image = save_icon
        save_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Separator
        sep = ttk.Separator(toolbar, orient='vertical')
        sep.pack(side=tk.LEFT, fill='y', padx=5)

        # Bold Button
        bold_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        bold_btn = tk.Button(toolbar, text="Bold", image=bold_icon, compound=tk.LEFT, command=self.make_bold)
        bold_btn.image = bold_icon
        bold_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Italic Button
        italic_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        italic_btn = tk.Button(toolbar, text="Italic", image=italic_icon, compound=tk.LEFT, command=self.make_italic)
        italic_btn.image = italic_icon
        italic_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Underline Button
        underline_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        underline_btn = tk.Button(toolbar, text="Underline", image=underline_icon, compound=tk.LEFT, command=self.make_underline)
        underline_btn.image = underline_icon
        underline_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Separator
        sep2 = ttk.Separator(toolbar, orient='vertical')
        sep2.pack(side=tk.LEFT, fill='y', padx=5)

        # Font Family Dropdown
        font_families = list(font.families())
        self.font_family_var = tk.StringVar()
        self.font_family_var.set(self.current_font_family)
        font_family_menu = ttk.Combobox(toolbar, textvariable=self.font_family_var, values=font_families, state='readonly')
        font_family_menu.bind("<<ComboboxSelected>>", self.change_font_family)
        font_family_menu.pack(side=tk.LEFT, padx=5)
        font_family_menu.set(self.current_font_family)

        # Font Size Dropdown
        font_sizes = list(range(8, 73, 2))
        self.font_size_var = tk.IntVar()
        self.font_size_var.set(self.current_font_size)
        font_size_menu = ttk.Combobox(toolbar, textvariable=self.font_size_var, values=font_sizes, state='readonly', width=3)
        font_size_menu.bind("<<ComboboxSelected>>", self.change_font_size)
        font_size_menu.pack(side=tk.LEFT, padx=5)

        # Text Color Button
        color_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        color_btn = tk.Button(toolbar, text="Text Color", image=color_icon, compound=tk.LEFT, command=self.change_text_color)
        color_btn.image = color_icon
        color_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # Background Color Button
        bg_color_icon = tk.PhotoImage(width=1, height=1)  # Placeholder for icon
        bg_color_btn = tk.Button(toolbar, text="Bg Color", image=bg_color_icon, compound=tk.LEFT, command=self.change_bg_color)
        bg_color_btn.image = bg_color_icon
        bg_color_btn.pack(side=tk.LEFT, padx=2, pady=2)

    def create_sidebar(self):
        """Create a sidebar listing existing notes."""
        self.sidebar_visible = True
        self.sidebar = tk.Frame(self.root, bd=1, relief=tk.SUNKEN, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        # Search Entry
        search_frame = tk.Frame(self.sidebar)
        search_frame.pack(padx=5, pady=5, fill=tk.X)

        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side=tk.LEFT)

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        search_entry.bind("<Return>", self.search_notes)

        search_btn = tk.Button(search_frame, text="Go", command=self.search_notes)
        search_btn.pack(side=tk.LEFT, padx=2)

        # Notes Listbox
        self.notes_listbox = tk.Listbox(self.sidebar)
        self.notes_listbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.notes_listbox.bind("<Double-Button-1>", self.open_selected_note)

        self.populate_notes_listbox()

    def create_tabs(self):
        """Create a tabbed interface for multiple notes."""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Initialize first tab
        self.add_new_tab()

    def create_status_bar(self):
        """Create a status bar at the bottom of the application."""
        self.status_bar_visible = True
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = tk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def add_new_tab(self, title="Untitled"):
        """Add a new tab with a text widget."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=title)
        self.notebook.select(tab)

        # Create Text Widget with Scrollbar in the tab
        text_area = tk.Text(tab, undo=True, wrap='word', font=(self.current_font_family, self.current_font_size))
        text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(tab, command=text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_area.config(yscrollcommand=scrollbar.set)

        # Bind events to update status bar (e.g., word count)
        text_area.bind("<KeyRelease>", self.update_status_bar)

    def get_current_tab(self):
        """Get the current tab and its text widget."""
        current_tab = self.notebook.select()
        if not current_tab:
            return None, None
        tab = self.notebook.nametowidget(current_tab)
        text_widget = tab.winfo_children()[0]
        return tab, text_widget

    def bind_shortcuts(self):
        """Bind keyboard shortcuts to respective functions."""
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-N>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-O>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-S>", lambda event: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda event: self.save_as())
        self.root.bind("<Control-q>", lambda event: self.exit_app())
        self.root.bind("<Control-Q>", lambda event: self.exit_app())
        self.root.bind("<Control-a>", lambda event: self.select_all())
        self.root.bind("<Control-A>", lambda event: self.select_all())
        self.root.bind("<Control-f>", lambda event: self.search_notes())
        self.root.bind("<Control-F>", lambda event: self.search_notes())

    def new_file(self):
        """Create a new note in a new tab."""
        if self.confirm_discard_changes():
            self.add_new_tab()

    def open_file(self):
        """Open an existing note from the notes directory in a new tab."""
        file_path = filedialog.askopenfilename(
            initialdir=self.notes_directory,
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    content = file.read()
                filename = os.path.basename(file_path)
                if self.is_duplicate_filename(filename):
                    messagebox.showwarning("Duplicate Filename",
                                           f"A file named '{filename}' is already open in a tab.")
                    return
                self.add_new_tab(title=filename)
                tab, text_widget = self.get_current_tab()
                text_widget.insert(tk.END, content)
                text_widget.edit_modified(False)
                self.update_status_bar()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        """Save the current note. If it's a new note, invoke Save As."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            return
        content = text_widget.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Empty Content", "Cannot save an empty note.")
            return

        filename = self.notebook.tab(tab, "text")
        if filename == "Untitled":
            self.save_as()
        else:
            file_path = os.path.join(self.notes_directory, filename)
            try:
                with open(file_path, "w", encoding='utf-8') as file:
                    file.write(content)
                messagebox.showinfo("Saved", f"File '{filename}' saved successfully.")
                self.status_var.set(f"Saved: {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def save_as(self):
        """Save the current note with a new name based on timestamp and title."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            return
        content = text_widget.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Empty Content", "Cannot save an empty note.")
            return

        # Prompt the user for a note title
        note_title = simpledialog.askstring("Save As", "Enter a title for your note:")
        if not note_title:
            messagebox.showwarning("Input Required", "Note title cannot be empty.")
            return

        # Sanitize the note title
        note_title_sanitized = self.sanitize_filename(note_title)

        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Construct the filename
        filename = f"{timestamp}_{note_title_sanitized}.txt"

        # Check for case-insensitive duplicate filenames
        if self.is_duplicate_filename(filename):
            messagebox.showwarning("Duplicate Filename",
                                   f"A file named '{filename}' already exists. Please choose a different title.")
            return

        # Full path
        file_path = os.path.join(self.notes_directory, filename)

        try:
            with open(file_path, "w", encoding='utf-8') as file:
                file.write(content)
            self.notebook.tab(tab, text=filename)
            messagebox.showinfo("Saved", f"File '{filename}' saved successfully.")
            self.status_var.set(f"Saved: {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

    def sanitize_filename(self, name):
        """Remove or replace characters that are invalid in filenames."""
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        sanitized = ''.join(c if c in valid_chars else '_' for c in name)
        return sanitized

    def is_duplicate_filename(self, filename):
        """
        Check if a file with the same name (case-insensitive) already exists in the notes directory.
        Returns True if a duplicate exists, False otherwise.
        """
        existing_files = os.listdir(self.notes_directory)
        # Normalize existing filenames to lower case for case-insensitive comparison
        existing_files_lower = [f.lower() for f in existing_files]
        return filename.lower() in existing_files_lower

    def toggle_sidebar(self):
        """Toggle the visibility of the sidebar."""
        if self.sidebar_visible:
            self.sidebar.pack_forget()
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
            self.sidebar_visible = True

    def toggle_toolbar(self):
        """Toggle the visibility of the toolbar."""
        if self.toolbar_visible:
            for widget in self.root.pack_slaves():
                if isinstance(widget, tk.Frame) and widget != self.sidebar and widget != self.notebook and widget != self.status_bar:
                    widget.pack_forget()
                    break
            self.toolbar_visible = False
        else:
            self.create_toolbar()
            self.toolbar_visible = True

    def toggle_status_bar(self):
        """Toggle the visibility of the status bar."""
        if self.status_bar_visible:
            self.status_bar.pack_forget()
            self.status_bar_visible = False
        else:
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
            self.status_bar_visible = True

    def show_about(self):
        """Display the About dialog."""
        messagebox.showinfo("About", "Enhanced Note-Taking App\nDeveloped By DevKay")

    def make_bold(self):
        """Toggle bold formatting."""
        self.toggle_text_style("bold")

    def make_italic(self):
        """Toggle italic formatting."""
        self.toggle_text_style("italic")

    def make_underline(self):
        """Toggle underline formatting."""
        self.toggle_text_style("underline")

    def toggle_text_style(self, style):
        """Toggle a text style (bold, italic, underline) in the current text widget."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            return

        current_tags = text_widget.tag_names("sel.first")
        if style in current_tags:
            text_widget.tag_remove(style, "sel.first", "sel.last")
        else:
            text_widget.tag_add(style, "sel.first", "sel.last")

        # Configure the tag if not already configured
        if not text_widget.tag_cget(style, "font"):
            current_font = font.Font(font=text_widget['font'])
            if style == "bold":
                current_font.configure(weight="bold")
            elif style == "italic":
                current_font.configure(slant="italic")
            elif style == "underline":
                current_font.configure(underline=True)
            text_widget.tag_configure(style, font=current_font)

    def change_font_family(self, event=None):
        """Change the font family of the current text widget."""
        self.current_font_family = self.font_family_var.get()
        self.apply_font_changes()

    def change_font_size(self, event=None):
        """Change the font size of the current text widget."""
        self.current_font_size = self.font_size_var.get()
        self.apply_font_changes()

    def apply_font_changes(self):
        """Apply font family and size changes to the current text widget."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            return
        text_widget.configure(font=(self.current_font_family, self.current_font_size))
        # Update all tags to use the new font
        for tag in text_widget.tag_names():
            if tag in ["bold", "italic", "underline"]:
                self.toggle_text_style(tag)

    def change_text_color(self):
        """Change the color of the selected text."""
        color = colorchooser.askcolor(title="Choose text color")
        if color[1]:
            tab, text_widget = self.get_current_tab()
            if not text_widget:
                return
            try:
                text_widget.tag_add("colored", "sel.first", "sel.last")
                text_widget.tag_configure("colored", foreground=color[1])
            except tk.TclError:
                messagebox.showwarning("Selection Error", "Please select text to change its color.")

    def change_bg_color(self):
        """Change the background color of the text widget."""
        color = colorchooser.askcolor(title="Choose background color")
        if color[1]:
            tab, text_widget = self.get_current_tab()
            if not text_widget:
                return
            text_widget.configure(bg=color[1])

    def select_all(self):
        """Select all text in the current text widget."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            return
        text_widget.tag_add("sel", "1.0", "end")

    def search_notes(self, event=None):
        """Search for text within the current note."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            return
        search_term = self.search_var.get()
        if not search_term:
            messagebox.showwarning("Input Required", "Please enter a search term.")
            return

        # Remove previous search highlights
        text_widget.tag_remove("search", "1.0", tk.END)

        # Find all occurrences of the search term
        idx = "1.0"
        while True:
            idx = text_widget.search(search_term, idx, nocase=1, stopindex=tk.END)
            if not idx:
                break
            end_idx = f"{idx}+{len(search_term)}c"
            text_widget.tag_add("search", idx, end_idx)
            idx = end_idx

        # Configure the search tag
        text_widget.tag_configure("search", background="yellow")

        if not text_widget.tag_ranges("search"):
            messagebox.showinfo("Search", f"No matches found for '{search_term}'.")

    def populate_notes_listbox(self):
        """Populate the sidebar listbox with existing notes."""
        self.notes_listbox.delete(0, tk.END)
        for file in os.listdir(self.notes_directory):
            if file.lower().endswith(".txt"):
                self.notes_listbox.insert(tk.END, file)

    def open_selected_note(self, event):
        """Open the note selected from the sidebar listbox."""
        selected = self.notes_listbox.curselection()
        if selected:
            filename = self.notes_listbox.get(selected[0])
            file_path = os.path.join(self.notes_directory, filename)
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    content = file.read()
                # Check if the note is already open
                for tab_id in self.notebook.tabs():
                    if self.notebook.tab(tab_id, "text").lower() == filename.lower():
                        self.notebook.select(tab_id)
                        return
                # Add a new tab
                self.add_new_tab(title=filename)
                tab, text_widget = self.get_current_tab()
                text_widget.insert(tk.END, content)
                text_widget.edit_modified(False)
                self.update_status_bar()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def update_status_bar(self, event=None):
        """Update the status bar with the current file name and word count."""
        tab, text_widget = self.get_current_tab()
        if not text_widget:
            self.status_var.set("Ready")
            return
        filename = self.notebook.tab(tab, "text")
        content = text_widget.get(1.0, tk.END)
        words = len(content.split())
        self.status_var.set(f"File: {filename} | Words: {words}")

    def exit_app(self):
        """Exit the application after confirming to save changes."""
        if self.confirm_discard_changes():
            self.root.destroy()

    def confirm_discard_changes(self):
        """
        Confirm with the user to discard changes if there are unsaved changes.
        Returns True if it's okay to proceed, False otherwise.
        """
        unsaved_tabs = []
        for tab_id in self.notebook.tabs():
            tab = self.notebook.nametowidget(tab_id)
            text_widget = tab.winfo_children()[0]
            if text_widget.edit_modified():
                filename = self.notebook.tab(tab_id, "text")
                unsaved_tabs.append(filename)

        if unsaved_tabs:
            response = messagebox.askyesnocancel("Save Changes",
                                                 f"Do you want to save changes to {', '.join(unsaved_tabs)} before exiting?")
            if response:  # Yes, save changes
                for tab_id in self.notebook.tabs():
                    tab = self.notebook.nametowidget(tab_id)
                    text_widget = tab.winfo_children()[0]
                    if text_widget.edit_modified():
                        self.notebook.select(tab_id)
                        self.save_file()
                return True
            elif response is False:  # No, discard changes
                return True
            else:  # Cancel
                return False
        return True

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = EnhancedNoteApp(root)
    root.mainloop()
