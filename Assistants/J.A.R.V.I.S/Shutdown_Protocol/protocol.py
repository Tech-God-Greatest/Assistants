def shutdown(Text):
    if "shutdown protocol 1029" in Text:
        with open("D:\\Assistants\\J.A.R.V.I.S\\state.txt", "w") as file:
                file.write("0")