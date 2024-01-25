# finalproject
Proiectul e structurat în mai multe clase care modelează diferite aspecte ale unui sistem de cumpărături online, manipulare de șiruri de caractere, validare a datelor de intrare și interacțiune cu o bază de date. 
Fiecare clasă are un scop specific și împreună formează un sistem integrat. 

Mai jos e prezentată o descriere detaliată a fiecărei clase și a scopului lor în cadrul scenariilor acoperite:

 - Pentru operații matematice de bază - Clasa Calculator: Această clasă oferă funcționalități de bază pentru operații matematice: adunare, scădere, înmulțire și împărțire. Este concepută pentru a manipula numere și a trata cazuri specifice, cum ar fi împărțirea cu zero.

 - Pentru manipularea șirurilor de caracter - Clasa StringManipulation: Această clasă este destinată manipulării șirurilor de caractere. Ea poate inversa un șir, capitaliza primul caracter și verifica dacă un șir este un palindrom.

 - Pentru validarea datelor de intrare ale utilizatorilor în scenariul unei logări în sistem - Clasa UserInputValidation: Aceasta gestionează validarea datelor de intrare pentru nume de utilizator și parole. Se asigură că numele de utilizator și parola respectă anumite criterii de lungime și compoziție.

 - Pentur gestionarea coșului de cumpărături - Clasa ShoppingCart: Modelează un coș de cumpărături într-un magazin online. Permite adăugarea, eliminarea și interogarea cantităților de articole.

 - Pentru autentificarea utilizatorilor - Clasa UserAuthentication: Gestionează autentificarea utilizatorilor. Verifică dacă numele de utilizator și parola corespund celor stocate în sistem.

 - Pentru fluxul de cumpărături online - Clasa OnlineShopping: Aceasta este o clasă centrală pentru cumpărăturile online, integrând interacțiunea cu clasele ce gestionează coșul de cumpărături și autentificarea utilizatorilor. Aceste două clase externe sunt instanțiate în constructor, pentru a se realiza ulterior diferite operații în cadrul metodelor clasei OnlineShopping. Sunt incluse metode pentru adăugarea și eliminarea articolelor din coș și pentru validarea autentificării utilizatorilor, abstractizând interacțiunea cu aceste două clase "helper" ShoppingCart și UserAuthentication.

 - Pentru interacțiunea cu baza de date - Clasa DatabaseInteraction: Simulează interacțiunea cu o bază de date, gestionând informații despre utilizatori și produse, precum și actualizarea stocului de produse.

 - Pentru scenariul integrării cu un sistem de facturare - Clasa BillingSystem: Gestionează facturarea, permițând adăugarea și eliminarea articolelor dintr-o factură, calcularea totalului, aplicarea reducerilor și taxelor.

 - Pentru managementul utilizatorilor logați în cadrul sistemului simulat - Clasa UserManagement: Se ocupă de administrarea utilizatorilor, inclusiv înregistrarea, ștergerea și obținerea informațiilor despre aceștia.

 - Pentru gestionarea produselor - Clasa Product: Modelează un produs, cu proprietăți precum nume și preț, oferind și metode pentru actualizarea prețului.

 - Pentru managementul comenzilor - Clasa OrderManagement: Gestionează comenzile plasate de utilizatori, integrând sistemul de facturare și managementul utilizatorilor. Permite plasarea, anularea și obținerea comenzilor, precum și procesarea plăților.

Pe lângă aceste clase, codul include și o serie de funcții de testare pentru fiecare clasă, asigurându-se că metodele implementate funcționează corect. 
Aceste teste verifică comportamentul așteptat al metodelor din fiecare clasă, folosind aserțiuni pentru a confirma rezultatele.

Codul prezet nu include referințe directe la framework-uri externe; este scris  folosind doar funcționalitățile și structurile de bază ale limbajului de programare Python în forma sa pură.
Totuși, proiectul în sine este structurat într-o manieră ce ar putea fi ușor adaptată sau integrată în cadrul unor framework-uri populare. Spre exemplu:
 
 - Unit Testing Framework-uri (ex. Pytest, Unittest în Python): Proiectul acordă importanță asigurării calității, iar un framework de testare unitară cum ar fi Pytest sau Unittest ar putea fi folosit pentru a structura și a rula aceste teste într-un mod mai eficient și mai sistematic. 
 
 - Web Framework-uri (ex. Flask, Django): Clasele precum OnlineShopping, UserAuthentication, ShoppingCart, UserManagement, și OrderManagement ar putea fi integrate într-un framework web pentru a crea o aplicație complet funcțională de cumpărături online. 


În ceea ce privește logica aplicată proiectului s-au avut în vedere urmarea urătoarelor principii:

 - Separarea Responsabilităților: Fiecare clasă are un rol specific și bine definit (de exemplu, Calculator pentru operații matematice, UserManagement pentru gestionarea utilizatorilor).

 - Modularitate: Codul este structurat modular, ceea ce face fiecare componentă ușor de întreținut și de extins. De exemplu, clasa ShoppingCart poate fi modificată sau înlocuită independent de restul sistemului.

 - Orientarea pe Obiect: Proiectul urmează principiile programării orientate pe obiect, cu clase care encapsulează date și metode specifice.

 - Reutilizabilitatea Codului: Prin definirea unor clase cu scopuri clare și bine definite, proiectul facilitează reutilizarea codului în diferite părți ale aplicației sau chiar în proiecte viitoare.

 - Testare Unitară: Prezența testelor unitare pentru fiecare clasă subliniază o abordare de dezvoltare care accentuează asigurarea calității și prevenirea erorilor.


Aceste scenarii reflectă un sistem care ar putea fi folosit într-o aplicație reală de cumpărături online, oferind o infrastructură pentru autentificarea și gestionarea utilizatorilor, operațiuni pe coșul de cumpărături, procesarea plăților și gestionarea comenzilor. 
De asemenea, demonstrează bune practici de programare, cum ar fi: modularitatea, testarea unitară și separarea responsabilităților.
