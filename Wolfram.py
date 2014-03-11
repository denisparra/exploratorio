import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def query(self):
        import urllib.request
        content = urllib.request.urlopen("http://api.wolframalpha.com/v2/query?appid=6V4244-XHERH3WH4P&input=" + self.entry.get().replace(" ", "%20") + "&format=image,plaintext").read()
        content = str(content)[2:-1].replace("\\n", "\n")
        f = open("xml.xml", mode="w")
        f.write(content)
        def parse(content):
            import xml.etree.ElementTree as ET
            root = ET.fromstring(content)
            if root.attrib['success'] == "true":
                print(root[0][0][0].text)
            else:
                print("error")
        parse(content)

    def createWidgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack()

        self.ok = tk.Button(self, text="OK", command=self.query)
        self.ok.pack(side="bottom")

    

root = tk.Tk()
app = Application(master=root)
app.mainloop()
