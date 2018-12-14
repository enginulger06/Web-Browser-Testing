# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pyspeedtest
from selenium import webdriver
class Ui_Dialog(object):

    def Speed(self):
        st = pyspeedtest.SpeedTest()
        ping = st.ping()
        download = int(st.download()) / 1048576
        upload = int(st.upload()) / 1048576
        p = str(round(ping, 2))+" ms"
        d = str(round(download, 2))+" Mbps"
        u = str(round(upload, 2))+" Mbps"
        self.ping_input.setText(p)
        self.download_input.setText(d)
        self.upload_input.setText(u)
    def hata(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def kontrol(self):
        self.web=self.source.text()
        durum=False
        if self.web=="":
            self.hata('URL Hatası', 'Lütfen Source adresine URL adresini giriniz..')
        else:
            self.combo_text = str(self.comboBox.currentText())
            durum=True
        return durum


    def chrome_check(self):
        durum=False
        if self.chrome_checkBox.isChecked():
            durum=True
        return durum

    def edge_check(self):
        durum=False
        if self.edge_checkBox.isChecked():
            durum=True
        return durum
    def firefox_check(self):
        durum=False
        if self.firefox_checkBox.isChecked():
            durum=True
        return durum
    def opera_check(self):
        durum=False
        if self.opera_checkBox.isChecked():
            durum=True
        return durum


    def Front_end(self):
        self.title="Front End"
        sozluk={}
        if self.kontrol()==True:
            URL=self.combo_text+self.web
            if self.chrome_check()==True:
                driver = webdriver.Chrome()
                driver.get(URL)
                self.test(driver)
                sozluk["chrome"]=self.Front_End
            if self.edge_check()==True:
                options = webdriver.ChromeOptions()
                options.binary_location ="C:/Windows/SystemApps/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/MicrosoftEdge.exe"
                driver = webdriver.Edge(options=options)
                driver.get(URL)
                self.test(driver)
                sozluk["edge"] = self.Front_End
            if self.firefox_check()==True:
                driver = webdriver.Firefox()
                driver.get(URL)
                self.test(driver)
                sozluk["firefox"] = self.Front_End
            if self.opera_check()==True:
                options = webdriver.ChromeOptions()
                options.binary_location = "C:\\Users\\Engin\\AppData\\Local\\Programs\\Opera\\57.0.3098.76\\opera.exe"
                driver = webdriver.Opera(options=options)
                driver.get(URL)
                self.test(driver)
                sozluk["opera"]=self.Front_End
        print(sozluk)
        self.deneme(sozluk)
    def Back_end(self):
        self.title="Back End"
        sozluk = {}
        if self.kontrol() == True:
            URL = self.combo_text + self.web
            if self.chrome_check() == True:
                driver = webdriver.Chrome()
                driver.get(URL)
                self.test(driver)
                sozluk["chrome"] = self.Back_End
            if self.edge_check() == True:
                driver = webdriver.Edge()
                driver.get(URL)
                self.test(driver)
                sozluk["edge"] = self.Back_End
            if self.firefox_check() == True:
                driver = webdriver.Firefox()
                driver.get(URL)
                self.test(driver)
                sozluk["firefox"] = self.Back_End
            if self.opera_check() == True:
                options = webdriver.ChromeOptions()
                options.binary_location = "C:\\Users\\Engin\\AppData\\Local\\Programs\\Opera\\57.0.3098.76\\opera.exe"
                driver = webdriver.Opera(options=options)
                driver.get(URL)
                self.test(driver)
                sozluk["opera"] = self.Back_End
        self.deneme(sozluk)
    def Back_Front_end(self):
        back={}
        front={}
        if self.kontrol() == True:
            URL = self.combo_text + self.web
            if self.chrome_check() == True:
                driver = webdriver.Chrome()
                driver.get(URL)
                self.test(driver)
                back["chrome"] = self.Back_End
                front["chrome"] = self.Front_End
            if self.edge_check() == True:
                driver = webdriver.Edge()
                driver.get(URL)
                self.test(driver)
                back["edge"] = self.Back_End
                front["edge"] = self.Front_End
            if self.firefox_check() == True:
                driver = webdriver.Firefox()
                driver.get(URL)
                self.test(driver)
                back["firefox"] = self.Back_End
                front["firefox"] = self.Front_End
            if self.opera_check() == True:
                options = webdriver.ChromeOptions()
                options.binary_location = "C:\\Users\\Engin\\AppData\\Local\\Programs\\Opera\\57.0.3098.76\\opera.exe"
                driver = webdriver.Opera(options=options)
                driver.get(URL)
                self.test(driver)
                back["opera"] = self.Back_End
                front["opera"] = self.Front_End
        self.deneme2(back,front)

    def deneme2(self,back,front):

        browser = []
        means_back = []
        means_front=[]
        for i in back:
            browser.append(i)
            means_back.append(back[i])
        for i in front:
            means_front.append(front[i])

        # data to plot
        n_groups = len(browser)

        # create plot
        fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(index, means_back, bar_width,
                         alpha=opacity,
                         color='b',
                         label='Back')

        rects2 = plt.bar(index + bar_width, means_front, bar_width,
                         alpha=opacity,
                         color='r',
                         label='Front')

        plt.xlabel('Browser')
        plt.ylabel('Saniye')
        plt.title('Browser Back and Front End Performans Testing')
        plt.xticks(index + bar_width, browser)
        plt.legend()

        plt.tight_layout()
        plt.show()
    def deneme(self, sozluk):

        objects = []
        performance = []
        for i in sozluk:
            objects.append(i)
            performance.append(sozluk[i])
        # objects = ('Chrome', 'Edge', 'Firefox', 'Opera')
        print(objects)
        print(performance)
        y_pos = np.arange(len(objects))
        # performance = [0,1,4,6,]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Saniye')
        plt.title('Browser '+self.title+' Performance Testing')

        plt.show()


    def Temizle(self):
        self.source.clear()
        if self.chrome_checkBox.isChecked():
            self.chrome_checkBox.setChecked(False)
        if self.edge_checkBox.isChecked():
            self.edge_checkBox.setChecked(False)
        if self.firefox_checkBox.isChecked():
            self.firefox_checkBox.setChecked(False)
        if self.opera_checkBox.isChecked():
            self.opera_checkBox.setChecked(False)
    def test(self, driver):
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")

        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart

        self.Back_End = float((backendPerformance) / float(1000))  # sonuc milisaniye olarak çıkıyor 1 saniye 1000 milisaniye
        self.Front_End = float((frontendPerformance) / float(1000))

        driver.quit()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1027, 458)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 70, 351, 221))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.ping_input = QtWidgets.QLineEdit(Dialog)
        self.ping_input.setGeometry(QtCore.QRect(240, 120, 113, 22))
        self.ping_input.setObjectName("ping_input")
        self.download_input = QtWidgets.QLineEdit(Dialog)
        self.download_input.setGeometry(QtCore.QRect(200, 180, 113, 22))
        self.download_input.setObjectName("download_input")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 120, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 180, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 240, 55, 16))
        self.label_3.setObjectName("label_3")
        self.upload_input = QtWidgets.QLineEdit(Dialog)
        self.upload_input.setGeometry(QtCore.QRect(160, 240, 113, 22))
        self.upload_input.setObjectName("upload_input")
        self.speed_btn = QtWidgets.QPushButton(Dialog)
        self.speed_btn.setGeometry(QtCore.QRect(30, 80, 93, 28))
        self.speed_btn.setObjectName("speed_btn")
        #speed btn
        self.speed_btn.clicked.connect(self.Speed)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(420, 70, 581, 331))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(450, 90, 55, 31))
        self.label_5.setObjectName("label_5")
        self.source = QtWidgets.QLineEdit(Dialog)
        self.source.setGeometry(QtCore.QRect(620, 90, 301, 31))
        self.source.setText("")
        self.source.setObjectName("source")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(520, 90, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(440, 150, 541, 171))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setEnabled(False)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(450, 200, 81, 61))
        self.label_6.setStyleSheet("image: url(:/newPrefix/icon/Chrome.ico);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(570, 200, 101, 61))
        self.label_7.setStyleSheet("image: url(:/newPrefix/icon/Explorer.ico);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(720, 200, 101, 61))
        self.label_8.setStyleSheet("image: url(:/newPrefix/icon/Firefox.ico);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(880, 200, 71, 61))
        self.label_9.setStyleSheet("image: url(:/newPrefix/icon/Opera.ico);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(470, 170, 55, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(580, 170, 91, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(730, 170, 91, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(900, 170, 55, 16))
        self.label_13.setObjectName("label_13")
        self.back_btn = QtWidgets.QPushButton(Dialog)
        self.back_btn.setGeometry(QtCore.QRect(460, 350, 93, 28))
        self.back_btn.setObjectName("back_btn")
        #tıklayınca
        self.back_btn.clicked.connect(self.Back_end)


        self.front_btn = QtWidgets.QPushButton(Dialog)
        self.front_btn.setGeometry(QtCore.QRect(570, 350, 93, 28))
        self.front_btn.setObjectName("front_btn")
        #tıklayınca
        self.front_btn.clicked.connect(self.Front_end)
        self.back_front_btn = QtWidgets.QPushButton(Dialog)
        self.back_front_btn.setGeometry(QtCore.QRect(680, 350, 141, 28))
        self.back_front_btn.setObjectName("back_front_btn")
        #tıklayınca
        self.back_front_btn.clicked.connect(self.Back_Front_end)

        self.temizle_btn = QtWidgets.QPushButton(Dialog)
        self.temizle_btn.setGeometry(QtCore.QRect(850, 350, 93, 28))
        self.temizle_btn.setObjectName("temizle_btn")
        #tıklayınca
        self.temizle_btn.clicked.connect(self.Temizle)

        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(430, 40, 241, 16))
        self.label_14.setObjectName("label_14")
        self.chrome_checkBox = QtWidgets.QCheckBox(Dialog)
        self.chrome_checkBox.setGeometry(QtCore.QRect(480, 280, 21, 20))
        self.chrome_checkBox.setText("")
        self.chrome_checkBox.setObjectName("chrome_checkBox")
        self.edge_checkBox = QtWidgets.QCheckBox(Dialog)
        self.edge_checkBox.setGeometry(QtCore.QRect(610, 280, 21, 20))
        self.edge_checkBox.setText("")
        self.edge_checkBox.setObjectName("edge_checkBox")
        self.firefox_checkBox = QtWidgets.QCheckBox(Dialog)
        self.firefox_checkBox.setGeometry(QtCore.QRect(760, 280, 21, 20))
        self.firefox_checkBox.setText("")
        self.firefox_checkBox.setObjectName("firefox_checkBox")
        self.opera_checkBox = QtWidgets.QCheckBox(Dialog)
        self.opera_checkBox.setGeometry(QtCore.QRect(910, 280, 21, 20))
        self.opera_checkBox.setText("")
        self.opera_checkBox.setObjectName("opera_checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Web Browser Performance Testing"))
        self.label.setText(_translate("Dialog", "PING"))
        self.label_2.setText(_translate("Dialog", "DOWNLOAD"))
        self.label_3.setText(_translate("Dialog", "UPLOAD"))
        self.speed_btn.setText(_translate("Dialog", "BAŞLAT"))
        self.label_4.setText(_translate("Dialog", "SPEED TEST"))
        self.label_5.setText(_translate("Dialog", "SOURCE"))
        self.comboBox.setItemText(0, _translate("Dialog", "http://www."))
        self.comboBox.setItemText(1, _translate("Dialog", "https://www."))
        self.label_10.setText(_translate("Dialog", "Chrome"))
        self.label_11.setText(_translate("Dialog", "Microsoft Edge"))
        self.label_12.setText(_translate("Dialog", "Mozilla Firefox"))
        self.label_13.setText(_translate("Dialog", "Opera"))
        self.back_btn.setText(_translate("Dialog", "BACK END "))
        self.front_btn.setText(_translate("Dialog", "FRONT END"))
        self.back_front_btn.setText(_translate("Dialog", "BACK and FRONT END"))
        self.temizle_btn.setText(_translate("Dialog", "TEMİZLE"))
        self.label_14.setText(_translate("Dialog", "WEB BROWSER PERFORMANCE TESTİNG"))

import xy

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())

