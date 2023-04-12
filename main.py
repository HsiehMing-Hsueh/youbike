import datasource
import tkinter as tk
from tkinter import ttk

sbi_number = 3
bemp_number = 3

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        top_wrapperFrame = ttk.Frame(self)
        top_wrapperFrame.pack(fill=tk.X)
        #建立行政區的topFrame
        topFrame =ttk.LabelFrame(top_wrapperFrame,text="台北市行政區")
        #建立(多選一選項)的事件
        self.radioStringVar =tk.StringVar()
        #取得行政區的名稱
        length = len(datasource.sarea_list)
        for i in range(length):
            cols = i % 3
            rows = i // 3
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.radioStringVar,command=self.radio_Event).grid(column=cols,row=rows,sticky=tk.W,padx=10,pady=10)
        topFrame.pack(side=tk.LEFT)
        #建立sbi_warningFrame--------------------------
        sbi_warningFrame = ttk.LabelFrame(top_wrapperFrame, text="可借目前不足站點")

        sbi_warningFrame.pack(side=tk.LEFT)
        #建立bemp_waringFrame
        bemp_warningFrame = ttk.LabelFrame(top_wrapperFrame, text="可還目前不足站點")

        bemp_warningFrame.pack(side=tk.LEFT)
        #預設選項選擇為信義區
        self.radioStringVar.set('信義區')
        self.area_data = datasource.getInfoFromArea('信義區')
        #建立warningFrame


        #建立bottomFrame裝Treeview-------------------
        bottomFrame = ttk.LabelFrame(self, text="信義區")
        bottomFrame.pack()
        #建立Treeview
        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')
        self.tree.heading('#1', text='站點')
        self.tree.column("#1", minwidth=0, width=200)
        self.tree.heading('#2', text='時間')
        self.tree.column("#2", minwidth=0, width=200)
        self.tree.heading('#3', text='總車數')
        self.tree.column("#3", minwidth=0, width=50)
        self.tree.heading('#4', text='可借')
        self.tree.column("#4", minwidth=0, width=30)
        self.tree.heading('#5', text='可還')
        self.tree.column("#5", minwidth=0, width=30)
        self.tree.heading('#6', text='地址')
        self.tree.column("#6", minwidth=0, width=250)
        self.tree.heading('#7', text='狀態')
        self.tree.column("#7", minwidth=0, width=30)
        self.tree.pack(side=tk.LEFT)

        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']])
        # 幫treeview加scrollbar------------------------------------------------

        scrollbar = ttk.Scrollbar(bottomFrame, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)

    def radio_Event(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        area_name = self.radioStringVar.get()
        self.area_data = datasource.getInfoFromArea(area_name)
        
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']])
#主程式
def main():
    window =Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()

if __name__ == "__main__":
    main()