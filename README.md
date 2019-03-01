# Count frequences of clicks

Sirovi podaci ukljuèuju datoteke:
samoprovjeraizlaz1.txt (frekvencija klikova vezano uz pristup samoprovjeri 1 za studenta x; koliko puta se x pojavljuje u datoteci toliko puta je student kliknuo vezano uz samoprovjeru 1)
samoprovjeraizlaz2.txt (isto za samoprovjeru2)
videoizlaz1.txt (frekvencija pristupa studenta za id=x video lekciji 1; koliko puta se x pojavio u datoteci toliko puta je student pristupio videu)
videoizlaz2.txt (isto za ostala videa)
videoizlaz3.txt
videoizlaz4.txt
videoizlaz5.txt
videoizlaz6.txt
videoizlaz7.txt
videoizlaz8.txt
videoizlaz9.txt
videoizlaz10.txt
videoizlaz11.txt
videoizlaz12.txt
videoizlaz13.txt

Na temelju sirovih podataka potrebno je dopuniti skup podataka koji je djelomièno formiran na temelju bodova iz sustava Mudri i ocjena iz sustava ISVU, a dan je u datoteci „Skup podataka za dopunit.xsl“.
Vrijednosti u stupcima koji nedostaju raèunaju se za studenta s oznakom id na sljedeæi naèin:
videos: ukupan broj pristupa pojedinog studenta svim video lekcijama
selfassesm1: ukupan broj pristupa pojedinog studenta samoprovjeri 1
selfassesm2: ukupan broj pristupa pojedinog studenta samoprovjeri 2
selfassesm: ukupan broj pristupa pojedinog studenta samoprovjeri 1 i 2 (zbroj pristupa)

Datoteka „Test podaci.xsl“ sadrži test podatke za provjeru stupaca videos i selfassesm.
Potrebno je na neki naèin podatke transformirati (ostavljam na volju kako æete riješiti problem). Možete napisati program u C++ ili odabrati neku drugu metodu za transformaciju podataka. Slijedeæi tjedan æu uploadati podatke za još èetiri generacije studenata, pa æete u iduæoj vježbi trebati pripremiti još èetiri skupa podataka i objedinjeni skup podataka. U izradi ovih vježbi predviðeno je da suraðujete meðusobno kad god smatrate da je potrebno.
