class Celular():
    bateria = 'Infinita'
    tela = '4x3'
    tem_camera = True
    tem_camera = True
    tem_antena = True 
    cor = 'Cinza'
    modelo = 'Tijolão'

    def ligacao():
        print('Ligando...')

    def mensagem():
        print('Enviando Mensagem...')

    def jogo_cobrinha():
        print('Jogando...')

print(Celular.bateria)
print(Celular.jogo_cobrinha())



class Animal():
    especie = ''

class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis Lupus familiares'
    raca = 'Cofap'
    nome = 'Clt'
    porte = 'Gigante'

    def latir():
        return 'auauauauauau'
    
    def comer():
        return 'shcolop'
    
    def dormir():
        return 'mimimimi'
    
print(Cachorro.comer)
print(Cachorro.dormir)
print(Cachorro.latir)
