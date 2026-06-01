import tkinter as tk

window = tk.Tk()
window.title("Calculator")

class Calculator:
    def __init__(self, window):
        self.equationStrVar = tk.StringVar()
        self.expressionStr = ""
        self.calcKeyboard = [
            ["7","8","9","+"],
            ["4","5","6","-"],
            ["1","2","3","*"],
            ["0","Clear","=","/"]
        ]
        self.prepareGui(window)
    
    def prepareGui(self, window):
        window.geometry("512x256")
        self.expressionField = tk.Entry(window, textvariable=self.equationStrVar)
        self.expressionField.grid(columnspan=4, ipadx=20)

        rowIndex = 0
        while rowIndex < len(self.calcKeyboard):
            calculatorRow = self.calcKeyboard[rowIndex]

            columnIndex = 0
            while columnIndex < len(calculatorRow):
                buttonText = calculatorRow[columnIndex]
                button = tk.Button(window, text=buttonText, height=1, width=4, fg="black", bg="silver", 
                                   command = lambda buttonValue = buttonText: self.buttonPressed(buttonValue) )
                button.grid(column=columnIndex, row=rowIndex+1)
                columnIndex += 1
            rowIndex += 1

    def buttonPressed(self, buttonValue):
        print(f"button pressed {buttonValue}")

        if buttonValue == "Clear":
            self.expressionStr = ""
            self.equationStrVar.set("")
            return

        if buttonValue == "=":
            result = str( eval(self.expressionStr) )
            self.expressionStr = result
            self.equationStrVar.set(result)
            return

        self.expressionStr += str(buttonValue)
        self.equationStrVar.set(self.expressionStr)

calculator = Calculator(window)

window.mainloop()
