# Count frequences of clicks

Sirovi podaci uklju�uju datoteke:
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

Na temelju sirovih podataka potrebno je dopuniti skup podataka koji je djelomi�no formiran na temelju bodova iz sustava Mudri i ocjena iz sustava ISVU, a dan je u datoteci �Skup podataka za dopunit.xsl�.
Vrijednosti u stupcima koji nedostaju ra�unaju se za studenta s oznakom id na sljede�i na�in:
videos: ukupan broj pristupa pojedinog studenta svim video lekcijama
selfassesm1: ukupan broj pristupa pojedinog studenta samoprovjeri 1
selfassesm2: ukupan broj pristupa pojedinog studenta samoprovjeri 2
selfassesm: ukupan broj pristupa pojedinog studenta samoprovjeri 1 i 2 (zbroj pristupa)

Datoteka �Test podaci.xsl� sadr�i test podatke za provjeru stupaca videos i selfassesm.
Potrebno je na neki na�in podatke transformirati (ostavljam na volju kako �ete rije�iti problem). Mo�ete napisati program u C++ ili odabrati neku drugu metodu za transformaciju podataka. Slijede�i tjedan �u uploadati podatke za jo� �etiri generacije studenata, pa �ete u idu�oj vje�bi trebati pripremiti jo� �etiri skupa podataka i objedinjeni skup podataka. U izradi ovih vje�bi predvi�eno je da sura�ujete me�usobno kad god smatrate da je potrebno.
