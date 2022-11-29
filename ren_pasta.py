import os

def principal ():
    i = 0
             #coloque aqui o diretorio que deseja renomear
    diretorio = "C:/Users/Vitor Life/Pictures/Saved Pictures/"
    for filename in os.listdir(diretorio):
        destino = "img" + str(i) + ".jpg"
        origem = diretorio + filename
        destino = diretorio + destino
        os.rename(origem, destino)
        i += 1

if __name__ == '__main__':
    principal()

