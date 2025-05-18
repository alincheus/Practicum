import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt6.QtCore import QSettings

# 🔹 Словарь локализации
translations = {
    "ru": {
        "title": "Калькулятор",
        "add": "Сложить",
        "subtract": "Вычесть",
        "multiply": "Умножить",
        "divide": "Делить",
        "history": "История вычислений",
        "settings": "Настройки",
        "theme": "Выбрать тему",
        "language": "Переключить язык"
    },
    "en": {
        "title": "Calculator",
        "add": "Add",
        "subtract": "Subtract",
        "multiply": "Multiply",
        "divide": "Divide",
        "history": "History",
        "settings": "Settings",
        "theme": "Choose Theme",
        "language": "Switch Language"
    }
}

# 🔹 Доступные темы
themes = {
    "Светлая": "background-color: white; color: black;",
    "Темная": "background-color: black; color: white;",
    "Синяя": "background-color: #2B65EC; color: white;"
}

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        self.settings = QSettings("MyApp", "Calculator")
        self.language = self.settings.value("language", "ru")
        self.theme = self.settings.value("theme", themes["Светлая"])  # 🔹 Дефолтная тема

        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Введите число 1")
        layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Введите число 2")
        layout.addWidget(self.input2)

        self.result_label = QLabel("Результат: ")
        layout.addWidget(self.result_label)

        self.btn_add = QPushButton(translations[self.language]["add"])
        self.btn_subtract = QPushButton(translations[self.language]["subtract"])
        self.btn_multiply = QPushButton(translations[self.language]["multiply"])
        self.btn_divide = QPushButton(translations[self.language]["divide"])

        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_subtract)
        layout.addWidget(self.btn_multiply)
        layout.addWidget(self.btn_divide)

        self.btn_history = QPushButton(translations[self.language]["history"])
        self.btn_settings = QPushButton(translations[self.language]["settings"])
        layout.addWidget(self.btn_history)
        layout.addWidget(self.btn_settings)

        self.btn_history.clicked.connect(self.show_history_window)
        self.btn_settings.clicked.connect(self.show_settings_window)

        self.setLayout(layout)

        self.history_window = HistoryWindow()
        self.settings_window = SettingsWindow(self)

        self.load_theme()
        self.apply_language()

    def show_history_window(self):
        self.history_window.show()

    def show_settings_window(self):
        self.settings_window.show()

    def apply_language(self):
        self.setWindowTitle(translations[self.language]["title"])
        self.btn_add.setText(translations[self.language]["add"])
        self.btn_subtract.setText(translations[self.language]["subtract"])
        self.btn_multiply.setText(translations[self.language]["multiply"])
        self.btn_divide.setText(translations[self.language]["divide"])
        self.btn_history.setText(translations[self.language]["history"])
        self.btn_settings.setText(translations[self.language]["settings"])

    def apply_theme(self, theme):
        self.setStyleSheet(theme)
        self.history_window.setStyleSheet(theme)
        self.settings_window.setStyleSheet(theme)
        self.settings.setValue("theme", theme)

    def load_theme(self):
        self.theme = self.settings.value("theme", themes["Светлая"])
        self.apply_theme(self.theme)


class HistoryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("История вычислений")
        self.resize(300, 200)

        layout = QVBoxLayout(self)
        self.history_label = QLabel("История операций:")
        layout.addWidget(self.history_label)

        self.history_data = []
        self.history_label.setText("История пуста.")

        self.setLayout(layout)

    def add_to_history(self, entry):
        self.history_data.append(entry)
        self.history_label.setText("\n".join(self.history_data[-10:]))  # Показываем последние 10 операций


class SettingsWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Настройки")
        self.resize(300, 200)

        layout = QVBoxLayout(self)

        self.theme_label = QLabel(translations[self.main_window.language]["theme"])
        layout.addWidget(self.theme_label)

        self.theme_selector = QComboBox()
        self.theme_selector.addItems(themes.keys())
        layout.addWidget(self.theme_selector)

        self.theme_btn = QPushButton("Применить тему")
        layout.addWidget(self.theme_btn)
        self.theme_btn.clicked.connect(self.toggle_theme)

        self.lang_btn = QPushButton(translations[self.main_window.language]["language"])
        layout.addWidget(self.lang_btn)
        self.lang_btn.clicked.connect(self.toggle_language)

        self.setLayout(layout)

    def toggle_theme(self):
        selected_theme = self.theme_selector.currentText()
        new_theme = themes[selected_theme]
        self.main_window.apply_theme(new_theme)

    def toggle_language(self):
        self.main_window.language = "en" if self.main_window.language == "ru" else "ru"
        self.main_window.settings.setValue("language", self.main_window.language)
        self.main_window.apply_language()


def validate_input(window):
    try:
        num1 = float(window.input1.text())
        num2 = float(window.input2.text())
        return num1, num2
    except ValueError:
        window.result_label.setText("Ошибка: введите числа!")
        return None, None

def calculate(operation, window):
    num1, num2 = validate_input(window)
    if num1 is None:
        return

    if operation == "сложение":
        result = num1 + num2
    elif operation == "вычитание":
        result = num1 - num2
    elif operation == "умножение":
        result = num1 * num2
    elif operation == "деление":
        result = num1 / num2 if num2 != 0 else "Ошибка (деление на 0)"

    window.result_label.setText(f"Результат: {result}")
    window.history_window.add_to_history(f"{num1} {operation} {num2} = {result}")


app = QApplication(sys.argv)
window = CalculatorWindow()

window.btn_add.clicked.connect(lambda: calculate("сложение", window))
window.btn_subtract.clicked.connect(lambda: calculate("вычитание", window))
window.btn_multiply.clicked.connect(lambda: calculate("умножение", window))
window.btn_divide.clicked.connect(lambda: calculate("деление", window))

window.show()
sys.exit(app.exec())
