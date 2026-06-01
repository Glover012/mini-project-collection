import tkinter as tk
import yfinance as yf

window = tk.Tk()
window.title("Stock info")

topWidget = tk.Frame(window) 
label = tk.Label(topWidget, text="Write stock ticker: ")
label.pack(side=tk.LEFT)
entry = tk.Entry(topWidget)
entry.pack(side=tk.RIGHT)
topWidget.pack()

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textBox = tk.Text(window, height=50, width=100, padx=10, pady=10, font="Helvetica 12")
textBox.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=textBox.yview)
textBox.config(yscrollcommand=scrollbar.set)

def downloadData(event):     
    textBox.delete("1.0", tk.END)

    stock = str( event.widget.get() )

    if not stock:
        print("Incorrect/no stock ticker")
        return
    
    stock = stock.upper().strip()
    print("Download stock data: ", stock)

    stockData = yf.Ticker(stock)
    print(stockData.info)
    
    textBox.insert(tk.END, f"Ticker: {stock}\n\n")
    for key in stockData.info.keys():
        try:
            v = str(key) + ":" + stockData.info[str(key)] + "\n\n"
            textBox.insert(tk.END, v)
        except:
            pass

    textBox.insert(tk.END, f"History: {stock}\n\n")
    history = stockData.history(period="1mo", interval="1d") 
    textBox.insert(tk.END, history)

entry.bind("<Return>", downloadData)

window.mainloop()
