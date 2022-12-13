"""Análisis + 
Desarrollo 
Crea un script en el lenguaje de tu elección y encuentra la(s)
cadena de texto que es(son) igual al revés en el siguiente texto:
"""

#Buscar palindromos en este texto
#palindromos = "a foolish consistency is the hobgoblin of little minds adored by little statesmen and philosophers and divines with consistency a great soul has simply nothing to do he may as well concern himself with his shadow on the wall speak what you think now in hard words and tomorrow speak what tomorrow thinks in hard words again though it contradict every thing you said today ah so you shall be sure to be misunderstood is it so bad then to be misunderstood pythagoras was misunderstood and socrates and jesus and luther and copernicus and galileo and newton and every pure and wise spirit that ever took flesh to be great is to be misunderstood"
def buscar_palindromo(palindromo):
    palindromos = []
    letra = ""
    for i in range(len(palindromo)):
        letra = palindromo[i] #a
        for j in range(i+1, len(palindromo)):
            letra += palindromo[j] #acumulador 
            if letra == letra[: :-1] and len(letra) > 2: #condicion que comprueba el palindromo
                palindromos.append(letra) 
    return palindromos
print(buscar_palindromo("afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood"))


