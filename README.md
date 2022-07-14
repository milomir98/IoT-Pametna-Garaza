# IoT Pametna Garaza

## Uvod
Ovaj projekat ima za cilj da realizuje - Pametnu garazu - . Otvaranje i zatvaranje vrata garaze se vrsi automatski. Koristi se senzor detekcije koji detektuje da je automobil stao ispred garaze. Nakon sto senzor detektuje automobil, ukljucuje se kamera koja snima tablicu automobila i na osnovu broja sa tablice otvara vrata i ukljucuje svjetlo u garazi. Vrata se otvaraju pomocu step motora (za potrebe naseg projekta bice koriscen servo motor radi lakse implementacije).

## Neophodne komponente:
1. Raspberry Pi 3
2. RPi Kamera
3. Senzor detekcije pokreta
4. Servo motor

## Instalacija:
Potrebno je pokrenuti kod __table_recognition.py__ direktno sa RPi-a ili preko SSH. <br />
SSH: Instalirati PUTTY na racunar, povezati RPi na mrezu, ocitati IP adresu i ukucati je u PUTTY. Lozinka i korisnicko ime zavise od RPi-a.
