# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    from random import randint
    mao = ""
    botao = 0
    senhaCerta = "hormônio do sono"
    senhaDigitada = ""




define mc = Character('[namemc]')
define mc_whisper = Character('[namemc]', what_size=16)
define ma = Character('[namema]')
define ma_whisper = Character('[namema]', what_size=16)
define r = Character('Fulaninha')
define s = Character('Sala')
define t = Character('Mabel')
define a = Character('Igaryx')
define f = Character('Najon')
define flash = Fade(.25, 0.0, .75, color="#fff")



# The game starts here.

label start:

    $namemc = "Alfonso"
    $namema = "Pinhata"
    $fofo = 0
    $alegre = 0
    $arrogante = 0

    scene escola2
    with dissolve


    t "[namemc]... {w}[namemc]..."
    show professora with moveinright
    t "{w}[namemc]!!"
    with vpunch
    hide professora

    show mc sono
    with dissolve
    mc "Ehh..."
    mc "?!"

    "{cps=25}Levanto meu rosto em direção à professora.{/cps}"

    s "Ahahahaha!! "
    s "Ele fez de novo!!"

    show mc normal

    mc "Ahh..."
    mc "Foi mal...!"

    s "Ahahahahaha!!!!!"
    hide mc normal

    show professora

    t "{cps=25}[namemc]. Por acaso, você faz isso de propósito?{/cps}"
    t "{cps=25}Todo dia.{w} Todo dia você dorme na aula. Gosta de fazer pouco dos professores?{/cps}"
    t "{cps=25}Além disso o que é toda esta tralha na sua mesa?{/cps}"

    hide professora
    show mc normal

    mc "..."
    "{cps=25}Abaixo o rosto, incomodado de sentir todos me olhando.{/cps}"
    "{cps=25}{i}...Idiotas, mal sabem que estive trabalhando duro.{/i}{/cps}"

    mc "{cps=25}Desculpe, professora... Não vai acontecer novamente.{/cps}"
    hide mc normal
    show professora
    t "{cps=25}Você disse isso na vez passada. E na anterior. E na antes dessa.{/cps}"
    t "Tente direito."
    hide professora
    show menina ma

    r "{cps=25}Problemas pra dormir, [namemc]?{/cps}"
    r "{cps=25}Pode tentar parar de assistir pornô às duas da madrugada~{/cps}"
    s "AHAHAHAHAHAHAH!!!!"
    "{cps=25}A cara da Fulaninha me olhando fazendo esse comentário.{/cps}"
    "{cps=25}Olha a cara dela. Ela sabe perfeitamente que tá sendo escrota.{/cps}"

    hide menina ma
    show professora

    t "{cps=25}Ok, chega de besteira. Se isso continuar, só vai tomar ainda mais tempo da aula.{/cps}"
    t "{cps=25}Voltando ao problema 3 na página...{/cps}"
    hide professora

    show mc normal

    "{cps=25}Ela continua com os problemas dela.{/cps}"
    "{cps=25}Tem uns 3 alunos com o celular escondido no estojo.{/cps}"
    "{cps=25}E ali mais 3 desenhando pintos nas carteiras.{/cps}"
    "{cps=25}Eu vou olhar pra cara dela aqui até esse negócio acabar.{/cps}"
    "{cps=25}Como?... Como não entendem que só estão desperdiçando seu tempo vindo pra cá e resolvendo problemas idiotas de matemática..{/cps}"
    "{cps=25}Esses imbecis nem vão aplicar em algo real.{/cps}"
    "{cps=25}Eu coloquei tudo o que eu conhecia na minhas pesquisas com transmissão de rádio.{/cps}"
    "{cps=25}Eu tive que pesquisar um monte de coisas, então a maioria do conteúdo da aula eu já vi antes.{/cps}"
    "{cps=25}Tudo isso toma muito tempo de mim. E por quê eu faço isso?{/cps}"
    "Muito simples."
    show mc sacana
    "Eu quero *****."
    "{cps=25}Não faço ideia de algum outro motivo pra alguém estudar isso.{/cps}"
    "{cps=25}...Se bem que ***** é um motivo justo.{/cps}"
    show mc orgulho
    "{cps=25}Hmmm~ Justíssimo~{/cps}"
    hide mc orgulho

    show professora
    t "...O comprimento da onda é igual a 'Y', portanto é igual a 15."
    "..."
    t "E isso é tudo por hoje."
    hide professora

    "Eh!? Acabou a aula..."

    scene escola2
    with dissolve

    "Enquanto todos se retiram, fico um pouco mais para recolher as minhas ferramentas da mesa."
    show mc feliz
    "Minha invenção vai funcionar logo logo, sinto que falta pouco para funcionar perfeitamente!"
    "Pois afinal rádios são incríveis, e eu também~"
    hide mc feliz

    show menina normal

    r "[namemc]..! Ei!"

    mc "Ah, é você, oi..."

    show menina normal:
       xalign 0.25
    with dissolve
    show mc entediado:
       xalign 0.75
       yalign 1.0
    with dissolve

    r "Ainda tentando achar demônios com este rádio velho?"

    mc "Não são simples demônios, são lindas garotas~{w} ...Que virão enquanto durmo."

    r "Quê... Eh, deixa pra lá, queria te perguntar... "

    r "Poderia me ajudar a levar estes documentos até a sala de diretoria?"

    menu:
     "Eh... claro...":
       $fofo += 1
       jump continue1
     "Nossa, você realmente não consegue fazer nada sozinha":
       $arrogante += 1
       jump continue1
     "Pode deixar comigo!":
       $alegre += 1
       jump continue1



