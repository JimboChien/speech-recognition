from tkinter import *
import io

def clickExit():
    global root
    root.destroy()
    
def read_setence():
    global t
    f = io.open('keysentence.txt', encoding = 'utf-8-sig')
    keysentence = f.read()
    t.left.insert('1.0',keysentence)
    f.close()
    f = io.open('reply.txt', encoding = 'utf-8-sig')
    reply = f.read()
    t.right.insert('1.0',reply)
    f.close()

def save_file():
    global t
    f = io.open('reply.txt', 'w' ,encoding = 'utf-8-sig')
    f.write(t.right.get('1.0', 'end'))
    f.close()
    f = io.open('keysentence.txt', 'w',encoding = 'utf-8-sig')
    f.write(t.left.get('1.0', 'end'))
    f.close()
    
def enterkey():
    global t
    print('enter')
    temp_keysentence = t.left.get('1.0', 'end')
    temp_reply = t.right.get('1.0', 'end')
    print(temp_keysentence)
    temp_keysentence = temp_keysentence.split(u'\n')
    temp_reply = temp_reply.split(u'\n')
    if len(temp_keysentence) > len(temp_reply):
        for i in range(len(temp_keysentence)):
            if temp_keysentence[i] == '':
                t.right.insert(str(i+1)+'.0','\n')
                print('right',i)
                break
    elif len(temp_keysentence) > len(temp_reply):
        for i in range(len(temp_reply)):
            if temp_reply[i] == '':
                t.left.insert(str(i+1)+'.0','\n')
                print('left',i)
                break
    else:
        return
            
class ScrolledTextPair(Frame):
    '''Two Text widgets and a Scrollbar in a Frame'''

    def __init__(self, master, **kwargs):
        Frame.__init__(self, master) # no need for super

        # Different default width
        if 'width' not in kwargs:
            kwargs['width'] = 30

        # Creating the widgets
        self.left = Text(self, wrap='none',width=60)
        self.left.grid(row=0,column=0,rowspan=15,columnspan=10,sticky='e')
        self.add = Button(self, text="Add",command=enterkey)
        self.add.grid(row=7,column=10,sticky='e')
        self.save = Button(self, text="Save",command=save_file)
        self.save.grid(row=8,column=10,sticky='e')
        self.right = Text(self,wrap='none',width=60)
        self.right.grid(row=0,column=11,rowspan=15,columnspan=10,sticky='e')
        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=0,column=21,rowspan=15,columnspan=1,sticky='ns')

        # Changing the settings to make the scrolling work
        self.scrollbar['command'] = self.on_scrollbar
        self.left['yscrollcommand'] = self.on_textscroll
        self.right['yscrollcommand'] = self.on_textscroll

    def on_scrollbar(self, *args):
        self.left.yview(*args)
        self.right.yview(*args)

    def on_textscroll(self, *args):
        self.scrollbar.set(*args)
        self.on_scrollbar('moveto', args[0])

# Example
if __name__ == '__main__':
    root = Tk()
    t = ScrolledTextPair(root, bg='white', fg='black')
    t.pack(fill=BOTH, expand=True)
    read_setence()    
    root.title("對應句編輯器")
    root.mainloop()

# Spinbox