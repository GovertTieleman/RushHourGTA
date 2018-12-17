# Code

Er zijn hier 2 mappen, een met python classes en een met algoritmes. Het doel van de classes is om een speelbare versie van het spel Rush Hour te vormen. Dit spel kan dan vervolgens door onze algoritmes worden gespeeld, met het doel om in zo min mogelijk zetten te winnen.

De classes zijn opgedeeld over een aantal bestanden. rushhour.py is waar het spel zelf is gecodeerd. Deze code maakt gebruikt van de classes Car.py en Board.py, die in aparte bestanden staan. 

Als rushhour.py wordt gerund wordt de speler om input gevraagd. Deze input wordt door de computer omgezet naar een zet en vervolgens wordt getracht deze uit te voeren. Het bord wordt in haar nieuwe staat uitgeprint en de speler wordt opnieuw verzocht een zet te doen. Dit gaat door tot de speler een stopcommando geeft of het spel wint.

Als experiment hebben we de find_moves functie, die de kinderen aanmaakt, aangepast om alleen moves van lengte 1 uit te voeren. We hoopten dat door minder moves aan te hoeven maken, de algoritmes efficiënter zouden worden in gebruik. Helaas bleek het te resulteren in veel grotere archieven voor oplossingen van dezelfde lengte, zonder duidelijke voordelen. Daarom hebben we dit experiment niet doorgevoerd naar de uiteindelijke versie.
