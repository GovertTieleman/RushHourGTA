# Analyse van Rush Hour boards

## Inhoud

Op de png's in deze folder staan de Rush Hour borden weergeven waar wij mee werken. De cijfers op de auto's geven het aantal mogelijke posities weer. De vakjes die groen omlijnd zijn, zal nooit een auto op staan en zijn dus permanent vrij. De rood omlijne vakjes zijn juist permanent bezet.

## Analyse

Voor ieder bord hebben we gekeken naar de lower bound, upper bound en state space. Voor een aantal borden waren wij niet in staat deze precies te berekenen dus hebben wij de 'constraints' ontspannen om een benadering te geven van de echte waarde.

### Lower Bound

Bij de lower bound met 'constraint relaxation' is het toegestaan voor alle auto's, behalve de rode, over elkaar heen te rijden. Het gegeven nummer weergeeft het aantal moves benodigd om de weg naar de uitgang vrij te maken.
De lower bound met 'constraints' toegepast is de kortste oplossing die mogelijk is voor het bord. Deze hebben wij gevonden met behulp van het Breadth First Algoritme.

### Upper Bound

De upper bound staat gelijk aan de effectieve state space. Dit is namelijk het maximale aantal posities dat te bereiken is binnen een gegeven bord.

### State Space

Voor het berekenen van de state space hebben wij twee methodes toegepast die het aantal moelijke opstellingen van voertuigen als uitganspunt nemen.

#### Benadering van de state space

Voor het benaderen van de state space hebben wij het aantal mogelijke opstellingen afgeleid uit de posities van de auto's. De berekening hiervoor is het aantal mogelijke posities van de auto's vermenigvuldigt met elkaar. Voor Game #1 is dit 4 * 4 * 4 * 5 * 5 * 5 * 5 * 5 * 5, oftewel 4^3 * 5^6 = 1.000.000.

#### Effectieve state space

De effectieve state space hebben we berekend door het Depth First algoritme te runnen zonder win conditie. Deze heeft alle bereikbare opstellingen opgeslagen in het archief, de grootte van het archief is het cijfer dat is weergegeven in de tabel.


![Tabel](Schermafbeelding 2018-12-06 om 15.10.04.png?raw=true "Tabel")
