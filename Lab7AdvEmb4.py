from guizero import App, Text, Picture


def exit_gui():
    if app.yesno("Exit", "Are you sure?"):
        app.destroy()


if __name__ == '__main__':
    app = App("Wanted!")
    app.bg = "#A0A0A0"
    wanted_text = Text(app,"YODA")
    wanted_text.text_size = 50
    wanted_text.font = "Times New Roman"
    cat = Picture(app, image = "yoda.png", width = 400, height = 400)
    app.when_closed = exit_gui
    app.display()



