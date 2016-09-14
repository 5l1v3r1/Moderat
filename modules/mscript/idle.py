from PyQt4.QtGui import *
from PyQt4.QtCore import *
import autocompleter
import keyword

import py_syntax


class DictionaryCompleter(QCompleter):
    def __init__(self, parent=None):
        QCompleter.__init__(self, keyword.kwlist, parent)


class LineTextWidget(QFrame):


 
    class NumberBar(QWidget):
 
        def __init__(self, *args):
            QWidget.__init__(self, *args)
            self.edit = None
            # This is used to update the width of the control.
            # It is the highest line that is currently visibile.
            self.highest_line = 0
 
        def setTextEdit(self, edit):
            self.edit = edit
 
        def update(self, *args):
            '''
            Updates the number bar to display the current set of numbers.
            Also, adjusts the width of the number bar if necessary.
            '''
            # The + 4 is used to compensate for the current line being bold.
            width = self.fontMetrics().width(str(self.highest_line)) + 4
            if self.width() != width:
                self.setFixedWidth(width)
            QWidget.update(self, *args)
 
        def paintEvent(self, event):
            contents_y = self.edit.verticalScrollBar().value()
            page_bottom = contents_y + self.edit.viewport().height()
            font_metrics = self.fontMetrics()
            current_block = self.edit.document().findBlock(self.edit.textCursor().position())
 
            painter = QPainter(self)
 
            line_count = 0
            # Iterate over all text blocks in the document.
            block = self.edit.document().begin()
            while block.isValid():
                line_count += 1
 
                # The top left position of the block in the document
                position = self.edit.document().documentLayout().blockBoundingRect(block).topLeft()
 
                # Check if the position of the block is out side of the visible
                # area.
                if position.y() > page_bottom:
                    break
 
                # We want the line number for the selected line to be bold.
                bold = False
                if block == current_block:
                    bold = True
                    font = painter.font()
                    font.setBold(True)
                    painter.setFont(font)
 
                # Draw the line number right justified at the y position of the
                # line. 3 is a magic padding number. drawText(x, y, text).
                painter.drawText(self.width() - font_metrics.width(str(line_count)) - 3, round(position.y()) - contents_y + font_metrics.ascent(), str(line_count))
 
                # Remove the bold style if it was set previously.
                if bold:
                    font = painter.font()
                    font.setBold(False)
                    painter.setFont(font)
 
                block = block.next()
 
            self.highest_line = line_count
            painter.end()
 
            QWidget.paintEvent(self, event)
 
 
    def __init__(self, title='idle', *args):
        QFrame.__init__(self, *args)

        idleTitle = title
 
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        self.setStyleSheet('''
padding: 2px;
color: #2ecc71;
font: 75 8pt "MS Shell Dlg 2";
border: 1px ridge;
border-color: #2c3e50;''')

        self.edit = autocompleter.CompletionTextEdit()
        self.completer = DictionaryCompleter()
        self.edit.setCompleter(self.completer)
        self.edit.setLineWrapMode(QTextEdit.NoWrap)
        self.edit.setFrameStyle(QFrame.NoFrame)
        self.edit.setAcceptRichText(False)
        self.edit.setTabStopWidth(20)
        self.edit.setStyleSheet('''
        color: #c9f5f7;
        border: none;
        background-color: #34495e;
        background-repeat: no-repeat;
        background-position: center;
        padding: 5px;
        padding-top: 1px;
        ''')
        highlight = py_syntax.MyHighlighter(self.edit, 'Classic')
 
        self.number_bar = self.NumberBar()
        self.number_bar.setTextEdit(self.edit)

        vbox = QVBoxLayout(self)
        vbox.setSpacing(0)
        vbox.setMargin(0)
        self.box_title = QLabel(idleTitle)
        self.box_title.setAlignment(Qt.AlignCenter)
        self.box_title.setStyleSheet('border: none; align: center;')
        vbox.addWidget(self.box_title)
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setMargin(0)
        hbox.addWidget(self.number_bar)
        hbox.addWidget(self.edit)
        vbox.addLayout(hbox)

 
        self.edit.installEventFilter(self)
        self.edit.viewport().installEventFilter(self)
 
    def eventFilter(self, object, event):
        # Update the line numbers for all events on the text edit and the viewport.
        # This is easier than connecting all necessary singals.
        if object in (self.edit, self.edit.viewport()):
            self.number_bar.update()
            return False
        return QFrame.eventFilter(object, event)
 
    def getTextEdit(self):
        return self.edit.toPlainText()

    def clearText(self):
        self.edit.clear()

    def setText(self, string):
        self.edit.setPlainText(string)

    def setHtml(self, string):
        self.edit.setHtml(string)

    def appendText(self, string):
        self.edit.append(string)