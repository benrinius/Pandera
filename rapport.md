# Pandera - datavalidering i Python

## Syfte
Syftet med denna fördjupning var att lära mig hur Pandera kan användas för datavalidering i Python. Jag ville undersöka hur man kan definiera regler för hur data ska se ut och sedan använda Pandera för att automatiskt upptäcka fel som bryter mot dessa regler.

## Området och dess relevans
Jag valde att fördjupa mig inom datavalidering med hjälp av Pandera, ett python-bibliotek som kan användas för att kontrollera att data följer fördefinierade regler. Pandera kan bland annat kontollera datatyper, tillåtna värden och andra villkor för en Dataframe. På så sätt kan problem i data upptäckas innan datan används vidare.

Datakvalitet är relevant inom Data Science eftersom analyser och maskininlärningsmodeller är beroende av den data som används. Felaktiga eller oväntade värden kan påverka resultatet och i förlängningen leda till felaktiga slutsatser. Genom att validera data kan vissa typer av problem upptäckas tidigare i ett dataflöde.

Området är därför relevant för Data Science-yrkesrollen eftersom en Data Scientist inte bara behöver analysera och modellera data, utan även behöver kunna arbeta med kvaliteten på den data som används. Pandera kan vara ett verktyg för att göra sådana kontroller mer strukturerade och återanvändbara i Python-baserade dataflöden.

## Viktiga begrepp
### DataFrameSchema
Ett **DataFrameSchema** används för att beskriva hur en pandas DataFrame förväntas vara uppbyggd och vilka regler datan ska följa. Schemat fungerar som en samlad beskrivning av datakvaliteten som ska kontrolleras.

### Column
**Column** används för att definiera regler för en specifik kolumn i DataFrame. Det kan exempelvis användas för att ange vilken datatyp kolumnen ska ha och vilka ytterligare kontroller som ska göras. I projektet används exempelvis **pa.Column(int)** för att ange att **age** ska innehålla heltal.

### Check
**Check** används för att definiera villkor som värden i en kolumn måste uppfylla. I projektet används exempelvis **pa.Check.between(18, 100)** för att kontrollera att åldrar ligger inom det definierade intervallet. För **purchase_amount** används **pa.Check.greater_than_or_equal_to(0)** för att förhindra negativa värden.

### Validation
Valideringen genomförs med **schema.validate(df)**. Då jämförs DataFrame mot reglerna i **DataFrameSchema**. Om datan uppfyller reglerna passerar valideringen. Om regler bryts rapporterar Pandera valideringsfel.

### lazy=True
Parametern **lazy=True** gör att Pandera samlar flera valideringsfel under samma validering istället för att rapportera det första felet direkt. Detta ger en bättre överblick över problemen i ett dataset och gör det möjligt att upptäcka flera fel samtidigt. 

### unique
**unique=True** används för att kontrollera att värdena i en kolumn är unika. I projektet används det på **customer_id** för att demonstrera hur Pandera kan upptäcka duplicerade värden.


## Genomförande
Jag började med att undersöka Pandera och hur biblioteket kan användas tillsammans med pandas för att validera data. Jag använde främst dokumentation och exempel för att förstå hur Pandera fungerar och vilka funktioner som var relevanta för projektet.

För att hålla projektet avgränsat valde jag att bygga en enkel lösning där en CSV-fil läses in som en pandas DataFrame och sedan valideras mot ett Pandera-schema. Jag skapade två dataset:ett med data som följer reglerna och ett med avsiktliga fel.

Jag började med en enkel schema-definition och testade bland annat hur Pandera kontrollerar datatyper. Därefter lade jag till olika regler för att kontrollera datan mer detaljerat. I projektet används bland annat:
- **int** för att kontrollera datatypen på **customer_id** och **age**
- **float** för datatypen på **purchase_amount**
- **Check.between(18, 100)** för att kontrollera åldersintervallet
- **Check.greater_than_or_equal_to(0)** för att förhindra negativa belopp
- **unique=True** för att kontrollera att **customer_id** inte innehåller duplicerade värden

Jag testade även skillnaden mellan vanlig validering och validering med **lazy=true**.

Slutligen skapade jag en funktion som läser in en CSV-fil och skickar DataFrame till schemat för validering. Jag testade funktionen på både den korrekta och den felaktiga datan. På så sätt kunde jag kontrollera att reglerna fungerade som förväntat och se hur Pandera rapporterar olika typer av fel.

