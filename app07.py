from guizero import App, Text, PushButton, TextBox


app = App(title="ICI App")

def suma():
    app.info("la suma",f"la suma es {int(number1.value)+ int(number2.value)}")


message = Text(app, text="Escribe un numero ")
number1 = TextBox(app)
message_2 = Text(app, text= "Escribe otro numero numero")
number2= TextBox(app)
button=PushButton(app, text = "sumar", command= suma )
message_3 = Text(app)

app.display()