label continue1 :
    r "Muito obrigada [namemc], foi uma mão na roda!"
    mc "Uhum."

    show menina envergonhada

    r "Você é muito esforçado, sabia?"
    mc "Sei."
    r "Eh.. eu tava pensando... Sua casa fica no caminho da minha... e.. "
    mc "O que?"
    r "E que o caminho é meio chato... "
    r "Quero dizer! Perigoso!.. então..."
    mc "..."
    r "P-poderiamos voltar juntos!"

    menu:
     "Se quer mesmo... não tem mal. ":
       $fofo += 1
       jump continue2
     "Foi mal, tenho que voltar rápido para terminar de ajustar meu {b}rádio velho{/b}, então se quiser me siga.":
       $arrogante += 1
       jump continue2
     "Tá legal! já estava voltando mesmo.":
       $alegre += 1
       jump continue2


label continue2 :
    scene rua
    with fade
    "Por que tenho que fazer isso? {w}Se tivesse sozinho já haveria chegado."
    show menina envergonhada:
       xalign 0.25
       yalign 1.0
    with dissolve
    show mc normal:
       xalign 0.75
       yalign 1.0
    with dissolve

    r "Ah é... [namemc], você está livre sábado? É que pensei que seria legal se pudessemos..."
    mc "Não posso, desculpe mas tenho que focar nos meus experimentos."
    r "Você é muito malvado, nem ao menos ouviu o que ia dizer...{w} Quero dizer, você não escuta niguém!"
    "Do que essa doida tá falando?"
    r "Já parou pra pensar nas oportunidades que você perde por não se socializar com os outros?"
    mc "Como o que? Usar todo o meu tempo e dinheiro indo em bares e karaokês? {w} Como todos os idiotas daquela maldita sala?"
    r "Por que está agindo assim? {w}Sabe... {w}eu conheço seu lado bom."
    r "Sei que é muito inteligente e cheio de ideais.{w} Por isso que...que.."
    "Que saco... só queria voltar logo."
    hide mc normal
    show menina envergonhada :
       xalign 0.5
       yalign 1.0
    r "POR ISSO QUE SEMPRE GOSTEI DE VOCÊ!"
    "Mas que ****??"

    menu:
     "...Olha, eu não tô entendo muito bem.":
       mc "...Olha, eu não tô entendo muito bem o que está acontecendo aqui, mas... Você é a única daqueles inúteis que considero como amiga... Então..."
       $fofo += 1
       jump continue3
     "Você está louca? Olha pra você!":
       mc "Você está louca? Olha pra você. Acha mesmo que eu tenho tempo a perder com tábuas? Ahahaha!"
       $arrogante += 1
       jump continue3
     "Quê? Ahahaha ata":
       mc "Quê? Ahahaha ata, sua casa é ali certo? Vou indo, até amanhã."
       $alegre += 1
       jump continue3

