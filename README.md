# Fancy To-Do App

A modern and visually appealing To-Do application built using `customtkinter` and `tkcalendar`. This app allows users to manage tasks with due dates, priorities, and descriptions in a sleek, dark-themed interface.

![App Screenshot](screenshot.png) *(Optional: Add a screenshot of your app here)*

---

## Features

- **Task Management**: Add, delete, and mark tasks as completed.
- **Due Dates**: Select due dates using an integrated calendar.
- **Task Priorities**: Assign priorities (High, Medium, Low) to tasks.
- **Task Descriptions**: Add detailed descriptions to tasks.
- **Dark Theme**: A modern dark theme for a comfortable user experience.
- **Responsive Design**: The app is designed to be user-friendly and visually consistent.

---

## Requirements

To run this application, you need the following Python packages:

- `customtkinter`
- `tkcalendar`

You can install these dependencies using `pip`:

```bash
pip install customtkinter tkcalendar
```

---

## How to Run the App

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Run the `main.py` file:

```bash
python main.py
```

---

## Usage

1. **Add a Task**:
   - Enter the task name in the "Task name" field.
   - Add a description (optional) in the description box.
   - Select a due date using the calendar.
   - Choose a priority (High, Medium, Low).
   - Click the "Add Task" button.

2. **Mark a Task as Completed**:
   - Check the checkbox next to the task to mark it as completed.

3. **Delete a Task**:
   - Click the "✕" button next to the task to delete it.

4. **Clear Completed Tasks**:
   - Click the "Clear Completed" button to remove all completed tasks.

---

## Code Structure

- **Main Application Class**: `FancyTodoApp`
  - Initializes the GUI and sets up the layout.
  - Handles task creation, deletion, and completion.
- **Task Management**:
  - Tasks are stored in a list and displayed in a scrollable frame.
  - Each task includes a checkbox, description, priority, and delete button.
- **Styling**:
  - The app uses `customtkinter` for a modern look and feel.
  - Dark theme and blue color scheme are applied.

---

## Customization

- **Theme**: You can change the app's appearance by modifying the `ctk.set_appearance_mode()` and `ctk.set_default_color_theme()` functions.
- **Priority Colors**: Adjust the priority colors in the `colors` dictionary inside the `add_task` method.
- **Layout**: Modify the geometry, padding, and other layout parameters to suit your preferences.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Screenshots *(Optional)*

Add screenshots of your app here to give users a visual preview.

---

Enjoy using the Fancy To-Do App! 🚀

