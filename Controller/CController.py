from Model.CModel import CModel
from View.CView import CView

class CController:

    def __init__(self):
        self.model = CModel()
        self.view = CView(self)

    def start(self):
        self.view.start()

    def add(self):
        try:
            a, b = self.view.get_numbers()
        except ValueError as e:
            self.view.display_result(str(e))
            return
        result = self.model.add(a, b)
        self.view.display_result(result)

    def subtract(self):
        try:
            a, b = self.view.get_numbers()
        except ValueError as e:
            self.view.display_result(str(e))
            return
        result = self.model.subtract(a, b)
        self.view.display_result(result)

    def multiply(self):
        try:
            a, b = self.view.get_numbers()
        except ValueError as e:
            self.view.display_result(str(e))
            return
        result = self.model.multiply(a, b)
        self.view.display_result(result)

    def divide(self):
        try:
            a, b = self.view.get_numbers()
        except ValueError as e:
            self.view.display_result(str(e))
            return
        if b == 0:
            self.view.display_result("Error: Division by zero.")
            return
        result = self.model.divide(a, b)
        self.view.display_result(result)