label continue3:
    show menina raiva
    with hpunch
    r "Que..."
    r "TA BOM entendi!... Até nunca imbecil!"
    hide menina raiva
    "..."
    "Ela saiu correndo por causa disso? Talvez deveria ter pensado melhor o que falar...{w}Mas tenho a impressão que daria no mesmo."

    scene mesa dark
    with fade

    "Chegando em casa, corro direto para o quarto."
    "Finalmete de volta à minha fortaleza~"
    show mc feliz
    mc "Vamos ver se hoje funciona..."
    mc "Minha íncrivel máquina de atração de sucubus, versão beta 0.8526!!"

    show mc sacana
    "A verdade é que meu sonho sempre foi ver uma succubus de verdade."
    "Dizem que elas são extremamente bonitas{w} e {b}bem dotadas~{/b}"
    "Não me importaria de ser atacado por uma.{w}Na verdade é isto que quero, caramba!"
    "Por isso trabalho dia e noite."
    "Descobri que as pessoas emitem uma frequência de ondas quando dormem."
    "E eu fiz este rádio produzir uma frequência similar com uma pessoa a dormir."
    "Porém centenas de vezes maior!... {w}Mas..."
    "Ainda não apareceu nada, e nem aconteceu algo comigo..."
    hide mc sacana

    "De repente uma luz forte surge no meio do meu quarto."
    with flash
    scene mesa light
    "Quase me cegando."

    "Seria isto...finalmente!..."
    "..."
    "..."
    "Mas que merda é essa ?!"
    show ma normal
    with vpunch

    ma "AAH você é o [namemc] certo??"
    "Esse troço fala??"
    mc "Quem? N-não! Não sou não!"
    show ma normal:
       xalign 0.25
       yalign 1.0
    with dissolve
    show mc surpreso:
       xalign 0.75
       yalign 1.0
    with dissolve
    ma "Que.. Mas eu não posso ter errado..."
    show mc normal
    mc "Pois errou, vaza bicho esquisito!"
    ma "Esperaa, você é mesmo o [namemc].{w} Olha só esta super máquina aqui, é disto que preciso!"
    mc "Eh?.. Este é meu rádio, tá doido?"
    ma "Hehe... Já saquei a tua."
    show ma confiante
    ma "Junte-se a mim!"
    mc "Mas o que..."
    mc "Juntar a quê?{w} PRA QUÊ?"

    ma "Você consegue atrair demônios sexuais com isto certo?? "
    mc "Não!{w} Quer dizer eu tentei... Mas..."
    mc "Nunca funcionou... {w} Talvez seja mesmo impossível..."
    ma "Bléh.. Seja mais otimista criança!"
    "O bicho estranho se aproxima de minha mesa e toca em meu querido rádio (!!!)"
    ma "O problema era,{w} que só estava faltando um pouquinho disto!"
    with flash
    mc "O que você fez?... Que merda fez com a minha grande invenção??"
    "Meu rádio de 1 kilo vira uma espécie de pulseira infantil...Quê?"
    ma "Ufufu~ Então agora você admite...{w} Enfim, só dei uma ajudinha...{w} Com um pouco de magia. "
    mc "É.{w} Eu tô sonhando, boa noite."
    show ma normal
    ma "Espere, com isto é pra estar funcionando..."
    show mc surpreso
    mc "Hã?"
    mc "Eeeh?...Espera, agora vai funcionar?"


    ma "Poderia ficar quieto? Jovem esquentadinho, eu não me apresentei ainda."
    ma "Meu nome é [namema], sou um holly, uma criatura mágica que caça..."
    mc "Oh Oh! Vo-você caça succubus!"
    ma "É.... quase isso..."
    menu:
     "Por favor, me ajude com esta tal magia!":
       jump continue4
     "Ah sei, por favor vá embora.":
       ma "Não posso fazer nada sendo assim."
       return

