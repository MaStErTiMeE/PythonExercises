

import immagini
def es49(fimm1,fimm2,fimm3):
    '''
    Si definisca la  funzione es49(fimm1,fimm2,fimm3) che, 
    - riceve gli  indirizzi di due file .PNG da leggere (fimm1 e fimm2) e l'indirizzo 
      di un file (fimm3) da creare.
    - legge le due immagini e crea la terza immagine da salvare all'indirizzo fimm3. 
      La terza immagine si ottiene dalle prime due. Ha ampiezza  minima tra 
      le ampiezze  di fimm1 e fimm2 ed  altezza minima tra le altezze di fimm1 e fimm2.
      il pixel [i][j] dell'immagine ha lo stesso colore del pixel corrispondente
      dell'immagine fimm1 se i e j sono entrambi numeri pari o entrambi numeri dispari, 
      ha il colore del pixel corrispondente in  fimm2 altrimenti
    - salva l'immagine creata all'indirizzo fimm3
    - calcola  il numero di pixel presenti nell'immagine creata per i quali  la somma delle 
      tre coordinate del colore e' un numero dispari.
      - restituisce il valore calcolato
    Per caricare e salvare i file PNG si possono usare load e save della libreria immagini.
    '''
    img1 = immagini.load(fimm1)
    img2 = immagini.load(fimm2)
    img3 = []
    altezza_img_1 = len(img1)
    larghezza_img_1 = len(img1[0])

    altezza_img_2 = len(img2)
    larghezza_img_2 = len(img2[0])

    min_altezza_img = min(altezza_img_1,altezza_img_2)
    min_larghezza_img = min(larghezza_img_1,larghezza_img_2)
    
    for y in range(min_altezza_img) :
        nuovaRiga = []
        for x in range(min_larghezza_img) :
            pixel_img_1 = img1[y][x]
            pixel_img_2 = img2[y][x]
            if y % 2 == 0 and x % 2 == 0 or y % 2 != 0 and x % 2 != 0:
                pixel_aggiungere = pixel_img_1
            else :
                pixel_aggiungere = pixel_img_2
        nuovaRiga.append(pixel_aggiungere)
    img3.append(nuovaRiga)

    immagini.save(img3,fimm3)
    altezzaImg3 = len(img3)
    larghezzaImg3 = len(img3[0])
    contatore = 0
    
    for x in range(altezzaImg3) :
        for y in range(larghezzaImg3) :
            somma = sum(img3[y][x])
            if somma % 2 != 0 :
                contatore += 1


    return contatore




