# dat158-project-2
Fruit Classifier
gruppe ---, 05.11.2024
Malen inneholder en del beskrivende tekst om hva dere kan skrive om under hver overskrift. Dette er kun forslag til elementer: dropp det som ikke er relevant i ditt tilfelle, og legg til element du finner relevant. Det eneste kravet er at beskrivelsen er i tråd med livssyklusen til maskinlæringsprosjekt skissert i kurset. Det vil si, at prosjektbeskrivelsen følger strukturen reflektert i overskriftene nedenfor. Slett alle instruksjoner (tekst i kursiv) før innlevering.
BESKRIV PROBLEMET
Fruktklassifiseringsprosjektet har som mål å utvikle et maskinlæringsbasert system som kan identifisere og klassifisere ulike typer frukt fra bilder. Modellen kan brukes av både privatpersoner og kommersielle aktører, som matbutikker, for å effektivisere fruktgjenkjenning for katalogisering eller prising. Dette kan spare tid og redusere behovet for manuell registrering.

SCOPE
●	Business objective: Målet med prosjektet er å automatisere klassifisering av frukt, noe som vil ha praktisk anvendelse for forhandlere eller automatiserte kjøkken.
●	Eksisterende løsninger: I dag løses dette manuelt av ansatte som identifiserer frukt visuelt, eller gjennom enklere systemer som strekoder
●	Ytelsesmåling (Business metrics): Forretningsmessig ytelse kan måles ved nøyaktigheten på klassifiseringen. Dersom modellen oppnår over 90 % nøyaktighet, kan den implementeres som et robust system.
●	Pipeline / Systemkomponenter: Fruktklassifiseringen vil være en del av et system som inkluderer en webapplikasjon med brukergrensesnitt (for eksempel Gradio), en backend for maskinlæringsmodellen og eventuell datalagring.
●	Stakeholders: Sluttbrukere er supermarkeder og matdistributører som ønsker å automatisere fruktgjenkjenning, samt utviklingsteamet og systemadministratorer. 
      Tentativ tidslinje og milepæler:
•	Uke 1-2: Datainnsamling og forberedelse
•	Uke 3-4: Modelltrening og validering
•	Uke 5: Testing og justering av modellen
•	Uke 6: Deployering og brukertesting
	
●	Ressurser: Prosjektet krever tilgang til datamaskin med GPU-støtte for modelltrening, samt tekniske ressurser for hosting av nettsiden og modellen
METRIKKER
•	Business metrics: En nøyaktighet på minst 90 % er nødvendig for å betrakte prosjektet som vellykket.
•	Maskinlærings- og software-metrikker:
o	Nøyaktighet (accuracy): Andelen korrekte klassifiseringer.
o	Latency: Responstid fra bildet lastes opp til prediksjonen er tilgjengelig.
o	Throughput: Antall bilder klassifisert per minutt.
•	Hvordan dette knyttes til målet: Nøyaktighet og latency vil påvirke brukervennligheten direkte, spesielt i miljøer som krever rask og pålitelig klassifisering.

DATA
•	Datakilder og etiketter: Datasettet kan være Fruits 360 fra Kaggle, et datasett med mange fruktsorter og etiketter. Dette gir et godt grunnlag for modelltrening og testing.
•	Datavolum og behov: Datasettet inneholder tusenvis av bilder, men flere eksemplarer kan forbedre modellen ytterligere.
•	Personvernhensyn: Ingen personlige data behandles, så personvern vil ikke være relevant i dette prosjektet.
•	Datarepresentasjon: Bildedata skal normaliseres og skaleres til 224x224 piksler, som er MobileNetV2-modellens input.
•	Forbehandling: Bildene vil bli forbehandlet for optimal kvalitet og størrelse før modelltrening. Ingen sensitive data behandles i dette prosjektet.

MODELLERING
•  Modellvalg: Vi bruker MobileNetV2, en pre-trent konvolusjonell nevralt nettverksmodell, som passer godt for bildeklassifisering med høy nøyaktighet.
•  Baseline-ytelse: Bruke enkle modeller som logistisk regresjon på dataene kan sette en baseline-ytelse, mens MobileNetV2 vil forhåpentligvis overgå denne baseline.
•  Evaluering av feil og viktige trekk: Feilprediksjoner vil bli analysert for å justere opplæringsdataene. "Feature importance" vil bli analysert ved hjelp av aktiveringskart for å forstå hvilke deler av bildet som bidrar mest til prediksjonene
DEPLOYMENT
•  Sette modellen i drift: Gradio-plattformen kan brukes til å hoste webapplikasjonen og gi brukerne enkel tilgang til modellen.
•  Monitorering og vedlikehold: Feilprediksjoner vil bli overvåket via brukerinteraksjon. Det planlegges regelmessige oppdateringer for å forbedre modellen.
•  Fremtidige forbedringer: Etter lansering vil brukernes tilbakemeldinger og feilrapporter brukes for kontinuerlig å forbedre modellen.
REFERANSER
1.	Kaggle Datasets: Fruits 360 Dataset
2.	Gradio Documentation - For hosting og UI utvikling
3.	TensorFlow Documentation

![image](https://github.com/user-attachments/assets/f75120cc-b4a2-458a-82db-d30d87034654)
