# Resultaten #

Hier zal de verzamelde data worden besproken en wordt er een poging gedaan de data te interpreteren om op die manier de volgende vragen te beantwoorden: 
* Hoe kan de kwaliteit van de verschillende oplossingen worden beoordeeld?
* Wat maakt bepaalde borden moeilijker dan andere borden?

Er is data verzameld met behulp van 3 verschillende algoritmes: 
<details>
  <summary>fully random</summary>
  <p> 
    Dit algoritme bereikt een oplossing door het maken van willekeurige zetten die worden gekozen uit een lijst van mogelijke zetten. Er     zijn data samples verzameld van 100.000 oplossingen voor elk spel behalve spel 7. Bij spel 7 liep het algoritme vast binnen een paar     honderd oplossingen, om deze reden is ervoor gekozen om 10 keer een sample van 100 oplossingen te nemen en daaruit de beste             oplossing te kiezen.
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
  
  </p>
</details>


## Hoe bepalen we wat de kwaliteit is van een oplossing? ##
De meest voor de hand liggende factor waarop een oplossing kan worden beoordeeld is het aantal zetten. Hoe minder zetten er worden gedaan, hoe beter de oplossing. Als dit als de enige belangrijke factor wordt beschouwd, zou een breadth first algoritme in theorie ideaal zijn, omdat daarmee altijd de best haalbare oplossing gegarandeerd wordt. Het blijkt echter dat de state space bij de moeilijkere problemen dusdanig groot wordt, dat zelfs op een computer met een redelijk grote hoeveelheid werkgeheugen(16 GB) het algoritme vastloopt. 

 
