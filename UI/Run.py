import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QSize, QParallelAnimationGroup, Qt
from Main_widget.MainWindow import Ui_MainWindow
from Main_widget.data_display import Graph_widget
from Main_widget.database_display import Database_widget
from Main_widget.prediction_display import Predict_widget

import time as t
class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window."""
    def __init__(self):
        """Initializer."""
        super().__init__()
        # Use a QPushButton for the central widget
        self.setupUi(self)
        # Set frameless window
        self.setWindowFlag(Qt.FramelessWindowHint) 
        #Set new title bar
        self.top_bar.mouseMoveEvent = self.MoveWindow
        self.top_bar.mousePressEvent = self.mousePressEvent
        #Expand and reduce side bar
        self.home_button.clicked.connect(self.expand)
        # Clear any existing layout in content_display
        if self.content_display.layout() is not None:
            self.content_display.layout().deleteLater()

        # Set up the layout and add CustomWidget to content_display
        self.frame_layout = QHBoxLayout(self.content_display)
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.database_button.clicked.connect(self.open_database_tab)
        self.graph_button.clicked.connect(self.open_graph_tab)
        self.predict_button.clicked.connect(self.open_predict_tab)
        # Add CustomWidget instance to content_display
        #custom_widget = CustomWidget(self)
        #self.frame_layout.addWidget(custom_widget)
    def MoveWindow(self, event):
        # Move the window only when the left mouse button is held
        if event.buttons() == Qt.LeftButton:
            if not self.isMaximized():
                self.move(self.pos() + event.globalPosition().toPoint() - self.clickPosition)
                self.clickPosition = event.globalPosition().toPoint()
                event.accept()
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition().toPoint()
        
    def expand(self):
        time = 500
        if self.side_bar.size().width() < 200:
            self.side_bar.setMaximumWidth(self.side_bar.width() + 200)

        self.home_button.setEnabled(False)
        self.anim_group = QParallelAnimationGroup()
        self.animation = QPropertyAnimation(self.side_bar, b"size")
        self.animation.setDuration(time)
        self.animation.setStartValue(self.side_bar.size())
        if self.side_bar.size().width() > 200:
            self.animation.setEndValue(self.side_bar.size() - QSize(200,0))
        else:
            self.animation.setEndValue(self.side_bar.size() + QSize(200,0))
        
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)
        # Top bar animation
        self.animation_1 = QPropertyAnimation(self.main_content, b"size")
        self.animation_1.setDuration(time)
        self.animation_1.setStartValue(self.main_content.size())
        if self.side_bar.size().width() > 200:
            self.animation_1.setEndValue(self.main_content.size() + QSize(200,0))
        else:
            self.animation_1.setEndValue(self.main_content.size() - QSize(200,0))
        
        self.animation_1.setEasingCurve(QEasingCurve.InOutQuad)
        #Main content animation
        self.animation_2 = QPropertyAnimation(self.main_content, b"pos")
        self.animation_2.setDuration(time)
        self.animation_2.setStartValue(self.main_content.pos())
        if self.side_bar.size().width() > 200:
            self.animation_2.setEndValue(self.main_content.pos() - QPoint(200, 0))

        else:
            self.animation_2.setEndValue(self.main_content.pos() + QPoint(200, 0))

    
        self.animation_2.setEasingCurve(QEasingCurve.InOutQuad)
       
        self.anim_group.addAnimation(self.animation)
        self.anim_group.addAnimation(self.animation_1)
        self.anim_group.addAnimation(self.animation_2)
        
        self.anim_group.start()
        
        self.anim_group.finished.connect(self.set_enabled)
        
        

        
    def set_enabled(self):
        self.home_button.setEnabled(True)
 
        if self.side_bar.size().width() < 200:
            self.side_bar.setMaximumWidth(self.side_bar.width())
            
       
    def open_database_tab(self):
        self.remove_all_widget(self.frame_layout)
        database_widget = Database_widget(self)
        self.frame_layout.addWidget(database_widget)
    def open_graph_tab(self):
        self.remove_all_widget(self.frame_layout)
        graph_widget = Graph_widget(self)
        self.frame_layout.addWidget(graph_widget)
    def open_predict_tab(self):
        self.remove_all_widget(self.frame_layout)
        predict_widget = Predict_widget(self)
        self.frame_layout.addWidget(predict_widget)
    def remove_all_widget(self, layout):
        for i in range(layout.count()):
            item = layout.itemAt(i)
            widget = item.widget()  # Get the widget from the layout item
            widget.close()

app = QApplication.instance()
if not app:  # If no QApplication instance exists
    app = QApplication(sys.argv)


window = MainWindow()
window.show()
app.exec()