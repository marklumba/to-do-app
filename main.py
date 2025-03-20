import customtkinter as ctk
from tkcalendar import Calendar
from datetime import datetime

class FancyTodoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fancy To-Do App")
        self.geometry("700x800")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title
        self.title_label = ctk.CTkLabel(self.main_frame, text="Task Master", 
                                      font=("Roboto", 24, "bold"))
        self.title_label.pack(pady=10)

        # Calendar
        self.cal = Calendar(self.main_frame, selectmode="day", 
                          background="#2b2b2b", foreground="white")
        self.cal.pack(pady=10)

        # Task entry
        self.task_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Task name", 
                                     width=400, corner_radius=8)
        self.task_entry.pack(pady=5)

        # Description entry
        self.desc_entry = ctk.CTkTextbox(self.main_frame, height=60, width=400, 
                                       corner_radius=8)
        self.desc_entry.pack(pady=5)

        # Priority and Add frame
        self.control_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.control_frame.pack(pady=5)

        self.priority_var = ctk.StringVar(value="Medium")
        self.priority_menu = ctk.CTkOptionMenu(self.control_frame, 
                                             values=["High", "Medium", "Low"],
                                             variable=self.priority_var,
                                             corner_radius=8)
        self.priority_menu.pack(side="left", padx=5)

        self.add_button = ctk.CTkButton(self.control_frame, text="Add Task", 
                                      command=self.add_task, corner_radius=8)
        self.add_button.pack(side="left", padx=5)

        # Task list
        self.task_frame = ctk.CTkScrollableFrame(self.main_frame, width=600, 
                                               height=300, corner_radius=10)
        self.task_frame.pack(pady=10, fill="both", expand=True)

        # Clear button
        self.clear_button = ctk.CTkButton(self.main_frame, text="Clear Completed", 
                                        command=self.clear_completed, corner_radius=8)
        self.clear_button.pack(pady=10)

        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get()
        desc_text = self.desc_entry.get("1.0", "end-1c")
        due_date = self.cal.get_date()
        priority = self.priority_var.get()

        if task_text:
            task_container = ctk.CTkFrame(self.task_frame, corner_radius=5)
            task_container.pack(pady=5, padx=10, fill="x")

            # Checkbox and text
            checkbox = ctk.CTkCheckBox(task_container, 
                                     text=f"{task_text} (Due: {due_date})")
            checkbox.pack(side="top", padx=5, pady=2, anchor="w")

            # Description
            desc_label = ctk.CTkLabel(task_container, 
                                    text=desc_text if desc_text else "No description",
                                    font=("Roboto", 12), wraplength=500)
            desc_label.pack(side="top", padx=5, pady=2, anchor="w")

            # Priority
            colors = {"High": "#ff5555", "Medium": "#ffff55", "Low": "#55ff55"}
            priority_label = ctk.CTkLabel(task_container, text=priority, 
                                        text_color=colors[priority])
            priority_label.pack(side="left", padx=5)

            # Delete button
            delete_btn = ctk.CTkButton(task_container, text="✕", width=30, 
                                     command=lambda: self.delete_task(task_container),
                                     corner_radius=5)
            delete_btn.pack(side="right")

            self.tasks.append((task_container, checkbox))
            self.task_entry.delete(0, "end")
            self.desc_entry.delete("1.0", "end")

    def delete_task(self, task_container):
        for task in self.tasks:
            if task[0] == task_container:
                task_container.destroy()
                self.tasks.remove(task)
                break

    def clear_completed(self):
        for task_container, checkbox in self.tasks[:]:
            if checkbox.get():
                task_container.destroy()
                self.tasks.remove((task_container, checkbox))

if __name__ == "__main__":
    app = FancyTodoApp()
    app.mainloop()