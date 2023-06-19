import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QComboBox, QFileDialog, QHeaderView, QMessageBox, QTableWidgetItem, QApplication, \
    QMainWindow, QTableWidgetItem, QTableView, QVBoxLayout
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit

from excel_writer import save_excel
from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
from connection import Data

import re  # импорт для regex


class Tracker(QMainWindow):
    def __init__(self):
        super(Tracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view_data()
        # Назначаем метод выделения по строкам и только одну ячейку
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows);
        self.ui.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection);
        # добавление сортировки
        self.ui.tableView.setSortingEnabled(True)
        # растяжение
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # связываем сигналы и слоты
        self.ui.exchange.clicked.connect(self.process_add_or_update_button)
        self.ui.repear.clicked.connect(self.delete_current_transaction)
        self.ui.openes.clicked.connect(self.create_report)
        # self.ui.open_xl.clicked.connect(self.loadExcelData('ras.xls', '(22)'))
        self.ui.open_xl.clicked.connect(self.loadExcelData)

        # связываем слоты фильтрации
        self.set_filter_slots()

        # связываем вкладки с staked widget
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.dnev.clicked.connect(lambda _: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.but_ktp.clicked.connect(lambda _: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.but_time.clicked.connect(lambda _: self.ui.stackedWidget.setCurrentIndex(2))


    def set_filter_slots(self):
        """
        Функция устанавливает слоты для фильтрации
        """
        self.mapper = QtCore.QSignalMapper()
        self.mapper.mapped[str].connect(self.filter_for_column)

        self.ui.month_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.month_1, self.ui.month_1.objectName())

        self.ui.number_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.number_1, self.ui.number_1.objectName())

        self.ui.item_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.item_1, self.ui.item_1.objectName())

        self.ui.group_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.group_1, self.ui.group_1.objectName())

        self.ui.classes_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.classes_1, self.ui.classes_1.objectName())

        self.ui.week_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.week_1, self.ui.week_1.objectName())

        self.ui.who_1.currentTextChanged.connect(self.mapper.map)
        self.mapper.setMapping(self.ui.who_1, self.ui.who_1.objectName())

    @QtCore.pyqtSlot(str)
    def filter_for_column(self, object_name):
        """
        Слот обрабатывает выбор ячейки в поле фильтра
        """
        # получаем весь список объектов
        list_obj = self.findChildren(QComboBox)
        # получаем объект от которого пришел сигнал
        obj = self.findChild(QComboBox, object_name)
        # проходимся, сбрасываем фильтры и назначаем новый
        for ui_obj in list_obj:
            if obj != ui_obj:
                ui_obj.setCurrentIndex(0) # type: ignore
        if object_name == "month_1":
            text = "" if obj.currentText() == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(1)
        elif object_name == "number_1":
            text = "" if obj.currentText()  == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(2)
        elif object_name == "item_1":
            text = "" if obj.currentText() == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(3)
        elif object_name == "group_1":
            text = "" if obj.currentText() == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(4)
        elif object_name == "classes_1":
            text = "" if obj.currentText() == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(5)
        elif object_name == "week_1":
            text = "" if obj.currentText() == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(6)
        elif object_name == "who_1":
            text = "" if obj.currentText() == "Все" else obj.currentText()
            self.model.setFilterFixedString(text)
            self.model.setFilterKeyColumn(7)

    def view_data(self):
        """
        Функция проверяет подключение к БД назначает модель, в случае ошибки
        выходит из приложения
        """
        try:
            self.conn = Data()
            self.sql_model = QSqlTableModel(self, self.conn.get_conn())
            self.sql_model.setTable('expense')
            self.sql_model.select()
            self.model = QtCore.QSortFilterProxyModel()
            self.model.setSourceModel(self.sql_model)
            self.ui.tableView.setModel(self.model)
        except FileExistsError as err:
            # В случае ошибки подключения выход с ошибкой
            QtWidgets.QMessageBox.critical(self, f"Error connection",
                                           f"{err},\nClick Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            sys.exit()


    """
    Чтение Excel файлов
    """

    def loadExcelData(self):
        print('a')
        """
        Функция читает Excel файл, считывает выбранного преподавателя и находит все его пары в расписании
        :return: отрисовывает таблицу Дата День недели Группа Номер пары Предмет Преподаватель Аудитория
        """
        choosed_fio = self.ui.FIO.currentText()  # ФИО выбранного преподавателя
        excel_file_path = 'ras.xls'
        df = pd.read_excel(excel_file_path,
                           skiprows=14,
                           usecols='A:AG'
                           )
        if df.size == 0:
            return
        df.fillna('', inplace=True)
        df = df.rename(columns={' ': 'День'})  # установить название столбца, хранящего день недели
        print('a')

        # нахождение по фамилии и сбор соответствующих данных
        pattern = r' \.\d{1,2}'
        res = []
        for column in df.columns:
            for i in range(1, len(df), 3):
                if df[column][i] == choosed_fio and not re.search(pattern, column):
                    day_number = (i // 24) * 24
                    res.append(f"{str(df[' .1'][day_number]).split()[0]}:{str(df['День'][day_number]).strip()}:{column}:"
                               f"{df[' .2'][i-1]}:{df[column][i-1]}:{df[column][i]}:{df[column][i+1]}")

        res = sorted(res, key=lambda x: x.split(',')[0])  # сортировка по дате

        model = QtGui.QStandardItemModel(len(res), 7)  # создание модели с количеством строк, равным длине массива
        model.setHorizontalHeaderLabels(
            ['Дата', 'День недели', 'Группа', 'Номер пары', 'Предмет', 'Преподаватель', 'Аудитория'])
        print('a')

        # заполнение модели данными из массива строк
        for row, line in enumerate(res):
            items = line.split(':')
            for col, item in enumerate(items):
                model.setItem(row, col,
                              QtGui.QStandardItem(item.strip()))  # добавить элемент в соответствующую ячейку таблицы

        self.ui.tableView_2.setModel(model)  # загрузить созданную модель в таблицу
        self.ui.tableView_2.setSortingEnabled(True)  # активировать предустановленную сортировку
        print('a')

    @QtCore.pyqtSlot()
    def create_report(self):
        """
        Функция создает excel документ
        """
        rows = []
        # Проходимся по полям таблицы и получаем список строк
        for row in range(self.model.rowCount()):
            data = []
            for col in range(self.model.columnCount()):
                data.append(
                    str(self.sql_model.record(row).value(col)) # обязательно данные преобразуем в str
                )
            rows.append(data)
        # Открываем диалог для сохранения
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","",
                                                  "All Files (*);;Excel files (*.xls, *.xlsx)", options=options)
        # если имя указано то сохраняем результат
        if fileName:
            # сохранение результата
            save_excel(fileName, rows)


    @QtCore.pyqtSlot()
    def process_add_or_update_button(self):
        """
        Функция используется для обработки кнопки добавления/обновления
        """
        index = self.ui.tableView.selectedIndexes()
        # если что-то выделено, то открываем обновление, если нет, то добавляем из combobox
        if len(index) > 0:
            self.update_row_into_table(index[0])
        else:
            self.insert_data_to_table()

    def update_row_into_table(self, index: QtCore.QModelIndex):
        """
        Обновление поля в таблице
        """
        # создаем диалог
        dialog = QtWidgets.QDialog()
        ui_window = Ui_Dialog()
        ui_window.setupUi(dialog)
        dialog.setWindowTitle(f"Обновление ячейки {index.data()}")
        print(f"Обновление ячейки {index.data()}")
        # запускаем
        ret_exec = dialog.exec()
        if ret_exec == 1:
            mounth = ui_window.comboBox_4.currentText()
            number_lesson = ui_window.comboBox.currentText()
            lesson = ui_window.comboBox_5.currentText()
            group = ui_window.comboBox_2.currentText()
            type_lesson = ui_window.comboBox_6.currentText()
            week = ui_window.comboBox_3.currentText()
            who = ui_window.comboBox_7.currentText()
            self.conn.update_transaction_query(mounth,
                                               number_lesson, lesson,
                                               group, type_lesson, week, who,
                                               index.data())
        # Обновляем модель
        self.sql_model.select()

    def insert_data_to_table(self):
        """
        Функция добавляет данные в таблицу
        """
        # создаем диалог
        dialog = QtWidgets.QDialog()
        ui_window = Ui_Dialog()
        ui_window.setupUi(dialog)
        # запускаем
        ret_exec = dialog.exec()
        if ret_exec == 1:
            mounth = ui_window.comboBox_4.currentText()
            number_lesson = ui_window.comboBox.currentText()
            lesson = ui_window.comboBox_5.currentText()
            group = ui_window.comboBox_2.currentText()
            type_lesson = ui_window.comboBox_6.currentText()
            week = ui_window.comboBox_3.currentText()
            who = ui_window.comboBox_7.currentText()
            self.conn.add_new_transaction_query(mounth, number_lesson, lesson,
                                                group, type_lesson, week, who)
        # Обновляем модель
        self.sql_model.select()

    @QtCore.pyqtSlot()
    def delete_current_transaction(self):
        """
        Слот предназначен для удаления полей в таблице
        """
        index = self.ui.tableView.selectedIndexes()
        # если что-то выделено, то открываем обновление, если нет, то добавляем из combobox
        if len(index) > 0:
            self.delete_row(index[0])

    def delete_row(self, index: QtCore.QModelIndex):
        """
        Удаление ячейки
        """
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f"Вы хотите удалить ячейку с № {index.data()}")
        msgBox.setWindowTitle("Удаление ячейки")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.conn.delete_transaction_query(index.data())
        # Обновляем модель
        self.sql_model.select()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Создаем класс главного окна приложения
    traker = Tracker()
    traker.show()
    # перехватываем выход из приложения
    sys.exit(app.exec_())