label continue4:
    ma "Tá legal, só preciso que você use esta pulseira-rádio ou sei lá."
    show mc normal
    mc "Mas por quê tem que ser eu a usar?"
    ma "..."
    show ma confiante
    ma "Por que não combina comigo."
    "Não vou responder isso."
    "Eu coloco a pulseira"
    mc "Não aconteceu nada."
    show ma normal
    ma "Espere um pouco..."
    "Pip pip pip!..."
    with flash


    scene quarto dark
    with fade
    show mc feliz
    with dissolve
    mc "Finalmente, finalmentee!!"
    show mc transformado
    with fade
    mc "Espera um pouco, por que minha roupa... também mudou?"
    mc "E que diabos de roupa é essa?"
    ma "Só parte do pacote, lide com isso."
    "Eu certamente nunca tive tanta vontade de matar uma alpaca falante e colorida como hoje."

    with dissolve
    "Olha esta fumaça toda..."
    #mc "Está aqui, minha querida sucu..."
    hide mc transformado




    if (fofo > arrogante and  fofo > alegre):
        jump incubusfofo

    elif (arrogante > fofo and arrogante > alegre):
        jump incubusarrogante

    elif (alegre > arrogante and alegre > fofo):
        jump incubusalegre

    else:
        python:
            sorteio = randint(0,2)

    if (sorteio == 0):
        jump incubusfofo

    elif (sorteio == 1):
        jump incubusarrogante

    elif (sorteio == 2):
        jump incubusalegre



label incubusfofo:
    #centered "Clique 10 vezes o botão!"

    #centered "Lá vai!"
    #show screen button
    #while botao < 10:
    #    "Clique no botão 10 vezes!"
    #hide screen button
    #if botao >= 10:
    #    centered "é acho que deu certo!"
    #return
    centered "Continua..."
    return



label incubusarrogante:
   show relaxado normal
   with pixellate
   mc "..."
   mc "Não..não..nãonãonão !!"
   "Olho rapidamente para o [namema]."

   show ma normal at left
   ma "Que foi? Faça seu trabalho e encontre uma maneira de derrotá-lo."
   show mc transformado at right
   mc "Derrotá-LO? Então é mesmo um homem??"
   ma "Não é um homeem...{w}É um íncubus!"
   mc "Íncu...quee?? Não era isso que eu queria!"
   ma "E eu não queria ser a porra de um híbrido de ovelha com lhama, mas olha só!"
   show mc transformado serio
   mc "Seu filho da GRRR!"
   hide ma normal
   show relaxado normal at left:
      zoom 1.1
   with fade


   f "Hmm... por que será que fui atraido pra cá sendo que não há mulher alguma..."
   f "Isso não faz o mínimo sentido."
   f "Por acaso isso é culpa sua?{w} Eu exijo explicações."
   "Ótimo! Era o que faltava."
   mc "O-olha... na verdade eu nem queria estar fazendo parte disto."
   f "Hmm... pode até ser que não foi de propósito. Mas de alguma forma seu dispositivo está me atraindo."
   f "Então caso não saiba, eu vou te dizer..."
   f "A melatonina é uma molécula antiga e onipresente na natureza, apresentando múltiplos mecanismos de ação e funções em praticamente todo organismo vivo."
   ma_whisper "Isso não é bom [namemc]... Você tem que fazer algo."
   f "Em mamíferos a melatonina funciona como um hormônio e um cronobiótico, desempenhando importante papel na regulação da ordem temporal circadiana interna, que seria o 'relógio biológico'."
   mc_whisper "Fazer algo? Fazer o quê??"
   f "Conhecida como 'o hormônio do sono', regula os ciclos circadianos, sendo a sua produção estimulada pela escuridão e inibida pela luz."
   ma_whisper "Você pode mudar a maneira como é transmitido a frêquencia do pulseira-rádio, caso consiga inverter...{w} Ela se tornará altamente destrutiva para ele!"
   show relaxado surpreso
   f "Hmm... ... Você está prestando atenção? Suas ações são muito estranhas, vou ter que concluir que afinal isto é plano seu? {w} Me atrair até aqui."
   "Merda, merda, merda!"
   "Okay, deve ter algum botão ou mini chave..."
   "Vruu~"
   "Oh ligou!"
   centered "RESOLVA PARA DESBLOQUEAR O ACESSO"

   while senhaDigitada != senhaCerta:
        python:
            senhaDigitada = renpy.input("Como é conhecida a molécula melatonina?")
        if senhaDigitada != senhaCerta:
            "Você errou a senha!"
            jump bearrogante

   jump gearrogante

