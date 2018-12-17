# Algoritmes
In deze map staan de algoritmes voor het oplossen van het spel

## Random
Dit algoritme maakt simpelweg willekeurige zetten totdat het bord is opgelost. Er kan worden ingesteld hoe vaak het algoritme het bord oplost, en daaruit wordt dan de snelste oplossing gekozen.

## 'Smart'-Random
Dit algoritme is een random algoritme dat echter de bord-states bijhoudt, en enkel (willekeurige) zetten doet waarvan het bord nog niet is langsgekomen. Als er geen zetten meer mogelijk zijn, 'backtrackt' het algoritme en kiest het een andere willekeurige zet. Ook identificeert het algoritme mogelijke 'winning moves' -zetten die de weg voor de rode auto vrijmaken- en voert dezen, als mogelijk, uit. Tevens geeft dit algoritme de voorkeur aan zetten die het bord 'more winnable' maken, oftewel: zetten waarbij auto's die tussen de rode auto en de uitgang staan opzij worden geschoven. Met een initiële upper bound van 500 word het algoritme 100 keer gerund, waarbij het aantal zetten in de gevonden oplossing als nieuwe upper bound wordt ingesteld.

## Depth First
Ons Depth First algoritme doorzoekt boomstructuur van een probleem door middel van recursie. Voor iedere 'state' worden de kinderen, 'moves', aangemaakt en wordt steeds het eerste kind gekozen dat naar naar een state leidt die niet eerder bezocht is. Wanneer de oplossing gevonden is, traceerd het algoritme het afgelegde pad en legt hij deze vast in een attribuut. 

## Branch n Bound
Dit algoritme is een uitbreiding van Depth First. Er is een bound aan het algoritme toegevoegd die ervoor zorgt dat er niet verder wordt gezocht dan de kortste route die bekend is voor het bord.

## Breadth First
Breadth first search werkt ook door de state te verkennen vanuit een boomstructuur. In plaats van een hele vertakking tot het einde af te gaan, zoals bij depth first gebeurt, wordt elke depth eerst volledig verkend. Dit houdt in dat elke mogelijke zet op een bord wordt gedaan, en de kinderborden worden opgeslagen. Pas als alle zetten van alle borden op een bepaalde diepte zijn geprobeerd gaat het algoritme verder naar de volgende diepte. Door een archief bij te houden wordt het herhalen van reeds gepasseerde borden vermeden.

## check moves
Met deze file kan een moves list worden gecontroleerd door na elke move het bord te printen. Kopiëer een lijst van moves en voer deze in als argument bij solve, onderaan de code. 