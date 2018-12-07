# Resultaten #

Hier zal de verzamelde data worden besproken en wordt er een poging gedaan de data te interpreteren om op die manier de volgende vragen te beantwoorden: 
* Hoe kan de kwaliteit van de verschillende oplossingen/algoritmes worden beoordeeld?
* Wat maakt bepaalde borden moeilijker dan andere borden?

Er is data verzameld met behulp van 3 verschillende algoritmes die op dezelfde computer werden uitgevoerd: 

### fully random ###
   Er zijn data samples verzameld van 100.000 oplossingen voor elk bord behalve nummer 7. Hierbij was het algoritme te traag om een        sample van 100.000 binnen een redelijke tijd te bemachtigen, en dus bestaat de sample hier uit slechts 10.000 oplossingen.
   
   ![alt text](https://raw.githubusercontent.com/ertzor/RushHourGTA/master/resultaten/Random%20solutions/Random%20table.png)

### breadth first search ###
   Het breadth first algoritme was in staat om oplossingen te vinden voor borden 1 t/m 4.
    
   ![alt text](https://raw.githubusercontent.com/ertzor/RushHourGTA/master/resultaten/BFS%20solutions/BFS%20table.png?)
    
### branch and bound ###
   Het branch and bound algoritme vond oplossingen voor de borden 1 t/m 4 met behulp van de upper bound die werd gevonden met breadth      first search.
    
   ![alt text](https://raw.githubusercontent.com/ertzor/RushHourGTA/master/resultaten/BranchnBound%20solutions/BnB%20table.png)
  

## Hoe kan de kwaliteit van de verschillende oplossingen/algoritmes worden beoordeeld? ##
De meest voor de hand liggende factor waarop een oplossing kan worden beoordeeld is het aantal zetten: hoe minder zetten er worden gedaan, hoe beter de oplossing. Hiervoor is het uiteraard wel nodig dat er op z'n minst een oplossing wordt gevonden. Daarnaast is het een pluspunt als het algoritme snel tot een oplossing komt. 

Een andere factor om mee te nemen is hoeveel informatie er vooraf nodig is om een oplossing te kunnen vinden. Bij branch and bound werd in de meeste gevallen sneller een oplossing gevonden dan bij breadth first search, maar alleen nadat de optimale hoeveelheid zetten al door breadth first was gevonden, en ingevoerd als upper bound in branch and bound.

Aangezien een breadth first algoritme garandeert dat de gevonden oplossing ideaal is, lijkt dit de beste kandidaat voor elk bord. Het blijkt echter dat de state space bij de moeilijkere problemen dusdanig groot wordt, dat het algoritme zelfs op een computer met een redelijk grote hoeveelheid werkgeheugen(16 GB) niet in staat is om een oplossing te vinden. Hetzelfde geldt voor de branch and bound.

Er is dus behoefte aan een ander algoritme om oplossingen te vinden voor de borden die te moeilijk zijn voor de breadth first en branch and bound algoritmes. Hierbij is tijd een belangrijke factor. Het genereren van een sample van 100.000 oplossingen duurde bij veel borden meer dan 15 uur. 

Al met al kunnen we zeggen dat breadth first voor de eerste 4 borden duidelijk het best was. Er werd binnen een relatief korte tijd een oplossing gevonden en er was geen extra informatie nodig om dit mogelijk te maken. Branch and bound was iets sneller dan breadth first, maar kan dit alleen klaarspelen wanneer de ideale oplossing al bekend is. Voor borden 5 t/m 7 was random het best geteste algoritme, aangezien dit het enige algoritme was dat een oplossing vond.

## Wat maakt bepaalde borden moeilijker dan andere borden? ##
Zoals in de tabellen te zien is, verschilt de grootte van het archief en de tijd om tot een oplossing te komen aanzienlijk per bord, zelfs als deze dezelfde grootte hebben. Hoewel de theoretische state space groter wordt door meer auto's op het bord te plaatsen, blijkt de effectieve state space op zeer volle borden(denk aan bord 3) juist kleiner te worden. Dit komt doordat er weinig mogelijke zetten zijn. We verwachten dus dat de moeilijkheid van een bord afhankelijk is van het aantal auto's, maar dat er een punt is waar meer auto's het bord juist makkelijker maken. Verder lijken borden die in een laag aantal zetten kunnen worden opgelost makkelijker dan borden waar meer zetten nodig zijn. 

De volgende eigenschappen kunnen de moeilijkheidsgraad van een bord beïnvloeden:
* de grootte van het bord
* het aantal auto's op het bord
* minimum aantal zetten dat benodigd is om een oplossing te vinden


## Visualisatie van de gevonden oplossingen (voor level 1, 2 en 3)
Level 1:
![Level 1](https://github.com/ertzor/RushHourGTA/blob/master/resultaten/L1%20gif.gif)

Level 2:
![Level 2](https://github.com/ertzor/RushHourGTA/blob/master/resultaten/L2%20gif.gif)

Level 3:
![Level 3](https://github.com/ertzor/RushHourGTA/blob/master/resultaten/L3%20gif.gif)