label gearrogante:
    centered "ACESSO DESBLOQUEADO"
    ma "Isso [namemc]! Agora você só precisa usar o Radar Delete!"
    "É o que?"
    f "Urgh, mas era óbvio."
    f "Gastei meu tempo, então você sabe muito bem como lidar com isso, quero dizer.{w} Em vez de hormônios, deve conhecer muito bem as frequências e como transmiti-las especificamente."
    show relaxado confiante
    f "Mas não ache que possa me vencer fedelho! Você, sendo humano está em um nível totalmente inferior ao meu..."
    "Ele caminha lentamente em minha direção"
    ma "Tem que ser agora [namemc]!"
    mc "Entendido!"
    menu:
       "Usar a magia em ..." :
          jump gearrogante1
       "Hesitar..." :
          jump bearrogante

label gearrogante1:
    show relaxado surpreso
    with dissolve
    f " O que... O que diabos? "
    f "Eu não posso ser derrotado por isso!!"
    f "AAAHHHH"
    "Como em camêra lenta, o íncubo foi sumindo na minha frente"
    hide relaxado surpreso
    with pixellate
    jump final

label bearrogante:
    centered "ACESSO BLOQUEADO"
    "Eu... não consegui..."
    f "Eu avisei que não poderia fazer nada contra mim."
    f "Agora, não posso admitir que você tenha um tipo de magia que eu não domine, logo eu, o grande Najon"
    mc "S-são as frequências! A pulseira que está emitindo, não eu!"
    f "Não irá me enganar novamente, criança tola."
    "O íncubo se aproxima ainda mais"
    show relaxado confiante at center
    with fade
    "Ele segura meu braço agressivamente."
    "Então é quando sinto uma aura pesada, que me faz perder um pouco das forças."
    f "Não admito, não isso, agora me mostre!"
    jump gameover

    return

