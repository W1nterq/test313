from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit

class Second(QWidget):
    def __init__(self):
        super().__init__()
        self.set_UI()
        self.set_clicks()
        self.show()

    def set_UI(self):
        main_line = QVBoxLayout()
        self.setLayout(main_line)
        age_input = QLineEdit()
        p1_input = QLineEdit()    
        p2_input = QLineEdit()  
        p3_input = QLineEdit()  

        taimer_label = QLabel('Таймер')
        start_training_btn = QPushButton('Начинайте приседать')
        result_btn = QPushButton('Подсчитать результат')

        main_line.addWidget(taimer_label)
        main_line.addWidget(QLabel('Ваш возраст:'))
        main_line.addWidget(age_input)   
        main_line.addWidget(QLabel('Лягте на спину, измерьте пульс по таймеру. Результат введите в окно ввода:'))
        main_line.addWidget(p1_input)

        main_line.addWidget(QLabel('Начинайте приседать 30 раз в течение 45 чекунд. Вам поможет таймер.'))
        main_line.addWidget(start_training_btn)
        main_line.addWidget(QLabel('Лягте на спину, измеряйте пуль в течение первых 15 секунд. Результат введите в окно ввода:'))
        main_line.addWidget(p2_input)
        main_line.addWidget(QLabel('Лягте на спину, измеряйте пуль в течение последних 15 секунд. Результат введите в окно ввода:'))
        main_line.addWidget(p3_input)
        main_line.addWidget(result_btn)
    def set_clicks(self):
        pass