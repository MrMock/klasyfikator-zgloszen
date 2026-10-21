"""Druga część przykładowych zgłoszeń. Treść bywa niejednoznaczna, ale w bazie nie ma etykiety."""

from app.samplelib import z

TICKETS = [
    z(
        "Nie wejdę do SAP, pisze że złe hasło",
        """Od rana SAP wyrzuca, że nazwa lub hasło jest nieprawidłowe. Do Windowsa loguję się tym samym hasłem bez problemu, poczta też wstaje. Wczoraj SAP jeszcze się otwierał. Nie wiem, czy zablokowało mi tylko SAP, czy system księgowy leży i pokazuje zły komunikat, bo koleżanka z przeciwka mówi, że jej też raz przeklikało, a potem weszła. Ja po trzech próbach przestałam, faktury stoją.""",
        "2026-10-15 08:26",
    ),
    z(
        "outlook ciagle pyta o haslo",
        """wchodze do windowsa normalnie, a outlook co chwila wyskakuje z okienkiem na haslo. wpisuje to co zawsze, na sekunde znika i wyskakuje znowu. poczty nie widze. w przegladarce na stronie poczty tym samym haslem wchodze. moze sie outlook zepsul, a moze haslo do poczty jest inne i sam sobie nakrecilem. nie chce tego zablokowac.""",
        "2026-09-21 08:19",
    ),
    z(
        "VPN nie przyjmuje hasła, w biurze wszystko działa",
        """Jestem w domu. VPN pyta o hasło, wpisuję to samo, którym minutę wcześniej odblokowałam laptopa, i jest komunikat, że uwierzytelnienie się nie powiodło. Po dwóch próbach nie próbuję dalej. W biurze w piątek VPN nie był mi potrzebny, na miejscu dyski były bez niego. Nie wiem, czy do VPN jest osobne hasło, czy konto blokuje się tylko na tej usłudze.""",
        "2026-08-18 07:58",
    ),
    z(
        "VPN przyjął hasło, ale nie mogę zatwierdzić logowania",
        """Hasło do VPN przechodzi, a potem ma wyskoczyć zatwierdzenie w telefonie. Telefon służbowy leży obok, jest sieć, aplikacja Authenticator jest, tylko prośba nie przychodzi. Czekam kilka minut, ponawiam i dalej cisza. Z biura, bez VPN, pracuję normalnie. Dziś cały dzień z domu i bez tego nie zobaczę dysku P.""",
        "2026-07-14 08:08",
    ),
    z(
        "Nowy telefon, nie mam kodów i nie działa poczta w telefonie",
        """Wczoraj dostałam zastępczy telefon, bo stary oddałam do wymiany szybki. Na tym nowym nie przeniesiono niczego. Nie mam Authenticatora, więc nie wejdę do VPN, i nie mam poczty w aplikacji na telefonie, a klienci piszą też tam. Nie wiem, czy to jest zgłoszenie o ustawienie telefonu, czy o kody do logowania. Jedno i drugie blokuje mi wyjazd do klienta po południu.""",
        "2026-09-29 10:06",
    ),
    z(
        "Mail od działu IT, czy to Wy?",
        """Dostałem wiadomość z prośbą o weryfikację skrzynki i linkiem. Nadawca wyświetla się jako Dział IT, ale jak najechałem na adres, to było it@meridian-support.example, a my jesteśmy na meridian.example. Nie klikałem. Możecie powiedzieć, czy to Wasza wiadomość, czy mam ją skasować? Leży w skrzynce odbiorczej, nie w spamie. Załącznika nie było, tylko link.""",
        "2026-06-11 09:46",
    ),
    z(
        "Hasło przestało działać zaraz po dziwnym mailu",
        """Koło 14:30 dostałam maila, że wykryto logowanie, i żebym kliknęła, jeśli to nie ja. Nie jestem pewna, czy klikałam. Chyba tylko podgląd w okienku Outlooka. Od tamtej pory nie wejdę do poczty w przeglądarce, hasło odrzuca, a do Windowsa jeszcze wchodzę, bo byłam zalogowana. Nie wiem, czy ktoś mi je zmienił, czy ja coś zatwierdziłam. Trochę się pogubiłam, przepraszam, że chaotycznie.""",
        "2026-10-16 15:12",
    ),
    z(
        "Outlook zawiesza się przy starcie, Word działa",
        """Po włączeniu komputera Outlook otwiera okno i pasek przetwarzania zostaje na stałe. Po 10 minutach zamykam go przez menedżer zadań. Word i Excel otwierają pliki normalnie, konto pakietu jest zalogowane. Na stronie poczty w przeglądarce maile widzę, więc serwer chyba żyje. Wygląda to albo na sam program Outlook, albo na coś w pakiecie, bo wczoraj wieczorem Office sam się aktualizował.""",
        "2026-07-08 10:34",
    ),
    z(
        "Przy odbieraniu poczty staje cały komputer",
        """Jak Outlook zaczyna pobierać pocztę, komputer na kilka minut przestaje reagować. Mysz skacze, da się klikać dopiero jak skrzynka doleci. Bez Outlooka, zaraz po zalogowaniu, laptop jest w porządku, Excel chodzi. Skrzynka jest duża, trzymam tam projekty. Nie wiem, czy to poczta tak muli, czy komputer już nie wyrabia i tylko przy poczcie to widać.""",
        "2026-09-04 08:50",
    ),
    z(
        "W biurze sieć się rwie, a z domu nie ma VPN",
        """Dwa problemy i nie wiem, który zgłaszać. W biurze od wczoraj Wi-Fi Meridian łączy się i po minucie znika, na kablu jest lepiej, ale też raz zerwało. W domu wieczorem chciałem dokończyć rzecz na VPN i VPN w ogóle nie wstał, został na oczekiwaniu. Film na tym samym łączu domowym działał. Mogę jutro zostać w biurze, jeśli tak łatwiej to zobaczyć, ale na dziś nie mam jak stabilnie pracować ani tu, ani tam.""",
        "2026-06-05 09:40",
    ),
    z(
        "Po włączeniu VPN nie da się pracować",
        """Bez VPN laptop działa normalnie. Jak zestawię VPN, wszystko staje się kilka razy wolniejsze: otwarcie dysku P trwa minutę, Teamsy na firmowym koncie się tną, nawet lokalny notatnik długo wstaje. Jak rozłączę VPN, znowu jest w porządku. Zwykłe strony na VPN też ledwo idą. Nie wiem, czy tunel jest źle ustawiony, czy komputer nie wyrabia, kiedy VPN działa w tle.""",
        "2026-08-27 13:06",
    ),
    z(
        "Nie ma sieci i drukarka też leży",
        """Na 2. piętrze od rana nie mam sieci: ani Wi-Fi, ani kabel przy biurku, ikonka mówi o braku dostępu. Drukarka przy kuchni, ta HP, jest na panelu offline i nikt na piętrze nie wydrukował od 8:30. Pewnie to przez sieć, ale piszę o obu, bo listy przewozowe miały iść przed południem, a jak sieć wróci, a drukarka zostanie, to i tak stoimy.""",
        "2026-07-10 11:19",
    ),
    z(
        "Na kolorowej pisze brak dostępu, na zwykłej drukuje",
        """Na drukarce czarno-białej przy kadrach drukuję normalnie. Jak wybieram kolorową przy marketingu, zlecenie od razu wraca z komunikatem o braku dostępu, po angielsku access denied, nie offline i nie zacięcie. Kierownik mówił, że kolorowa jest dla nas otwarta, bo drukujemy okładki ofert. Może ktoś zdjął mi uprawnienie, a może ta drukarka tak nazywa zwykłą awarię.""",
        "2026-09-17 10:47",
    ),
    z(
        "lapek wolny, goracy i gasnie na teamsach",
        """nie wiem jak to nazwac. na poczatku dnia jest ok, po godzinie wentylator wyje, obudowa ciepla i wszystko muli, a jak dlugo trwa spotkanie na teamsach to raz juz sam sie przeladowal. niebieski ekran nie wyskoczyl. po przeladowaniu znowu przez chwile jest ok i wraca to samo. moze mu sie konczy zyciorys, a moze tylko cos zarlo w tle. nie chce oddawac sprzetu jak to program, bo jutro jade do klienta.""",
        "2026-08-14 15:33",
    ),
    z(
        "Przy stacji dokującej laptop nie ładuje, monitory migają",
        """Jak wpinam laptopa w swoją stację, monitory łapią sygnał na sekundę i gasną, a bateria nie ładuje. Mój laptop na stacji kolegi ładuje i pokazuje obraz. Laptop kolegi wpięty w moją stację też nie ładuje i monitory gasną. Własny zasilacz laptopa działa. Wczoraj ta stacja jeszcze była dobra, nic przy biurku nie przestawiałam.""",
        "2026-06-19 08:42",
    ),
    z(
        "PDF-y otwierają się w Wordzie i od razu błąd",
        """Jak klikam PDF z maila, otwiera się Word i krzyczy, że plik jest uszkodzony. W przeglądarce ten sam PDF widać normalnie. Chyba nie mam czytnika i Windows podstawia Worda. Da się dołożyć normalną przeglądarkę PDF? Z drugiej strony może pakiet się rozjechał, bo jeszcze w zeszłym miesiącu PDF otwierał się w osobnym okienku, nie w Wordzie. Nic świadomie nie zmieniałam.""",
        "2026-09-08 12:12",
    ),
    z(
        "Excel z dysku sieciowego nie otwiera się tylko u mnie",
        """Plik raportu tygodniowego na dysku sprzedaży u koleżanki się otwiera. U mnie Excel najpierw pisze, że plik jest zablokowany do edycji przez innego użytkownika, choć ona go już zamknęła, a przy drugiej próbie, że wykryto błąd w pliku. Kopia, którą zgrałem na pulpit, otwiera się od razu. Nie wiem, czy zepsuł się udział, czy mój Excel źle czyta pliki z sieci. Reszta plików z tego folderu, głównie PDF, otwiera się.""",
        "2026-07-31 09:58",
    ),
    z(
        "nie widze folderu projektu a inni widza",
        """hej, podobno wrzucili mi rysunki do akustyki w projekcie Atrium na dysku P, ale ja tego folderu nie widze w ogole. nie ma komunikatu o braku dostepu, po prostu konczy sie na poprzednim numerze. Ewa mowi ze u niej folder jest i ma 2 GB. moze mi sie nie zmapowalo, a moze nie mam uprawnien i windows go chowa. dysk P widze, inne projekty tez. potrzebuje tego na dzisiaj, bo akustyka dzwoni po poludniu.""",
        "2026-08-21 10:16",
    ),
    z(
        "SAP wpuszcza, ale transakcji do faktur nie mam",
        """Logowanie do SAP przechodzi, kod z telefonu też. Jak wpisuję FB60, dostaję komunikat: brak uprawnień do transakcji FB60. Nie wygląda to jak awaria ekranu, po prostu mnie nie wpuszcza dalej. Księgowość mówi, że rolę powinienem mieć od przeniesienia w czerwcu i że u nich FB60 działa, łącznie z zapisem dokumentu. Proszę o nadanie albo o sprawdzenie, czy rola się nie zdjęła. Jak to jednak błąd SAP-a, to też dajcie znać, bo komunikat jest bardzo krótki.""",
        "2026-06-24 11:41",
    ),
    z(
        "Drugi dzień, mam komputer, nie mam dysku ani grupy",
        """Dzień dobry, wczoraj dostałem laptopa i konto, do Windowsa wchodzę. Nie widzę dysku P. Outlook ma tylko moją skrzynkę, bez skrzynki zespołu oferty. Kierownik mówił, że wszystko będzie nadane. Nie wiem, czy moje stanowisko jest jeszcze nieprzygotowane, czy mam osobno prosić o każdy dostęp. Na liście pracowników w Teamsach już jestem. Nazywam się Leon Grabowski, sprzedaż, pokój 208.""",
        "2026-09-30 08:15",
    ),
    z(
        "Konto jest, ale poczta mówi, że skrzynka nie istnieje",
        """Zaczęłam 1 września, do komputera się loguję, Teams działa. Outlook przy starcie pisze, że skrzynka zuzanna.olczyk@meridian.example nie istnieje na serwerze albo nie mam do niej uprawnień. W Teamsach mogę pisać na czacie. Maile od opiekuna podobno wychodzą i wracają. Czy skrzynka w ogóle została założona, czy tylko konto do Windowsa?""",
        "2026-09-11 09:24",
    ),
    z(
        "W Teamsach cisza, a na telefonie Teams się nie loguje",
        """Na laptopie Teams wstaje, ale na spotkaniu jest kompletna cisza w dwie strony, choć suwak nie jest wyciszony. Słuchawki w odtwarzaczu muzyki grają. Na służbowym telefonie chciałem wejść w to samo spotkanie i aplikacja Teams wyrzuca mnie do ekranu logowania, kręci się i wraca. Telefon poza tym dzwoni normalnie. Za 25 minut mam drugą rozmowę z klientem.""",
        "2026-10-08 16:18",
    ),
    z(
        "Kamera nie działa, w Teamsach i w Windowsie czarno",
        """Na spotkaniu Teams kamera pokazuje czarny obraz. Lampka przy obiektywie się nie zapala. Otworzyłam aplikację Aparat w Windowsie i tam też jest czarno, więc to chyba nie sam Teams, ale wolę napisać, bo problem wyszedł na spotkaniu i ludzie mówią, żebym wyłączyła kamerkę w Teamsach. Zewnętrznej kamery nie mam, tylko ta w laptopie. Restart nie pomógł.""",
        "2026-07-17 09:05",
    ),
    z(
        "po zalaczniku komputer zwariowal",
        """otworzylem excel od goscia ktorego nie znam, mial przyjsc harmonogram platnosci. od tamtej chwili komputer strasznie muli, wyskakuja jakies okna na ulamek sekundy i antywirus cos pisze, ale znika zanim przeczytam. excel tego pliku juz nie ma na pulpicie, sam zniknal. nie wiem czy to wirus czy po prostu zawieszenie, bo komputer i wczesniej potrafil zamulic. hasla nie wpisywalem nigdzie. troche mnie skreca, szczerze.""",
        "2026-08-07 11:27",
    ),
    z(
        "Ze mnie wychodzą maile, których nie pisałam",
        """Kontrahent odesłał mi wiadomość, którą rzekomo wysłałam w nocy, z linkiem do zaktualizowania danych do przelewu. Nie pisałam tego. W wysłanych tego maila nie widzę. Hasło do poczty dziś rano weszło normalnie, do komputera też. Outlook działa jak zwykle, nic nie muli. Bardzo proszę o sprawdzenie, czy ktoś nie wysyła z mojego adresu, i o informację, co zmienić. Na razie nikomu nie odpisuję.""",
        "2026-06-01 08:21",
    ),
    z(
        "Word mówi, że plik na dysku wspólnym jest uszkodzony",
        """Otwieram aneks umowy na dysku kancelarii i Word pisze, że w pliku znalazł uszkodzoną zawartość i próbuje odzyskać. Odzysk wychodzi pusty. Wczoraj aneks był dobry, poprawiała go kancelaria i ja go jeszcze zamykałem. U mecenas na zewnętrznej skrzynce podobno otwiera się ostatnia wersja, którą jej wysłałem mailem. Na dysku została nowsza, z uwagami z wczoraj, i tej nie mogę ruszyć. Inne dokumenty z tego folderu, starsze, otwierają się.""",
        "2026-09-23 13:52",
    ),
    z(
        "Formularz delegacji otwiera się, zapis odmawia",
        """Na portalu pracowniczym wchodzę w delegacje, formularz się wyświetla, wypełniam go i przy zapisie dostaję czerwoną linijkę, że brak uprawnień do zapisania dokumentu. Strona nie zwraca błędu 500, nie znika menu, inne osoby z zespołu podobno zapisują delegacje dziś. Moje konto na portalu jest zalogowane, widzę swoje stare delegacje z czerwca. Nie wiem, czy zdjęto mi prawo do nowych, czy formularz jest zepsuty tylko na zapisie.""",
        "2026-10-02 14:08",
    ),
    z(
        "Wniosek urlopowy kręci się i nie wpada do kadr",
        """Składam urlop z portalu pracowniczego. Przycisk Złóż kręci się i po chwili wraca ten sam formularz, bez numeru wniosku i bez komunikatu. W aplikacji kadr na pulpicie, tam gdzie widać wnioski, tego urlopu nie ma. Koleżanka złożyła urlop z tej samej strony godzinę temu i jej się pojawił. U mnie i portal nie domyka, i w kadrach pusto. Nie wiem, czy to iść do strony, czy do systemu kadr.""",
        "2026-07-15 12:22",
    ),
    z(
        "Osoba po odejściu nadal widzi folder z danymi",
        """Radosław Kruk odszedł od nas w czerwcu, a dziś przy pliku ofert na dysku P widzę w historii, że otwierał go wczoraj o 21:14. Konto podobno miało być wyłączone. Nie wiem, czy ktoś nie założył mu dostępu na nowo, czy odejście nie zostało dokończone i konto żyje. Proszę to zabrać, w folderze są stawki. Ja dostęp mam i mieć powinnam, nie zgłaszam braku swoich uprawnień.""",
        "2026-08-04 09:37",
    ),
    z(
        "Nie zainstaluję programu, Windows pyta o hasło administratora",
        """Kierownik kazał dziś zainstalować program do podglądu rysunków DWG, bo klient przysłał pliki, których nie otworzę. Ściągnąłem instalator ze strony, którą IT podało w zeszłym roku na intranetie, i przy uruchomieniu Windows pyta o hasło administratora. Nie mam go i nie będę zgadywał. Czy macie mi to zainstalować, czy muszę dostać uprawnienie administratora na laptopie? Na SAP i na dyski wchodzę normalnie, tu chodzi tylko o instalację.""",
        "2026-09-15 15:44",
    ),
]
