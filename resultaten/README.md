# Resultaten #

Hier zal de verzamelde data worden besproken en wordt er een poging gedaan de data te interpreteren om op die manier de volgende vragen te beantwoorden: 
* Hoe kan de kwaliteit van de verschillende oplossingen/algoritmes worden beoordeeld?
* Wat maakt bepaalde borden moeilijker dan andere borden?

Er is data verzameld met behulp van 3 verschillende algoritmes die op dezelfde computer werden uitgevoerd: 
<details>
  <summary>fully random</summary>
  <p> 
   Er zijn data samples verzameld van 100.000 oplossingen voor elk bord behalve nummer 7. Hierbij was het algoritme te traag om een        sample van 100.000 binnen een redelijke tijd te bemachtigen, en dus bestaat de sample hier uit slechts 10.000 oplossingen.
  </p>
</details>
<details>
<summary>branch and bound</summary>
  <p>
    
  </p>
</details>  
<details>  
<summary>breadth first</summary>
  <p>
    Het breadth first algoritme was in staat om oplossingen te vinden voor borden 1 t/m 4.
    
  </p>
</details>

## Hoe kan de kwaliteit van de verschillende oplossingen/algoritmes worden beoordeeld? ##
De meest voor de hand liggende factor waarop een oplossing kan worden beoordeeld is het aantal zetten: hoe minder zetten er worden gedaan, hoe beter de oplossing. Hiervoor is het uiteraard wel nodig dat er op z'n minst een oplossing wordt gevonden. Daarnaast is het een pluspunt als het algoritme snel tot een oplossing komt. 

Een andere factor om mee te nemen is hoeveel informatie er nodig is om een oplossing te kunnen vinden. Bij branch and bound werd in de meeste gevallen sneller een oplossing gevonden dan bij breadth first search, maar alleen nadat de optimale hoeveelheid zetten al door breadth first was gevonden, en ingevoerd als upper bound in branch and bound.

De kwaliteit van Aangezien een breadth first algoritme de beste oplossing garandeert, isHet blijkt echter dat de state space bij de moeilijkere problemen dusdanig groot wordt, dat het algoritme zelfs op een computer met een redelijk grote hoeveelheid werkgeheugen(16 GB) niet in staat is om een oplossing te vinden.

Er is dus behoefte aan een andere parameter om de kwaliteit te bepalen voor borden die te moeilijk zijn voor een conventioneel breadth first algoritme. Er is bijgehouden wat de runtime en de grootte van het archief waren bij zowel breadth first als branch and bound. Bij de random functie is de runtime en de best gevonden oplossing bijgehouden.  

## Hoe kan de kwaliteit van de verschillende algoritmes worden beoordeeld? ##


## Wat maakt bepaalde borden moeilijker dan andere borden? ##

