screen button:

    textbutton "Clicou [botao] vezes" clicked SetVariable("botao", botao+1)align (.95,.04)
    if botao == 9:
        textbutton "Clicou [botao] vezes" clicked [SetVariable("botao", botao+1), Return("foi")] align (.95,.04)
