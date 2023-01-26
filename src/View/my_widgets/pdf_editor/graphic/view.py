import sys
from PySide2 import QtWidgets, QtGui,  QtCore 


import src.View.my_widgets.pdf_editor.graphic.scene as graphics_scene

class MyGraphicsView(QtWidgets.QGraphicsView):
    """класс переопределяющий  графическую вьюху"""

    def __init__(self, root, scene, **kwargs):
        super().__init__( **kwargs)
        # self.setupUi(self)
        self.main = root
        self.enter_event = False
        
        self.scene = scene
        self.setScene(self.scene)
        self.pen = QtGui.QPen(QtCore.Qt.green)
        self.greenBrush = QtGui.QBrush(QtCore.Qt.green)
        self.grayBrush = QtGui.QBrush(QtCore.Qt.gray)

    def zoom_view(self, int_scale):
        scale_scene = 1
        if int_scale > 0:
            scale_scene *= 1.25
            self.scale(scale_scene, scale_scene)
        elif int_scale < 0:
            scale_scene *= 0.8
            self.scale(scale_scene, scale_scene)
    
    def keyPressEvent(self, event):
        if event.key() == 16777249:
            self.enter_event = True
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        super().keyPressEvent(event)
        

    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == 16777249:
                self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
                self.enter_event = False
        super().keyReleaseEvent(event)

    def wheelEvent(self, event):
        int_y = event.angleDelta().y()
        scale_scene = 1
        if self.enter_event:
            if int_y > 0:
                scale_scene *= 1.25
                self.scale(scale_scene, scale_scene)
            if int_y < 0:
                scale_scene *= 0.8
                self.scale(scale_scene, scale_scene)

