label incubusalegre:

    show alegre normal
    with pixellate
    mc "..."
    mc "Não..não..nãonãonão !!"
    "Olho rapidamente para o [namema]."

    show ma normal at left
    ma "Que foi? Faça seu trabalho e encontre uma maneira de derrotá-lo."
    show mc transformado at right
    mc "Derrotá-LO? Então é mesmo um homem??"
    ma "Não é um homeem...{w}É um íncubus!"
    mc "Íncu...quee?? Não era isso que eu queria!"
    ma "E eu não queria ser a porra de um híbrido de ovelha com lhama, mas olha só!"
    show mc transformado serio
    mc "Seu filho da GRRR!"

    hide ma normal
    show alegre normal at left
    with fade

    a "Ei ei ei~ Mas que cheiro maravilhoso é esse hein?"
    a "Ho... Que inusitado, você é um humano macho certo?{w} E ainda por cima está acordado..."
    "Por que não tenho uma boa impressão sobre isso?"
    a "E como você emite essas frequências? Isso é tão interessante ahahaha!"
    a "Mas sabe...isso deve ser 'ilegal' hehe, por acaso é esta pulseira que faz isso? Ou seria você?"
    "Que sensação é esta? Estou imobilizado."
    ma_whisper "Isso não é bom [namemc]... Você tem que fazer algo."
    mc_whisper "Fazer algo? Fazer o quê??"
    ma_whisper "Você pode mudar a maneira como é transmitido a frêquencia do pulseira-rádio, caso consiga inverter...{w} Ela se tornará altamente destrutiva para ele!"
    "Okay, deve ter algum botão ou mini chave..."
    "Vruu~"
    "Oh ligou!"
    centered "RESOLVA PARA DESBLOQUEAR O ACESSO"

label incubusalegre1:

    python:
        sorteio = randint(1,3)

    if sorteio == 1:
        $mao = "pedra"
    elif sorteio == 2:
        $mao = "papel"
    else:
        $mao = "tesoura"
    menu:
        "Pedra":

            "Na tela aparece:{w} [mao]."
            if sorteio == 1:
                "Empate!"
                jump incubusalegre1
            elif sorteio == 2:
                "Eu perdi..."
                jump bealegre
            else:
                "Eu venci!"
                jump gealegre
        "Papel":
            "Na tela aparece:{w} [mao]."
            if sorteio == 1:
                "Eu venci!"
                jump gealegre
            elif sorteio == 2:
                "Empate!"
                jump incubusalegre1
            else:
                "Eu perdi..."
                jump bealegre
        "Tesoura":
            "Na tela aparece:{w} [mao]."
            if sorteio == 1:
                "Eu perdi..."
                jump bealegre
            elif sorteio == 2:
                "Eu venci!"
                jump gealegre
            else:
                "Empate!"
                jump incubusalegre1

label gealegre:
    centered "ACESSO DESBLOQUEADO"
    ma "Isso [namemc]! Agora você só precisa usar o Radar Delete!"
    "É o que?"
    a "O que vocês dois estam tramando hein?"
    mc "Não-o.. se aproxi..."
    a "O que? Não te escutei. {w} Sabe de uma coisa? Você me atraiu até aqui, logo deveria se responsabilizar. "
    "Merda, merda, merda!"
    ma "Tem que ser agora [namemc]!"
    mc "Entendido!"
    menu:
       "Usar a magia em ..." :
          jump final
       "Hesitar..." :
          jump bealegre

label bealegre:
    centered "ACESSO BLOQUEADO"
    mc "... ah"
    ma "Isso nunca tinha ocorrido comigo até agora."
    a "Eu não sei como você tem esse cheiro, mas eu quero descobrir."
    a "Nunca vi um humano macho conseguir atrair um íncubo. Será que você tem algum tipo de magia diferente?"
    #show mc tranformado
    mc "S-são as frequências! A pulseira que está emitindo, não eu!"
    a "Aaah não, não! Eu vim seguindo a frequência."
    a "Mas você emite algo forte. Estou realmente curioso pra saber o que é!"
    mc "E-eu emito?"
    "Eu olho para [namema]"
    ma "*Sorrisinho*"
    ma "Ufufufu~"
    "Quando eu olho pro íncubo novamente, ele está mais perto."
    show alegre normal at center:
        zoom 1.1
    with fade

    a "Ehehehe. Eu quero experimentar essa magia e ver o que acontece!"
    mc "EEEEH?"
    jump gameover
    

label final:
    show mc normal at right

    ma "Enfim tudo deu certo [namemc]~"
    mc "Fala como se tivesse sido fácil..."
    scene end


label gameover:
    scene end
