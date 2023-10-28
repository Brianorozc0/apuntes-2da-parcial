"""aplicacion para preguntar el nombre """

from guizero import App, Text, PushButton, TextBox


app = App(title="ICI App")

message = Text(app, text="¿Cómo te llamas? ")
name = TextBox(app)

app.display()