"""aplicacion para preguntar el nombre """

from guizero import App, Text, PushButton, TextBox

def say_hello():
    app.info("mensaje", f"hola  {name.value}")
    #message_2.value = "hola " + name.value

app = App(title="ICI App")

message = Text(app, text="¿Cómo te llamas? ")
name = TextBox(app)
message_2=Text(app)
button=PushButton(app, text = "click me", command= say_hello )
app.display()