## Resultat
Testerna visade att Pandera kunde upptäcka flera olika typer av fel i datan. När den korrekta CSV-filen validerades passerade datan schemat utan fel. När den felaktiga filen användes upptäcktes tre problem: ett duplicerat **customer_id**, en ålder på 17 år och ett negativt **purchase_amount** på -200.

Testerna visade att Pandera kunde upptäcka flera olika typer av fel beroende på vilken regel som bröts. Det blev också tydligt att olika valideringsregler leder till olika typer av valideringsfel.

Testerna visade även skillnaden mellan vanlig validering och validering med **lazy=True**. I testet med den felaktiga datan kunde flera problem identifieras samtidigt, vilket gav en tydligare bild av vilka regler som inte uppfylldes.

Jag fick även en bättre förståelse för Pandera valideringsfel. Olika regler kan ge olika typer av fel. Felmeddelandena innehåller information om vilken kolumn och vilken regel som inte uppfylldes. Detta var en av de delar som tog mest tid att förstå under projektet.

En viktig slutsats är att Pandera kan upptäcka om data bryter mot reglerna som har definierats, men Pandera kan inte själv avgöra om reglerna är rätt för verksamheten. Exempelvis kan **customer_id** vara unikt i detta testdataset, men om varje rad istället representerar ett köp kan samma kund förekomma flera gånger. Då skulle en unik order/transaktionsidentifierare vara mer lämplig.

Projektet gav därför en mer praktisk förståelse för hur Pandera kan användas för att göra datavalidering mer strukturerad och återanvändbar i ett Python-baserat dataflöde.

## Begränsningar och möjliga förbättringar
Projektet är medvetet litet och har därför flera begränsningar. Datan består endast av några få rader och reglerna är valda för att demonstrera Pandera funktioner. I ett verkligt dataflöde skulle det behövas fler och mer verksamhetsanpassade regler.

En viktig begränsning är att Pandera bara kan kontrollera de regler som har definierats. Biblioteket kan exempelvis upptäcka att en ålder är utanför intervallet 18-100, men kan inte själv avgöra om just det intervallet är rätt. Det är därför viktigt att valideringsreglerna bygger på en förståelse för den data och verksamhet som lösningen används för.

Även regeln **unique=True** för **customer_id** är en förenkling i projektet. Om varje rad representerar ett köp kan samma kund förekomma flera gånger. I ett sådant scenario skulle exempelvis ett **order_id** eller **transaction_id** kunna vara ett bättre fält att kontrollera som unikt.

En annan möjlig förbättring är att utveckla hur valideringsfelen hanteras. I projektet skrivs felmeddelandet ut i terminalen. I en större lösning skulle felen exempelvis kunna loggas, sparas eller användas för att stoppa ett dataflöde tills problemen har hanterats.

Jag skulle även kunna undersöka fler funktioner i Pandera. Ett naturligt nästa steg är att undersöka hur Pandera kan användas tillsammans med exempelvis preprocessing och andra delar av ett dataflöde. Det skulle ge en bättre bild av hur biblioteket kan användas i en mer komplett datapipeline.

Projektet hade också kunnat innehålla fler typer av valideringsregler och större dataset. Det hade gjort det möjligt att testa fler situationer och få en djupare förståelse för hur Pandera fungerar vid mer realistiska dataproblem.

## Koppling till yrkesrollen
Datavalidering är relevant för Data Scientist-rollen eftersom analyser och modeller är beroende av att den data som används håller tillräcklig kvalitet. En Data Scientist behöver därför inte bara kunna analysera data och bygga modeller, utan även kunna upptäcka och hantera problem i datan.

Pandera kan vara användbart i Python-baserade dataflöden där data behöver kontrolleras innan den används vidare. Genom att samla valideringsregler i ett schema blir reglerna tydligare och kan återanvändas när samma typ av data valideras flera gånger.

Jag ser även en koppling till arbete med datapipelines. Om data exempelvis hämtas från flera olika källor kan validering användas för att upptäcka oväntade värden eller förändringar innan datan går vidare till analys eller maskininlärning. Det kan minska risken för att felaktig data påverkar resultatet.

Projektet har därför gett mig en bättre förståelse för en del av Data Scientist-rollen som inte alltid handlar om själva modelleringen, men som är viktig för att kunna arbeta med data på ett tillförlitligt sätt.

