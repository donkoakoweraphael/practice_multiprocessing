from utils import *

def main():
    recuperer_un_etudiant()
    recuperer_un_prof()


if __name__ == '__main__':
    import time
    debut = time.perf_counter()
    main()
    fin = time.perf_counter()
    print(f'Programme executé en {fin-debut} s .')

print(__name__)