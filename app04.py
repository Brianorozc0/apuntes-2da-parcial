from guizero import App, Text, PushButton

def say_hello():
    message_2.value = "ICI Rocks! "

app = App(title="ICI App")
message = Text(app, text="welcome to the ICI App! ")

button = PushButton(app, text="Click me! ", command=say_hello)
message_2= Text(app)

app.display()