## Källor
- Pandera Documentation. *Pandera documentation*.
https://pandera.readthedocs.io/
- Pandera Documentation. *Lazy validation*.
https://pandera.readthedocs.io/en/stable/lazy_validation.html
- Pandera Documentation. *Check*.
https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.checks.Check.html
- Pandera Documentation. *Column*
https://pandera.readthedocs.io/en/stable/reference/generated/pandera.api.pandas.components.Column.html

## Självreflektion
### 1. Vad lärde du dig som du inte kunde innan?
Jag lärde mig hur Pandera kan användas för att validera en Pandas DataFrame mot ett schema. Innan projektet hade jag inte arbetat med Pandera eller den här typen av strukturerad datavalidering. 

Jag lärde mig bland annat hur **DataFrameSchema**, **Column** och **Check** används tillsammans och hur olika regler kan användas för att kontrollera datatyper, intervall, negativa värden och duplicerade värden. Jag fick också en bättre förståelse för hur Pandera rapporterar olika typer av valideringsfel.

### 2. Vad var svårast att förstå eller genomföra?
Det svåraste var att förstå valideringsfelen och skillnaden mellan olika typer av fel. Genom att testa med och utan **lazy=True** kunde jag se skillnaden i praktiken och förstå varför parametern var användbar i projektet.

### 3. Vilket tekniskt val är du mest nöjd med och varför?
Det tekniska val jag är mest nöjd med är att använda **lazy=True** vid valideringen. Jag valde det eftersom jag ville kunna se flera problem i samma dataset samtidigt.

Det blev också ett bra sätt att undersöka Pandera praktiskt. När jag testade felaktig data kunde jag se att Pandera upptäckte duplicerat **customer_id**, en ålder utanför det tillåtna intervallet och ett negativt köpbelopp i samma validering. Det gjorde funktionen mer användbar för att undersöka datakvalitet.

### 4. Vad hade du gjort annorlunda om du började om?
Om jag började om hade jag planerat projektets omfattning lite tidigare och snabbare bestämt vilka delar av Pandera jag ville undersöka. Jag hade också kunnat lägga mer tid på att testa olika typer av valideringsfel från början.

Jag hade dessutom kunnat använda ett mer realistiskt dataset där exempelvis varje rad representerar ett köp. Då hade jag kunnat använda **order_id** eller **transaction_id** som unikt värde istället för **customer_id**, vilket hade gjort datamodellen mer realistisk. 

### 5. Vad skulle vara ett naturligt nästa steg om du fortsatte arbetet?
Ett naturligt nästa steg skulle vara att undersöka fler delar av Pandera och hur det kan användas i ett större dataflöde. Jag skulle framför allt vilja undersöka hur Pandera kan användas tillsammans med preprocessing och andra steg i en datapipeline.

Jag skulle även kunna testa lösningen med ett större och mer realistiskt dataset. Att Utveckla felhanteringen så att valideringsfel exempelvis loggas eller hanteras på ett mer automatiserat sätt hade också varit intressant att testa.

### 6. Vilket betyg tycker du själv att arbetet motsvarar – G eller VG?
Jag tycker att arbetet motsvarar VG.

### 7. Motivera din bedömning genom att koppla till kraven för G och VG nedan.
Jag anser att arbetet uppfyller kraven för G eftersom jag valt ett relevant område inom Python för Data Science, använt dokumentation för att lära mig ett nytt bibliotek och byggt en fungerande lösning. Jag kan även förklara de viktigaste delarna av koden och visa hur lösningen fungerar genom tester med korrekt och felaktig data.

Jag tycker även att arbetet når flera av kraven för VG. Jag har inte bara använt Pandera, utan undersökt hur och varför olika delar fungerar. Jag har exempelvis testat skillnaden mellan **SchemaError** och **SchemaErrors**, undersökt vad lazy=True innebär och resonerat kring varför **customer_id** kanske inte är ett lämpligt fält att kräva som unikt i ett verkligt dataset.

Jag har också kunnat resonera kring begränsningar och möjliga förbättringar. En viktig insikt är att Pandera inte själv kan avgöra vilka regler som är korrekta för verksamheten, utan bara kontrollera reglerna som utvecklaren har definierat. Jag har därför försökt koppla de tekniska valen till hur lösningen skulle kunna användas i ett verkligt dataflöde.

Samtidigt är projektet relativt litet och jag har inte undersökt alla möjligheter med Pandera. Min bedömning bygger därför främst på den förståelse, de tekniska resonemang och de tester jag genomfört, snarare än projektets storlek.