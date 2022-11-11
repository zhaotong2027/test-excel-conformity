import sys
from PySide2.QtWidgets import QWidget, QComboBox, QTextEdit, QHBoxLayout, \
    QVBoxLayout, QApplication


class ComboxDemo(QWidget):
    def __init__(self, parent=None):
        super(ComboxDemo, self).__init__(parent)
        self.setWindowTitle('ComBox例子')
        self.textEditL = QTextEdit()
        self.textEditR = QTextEdit()
        self.textEditL.resize(200, 200)
        self.textEditR.resize(200, 200)

        self.cb1 = QComboBox()
        self.cb2 = QComboBox()

        '''单个添加条目'''
        self.cb1.addItem('textEditL1')
        self.cb1.addItem('textEditL2')
        self.cb1.addItem('textEditL3')
        '''多个添加条目'''
        self.cb2.addItems(['textEditR1', 'textEditR2', 'textEditR3'])

        '''当下拉索引发生改变时发射信号触发绑定的事件'''
        self.cb1.currentIndexChanged.connect(self.selectionchange1)
        self.cb2.currentIndexChanged.connect(self.selectionchange2)

        '''设置布局,hboxup用来将两个textEdit放在同一个水平布局上,hboxdown将两个combobox放在同一个水平布局上,
        vbox用来将hboxup和hboxdown放在同一个垂直布局上,在hboxdown后面或者前面添加一条hboxdown.addstretch(1)
        可以在hboxdown的布局中添加一些空白距离,距离的大小由addstretch()括号中的值和addstretch()使用次数决定'''
        vbox = QVBoxLayout()
        hboxdown = QHBoxLayout()
        hboxup = QHBoxLayout()
        hboxup.addWidget(self.textEditL)
        hboxup.addWidget(self.textEditR)
        hboxdown.addWidget(self.cb1)
        hboxdown.addStretch(1)
        hboxdown.addWidget(self.cb2)
        hboxdown.addStretch(1)
        vbox.addLayout(hboxup)
        vbox.addLayout(hboxdown)
        self.setLayout(vbox)

    def selectionchange1(self, i):
        self.textEditL.setText(
            self.cb1.currentText())  # currentText()：返回选中选项的文本
        print('Items in the list are:')
        '''输出选项集合中每个选项的索引与对应的内容
           count()：返回选项集合中的数目'''
        for count in range(self.cb1.count()):
            print('Item' + str(count) + '=' + self.cb1.itemText(count))
            print('current index', i, 'selection changed',
                  self.cb1.currentText())

    def selectionchange2(self, j):
        self.textEditR.setText(self.cb2.currentText())
        for count in range(self.cb2.count()):
            print('Item' + str(count) + '=' + self.cb2.itemText(count))
            print('current index', j, 'selection changed',
                  self.cb2.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    comboxDemo = ComboxDemo()
    comboxDemo.show()
    sys.exit(app.exec_())