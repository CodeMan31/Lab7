from guizero import App, Text, Box, PushButton


def correct():
    if app.yesno("Correct!", "Do you want to quit?"):
        app.destroy()
        print("Adios")
    
    
def incorrect():
    if app.yesno("Incorrect!", "Do you want to quit?"):
        app.destroy()
        print("Adios")
    

if __name__ == '__main__':
    app =App(title="My app", height=300, width=600, layout="grid")
    text = Text(app, text="Who was the first person in Space?", grid = [0,0])
    box = Box(app, layout="grid", grid=[0,2])
    button1 = PushButton(box, command=incorrect, text = "1", grid = [0,1])
    button2 = PushButton(box, command=incorrect, text = "2", grid = [0,2])
    button3 = PushButton(box, command=correct, text = "3", grid = [0,3])
    text1 = Text(box, text="Lance Armstrong", grid = [1,1])
    text2 = Text(box, text="Neil Armstrong", grid = [1,2])
    text3 = Text(box, text="Yuri Gagarin", grid = [1,3])
    app.display()
    
