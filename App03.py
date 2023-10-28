from guizero import App, Text, PushButton

app = App(title="ICI App")
message = Text(app, text="welcome to the ICI App! ")

button = PushButton(app, text="Click me! ")

app.display()