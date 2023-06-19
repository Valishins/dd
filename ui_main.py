from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FIO = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FIO.setFont(font)
        self.FIO.setObjectName("FIO")
        self.FIO.addItem("")
        self.horizontalLayout.addWidget(self.FIO)
        self.dnev = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dnev.setFont(font)
        self.dnev.setObjectName("dnev")
        self.horizontalLayout.addWidget(self.dnev)
        self.but_ktp = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.but_ktp.setFont(font)
        self.but_ktp.setObjectName("but_ktp")
        self.horizontalLayout.addWidget(self.but_ktp)
        self.but_time = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.but_time.setFont(font)
        self.but_time.setObjectName("but_time")
        self.horizontalLayout.addWidget(self.but_time)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table = QtWidgets.QWidget(self.page1)
        self.table.setObjectName("table")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.table)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addWidget(self.table)
        self.labels = QtWidgets.QWidget(self.page1)
        self.labels.setObjectName("labels")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.labels)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.labels)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.month_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.month_2.setFont(font)
        self.month_2.setAlignment(QtCore.Qt.AlignCenter)
        self.month_2.setObjectName("month_2")
        self.horizontalLayout_2.addWidget(self.month_2)
        self.number_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_2.setFont(font)
        self.number_2.setAlignment(QtCore.Qt.AlignCenter)
        self.number_2.setObjectName("number_2")
        self.horizontalLayout_2.addWidget(self.number_2)
        self.item_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.item_2.setFont(font)
        self.item_2.setAlignment(QtCore.Qt.AlignCenter)
        self.item_2.setObjectName("item_2")
        self.horizontalLayout_2.addWidget(self.item_2)
        self.group_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.group_2.setFont(font)
        self.group_2.setAlignment(QtCore.Qt.AlignCenter)
        self.group_2.setObjectName("group_2")
        self.horizontalLayout_2.addWidget(self.group_2)
        self.classes_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classes_2.setFont(font)
        self.classes_2.setAlignment(QtCore.Qt.AlignCenter)
        self.classes_2.setObjectName("classes_2")
        self.horizontalLayout_2.addWidget(self.classes_2)
        self.week_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.week_2.setFont(font)
        self.week_2.setAlignment(QtCore.Qt.AlignCenter)
        self.week_2.setObjectName("week_2")
        self.horizontalLayout_2.addWidget(self.week_2)
        self.who_2 = QtWidgets.QLabel(self.labels)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.who_2.setFont(font)
        self.who_2.setAlignment(QtCore.Qt.AlignCenter)
        self.who_2.setObjectName("who_2")
        self.horizontalLayout_2.addWidget(self.who_2)
        self.verticalLayout_2.addWidget(self.labels)
        self.combos = QtWidgets.QWidget(self.page1)
        self.combos.setObjectName("combos")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.combos)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.id = QtWidgets.QLabel(self.combos)
        self.id.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.id.setAlignment(QtCore.Qt.AlignCenter)
        self.id.setObjectName("id")
        self.horizontalLayout_3.addWidget(self.id)
        self.month_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.month_1.setFont(font)
        self.month_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.month_1.setObjectName("month_1")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.month_1.addItem("")
        self.horizontalLayout_3.addWidget(self.month_1)
        self.number_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.number_1.setFont(font)
        self.number_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_1.setObjectName("number_1")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.number_1.addItem("")
        self.horizontalLayout_3.addWidget(self.number_1)
        self.item_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.item_1.setFont(font)
        self.item_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_1.setObjectName("item_1")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.item_1.addItem("")
        self.horizontalLayout_3.addWidget(self.item_1)
        self.group_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.group_1.setFont(font)
        self.group_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.group_1.setObjectName("group_1")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.group_1.addItem("")
        self.horizontalLayout_3.addWidget(self.group_1)
        self.classes_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.classes_1.setFont(font)
        self.classes_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.classes_1.setObjectName("classes_1")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.classes_1.addItem("")
        self.horizontalLayout_3.addWidget(self.classes_1)
        self.week_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.week_1.setFont(font)
        self.week_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.week_1.setObjectName("week_1")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.week_1.addItem("")
        self.horizontalLayout_3.addWidget(self.week_1)
        self.who_1 = QtWidgets.QComboBox(self.combos)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.who_1.setFont(font)
        self.who_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.who_1.setObjectName("who_1")
        self.who_1.addItem("")
        self.who_1.addItem("")
        self.who_1.addItem("")
        self.horizontalLayout_3.addWidget(self.who_1)
        self.verticalLayout_2.addWidget(self.combos)
        self.tableView = QtWidgets.QTableView(self.page1)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.buttons = QtWidgets.QWidget(self.page1)
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.openes = QtWidgets.QPushButton(self.buttons)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openes.setFont(font)
        self.openes.setObjectName("openes")
        self.horizontalLayout_5.addWidget(self.openes)
        self.exchange = QtWidgets.QPushButton(self.buttons)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exchange.setFont(font)
        self.exchange.setObjectName("exchange")
        self.horizontalLayout_5.addWidget(self.exchange)
        self.repear = QtWidgets.QPushButton(self.buttons)
        self.repear.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.repear.setFont(font)
        self.repear.setObjectName("repear")
        self.horizontalLayout_5.addWidget(self.repear)
        self.verticalLayout_2.addWidget(self.buttons)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.stackedWidget.addWidget(self.page2)
        self.tableView_2 = QtWidgets.QTableView(self.page2)
        self.tableView_2.setGeometry(QtCore.QRect(10, 10, 800, 700))
        self.tableView_2.setObjectName("tableView_2")
        self.open_xl = QtWidgets.QPushButton(self.page2)
        self.open_xl.setGeometry(QtCore.QRect(10, 600, 211, 30))
        self.open_xl.setObjectName("open_xl")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.stackedWidget.addWidget(self.page3)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.FIO.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учёт"))
        self.FIO.setCurrentText(_translate("MainWindow", "Стерлядева Л.В."))
        self.FIO.setItemText(0, _translate("MainWindow", "Стерлядева Л.В."))
        self.dnev.setText(_translate("MainWindow", "Главная"))
        self.but_ktp.setText(_translate("MainWindow", "Дневник"))
        self.but_time.setText(_translate("MainWindow", "Часы"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.month_2.setText(_translate("MainWindow", "Месяц"))
        self.number_2.setText(_translate("MainWindow", "№ Пары"))
        self.item_2.setText(_translate("MainWindow", "Предмет"))
        self.group_2.setText(_translate("MainWindow", "Группа"))
        self.classes_2.setText(_translate("MainWindow", "Вид занятия"))
        self.week_2.setText(_translate("MainWindow", "Неделя"))
        self.who_2.setText(_translate("MainWindow", "Кто"))
        self.id.setText(_translate("MainWindow", "ID"))
        self.month_1.setItemText(0, _translate("MainWindow", "Все"))
        self.month_1.setItemText(1, _translate("MainWindow", "Сентябрь"))
        self.month_1.setItemText(2, _translate("MainWindow", "Октябрь"))
        self.month_1.setItemText(3, _translate("MainWindow", "Ноябрь"))
        self.month_1.setItemText(4, _translate("MainWindow", "Декабрь"))
        self.month_1.setItemText(5, _translate("MainWindow", "Январь"))
        self.month_1.setItemText(6, _translate("MainWindow", "Февраль"))
        self.month_1.setItemText(7, _translate("MainWindow", "Март"))
        self.month_1.setItemText(8, _translate("MainWindow", "Апрель"))
        self.month_1.setItemText(9, _translate("MainWindow", "Май"))
        self.month_1.setItemText(10, _translate("MainWindow", "Июнь"))
        self.number_1.setItemText(0, _translate("MainWindow", "Все"))
        self.number_1.setItemText(1, _translate("MainWindow", "1"))
        self.number_1.setItemText(2, _translate("MainWindow", "2"))
        self.number_1.setItemText(3, _translate("MainWindow", "3"))
        self.number_1.setItemText(4, _translate("MainWindow", "4"))
        self.number_1.setItemText(5, _translate("MainWindow", "5"))
        self.number_1.setItemText(6, _translate("MainWindow", "6"))
        self.item_1.setItemText(0, _translate("MainWindow", "Все"))
        self.item_1.setItemText(1, _translate("MainWindow", "ДМ"))
        self.item_1.setItemText(2, _translate("MainWindow", "ИнфИС11к"))
        self.item_1.setItemText(3, _translate("MainWindow", "ИнфИС12к"))
        self.item_1.setItemText(4, _translate("MainWindow", "ИнфЮр11К"))
        self.item_1.setItemText(5, _translate("MainWindow", "ИнфЮр21К"))
        self.item_1.setItemText(6, _translate("MainWindow", "ИнфЮр22К"))
        self.item_1.setItemText(7, _translate("MainWindow", "ИнфЮр23К"))
        self.item_1.setItemText(8, _translate("MainWindow", "ИТИС21к"))
        self.item_1.setItemText(9, _translate("MainWindow", "МатИС11к"))
        self.item_1.setItemText(10, _translate("MainWindow", "УПр"))
        self.group_1.setItemText(0, _translate("MainWindow", "Все"))
        self.group_1.setItemText(1, _translate("MainWindow", "ИС21к"))
        self.group_1.setItemText(2, _translate("MainWindow", "ИС11к"))
        self.group_1.setItemText(3, _translate("MainWindow", "ИС12к"))
        self.group_1.setItemText(4, _translate("MainWindow", "ЮР11к"))
        self.group_1.setItemText(5, _translate("MainWindow", "ЮР21к"))
        self.group_1.setItemText(6, _translate("MainWindow", "ЮР22к"))
        self.group_1.setItemText(7, _translate("MainWindow", "ЮР23к"))
        self.classes_1.setItemText(0, _translate("MainWindow", "Все"))
        self.classes_1.setItemText(1, _translate("MainWindow", "0"))
        self.classes_1.setItemText(2, _translate("MainWindow", "Лекция"))
        self.classes_1.setItemText(3, _translate("MainWindow", "Практика"))
        self.classes_1.setItemText(4, _translate("MainWindow", "Урок"))
        self.classes_1.setItemText(5, _translate("MainWindow", "№Н/Д"))
        self.week_1.setItemText(0, _translate("MainWindow", "Все"))
        self.week_1.setItemText(1, _translate("MainWindow", "1"))
        self.week_1.setItemText(2, _translate("MainWindow", "2"))
        self.week_1.setItemText(3, _translate("MainWindow", "3"))
        self.week_1.setItemText(4, _translate("MainWindow", "4"))
        self.week_1.setItemText(5, _translate("MainWindow", "5"))
        self.week_1.setItemText(6, _translate("MainWindow", "6"))
        self.week_1.setItemText(7, _translate("MainWindow", "7"))
        self.week_1.setItemText(8, _translate("MainWindow", "8"))
        self.week_1.setItemText(9, _translate("MainWindow", "9"))
        self.week_1.setItemText(10, _translate("MainWindow", "10"))
        self.week_1.setItemText(11, _translate("MainWindow", "11"))
        self.week_1.setItemText(12, _translate("MainWindow", "12"))
        self.week_1.setItemText(13, _translate("MainWindow", "13"))
        self.week_1.setItemText(14, _translate("MainWindow", "14"))
        self.who_1.setItemText(0, _translate("MainWindow", "Все"))
        self.who_1.setItemText(1, _translate("MainWindow", "Я"))
        self.who_1.setItemText(2, _translate("MainWindow", "Другой"))
        self.openes.setText(_translate("MainWindow", "Сохранить"))
        self.exchange.setText(_translate("MainWindow", "Добавить/Изменить"))
        self.repear.setText(_translate("MainWindow", "Удалить"))
        self.open_xl.setText(_translate("MainWindow", "Открыть"))
