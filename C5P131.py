Yellow = 'Yellow'
Green  = 'Green'
Red    = 'Red'
Nada   = 'Nada'

alien_color = Nada

if alien_color == Green:
    pontos = [5]    
    print('\nSeu alien é verde, ganhou ' + str(pontos) + ' Pontos.')

elif alien_color == Yellow:
    pontos = [10]
    print('Seu alien é Amarelo, ganhou ' + str(pontos) + ' Pontos.')

if alien_color == Red:
    pontos = [15]
    print('Seu alien é Vermelho, ganhou' + str(pontos) + ' Pontos')

else:
    print('Nada a informar.')