import time


def recuperer_un_etudiant():
    print('Recupération d\'un etudiant en cours ...')
    time.sleep(1)
    print('Etudiant récupéré en 1 s')


def recuperer_un_prof():
    print('Recupération d\'un professeur en cours ...')
    time.sleep(2)
    print('Professeur récupéré en 2 s')

if __name__ == '__main__':
    print('utils')
    print(__name__)