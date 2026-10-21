"""Pierwsza część przykładowych zgłoszeń. W rekordzie jest temat, treść i data."""

from app.samplelib import z

TICKETS = [
    z(
        "Hasło do Windowsa wygasło",
        """Dzień dobry,
od dziś rana przy logowaniu wyskakuje, że hasło wygasło i muszę ustawić nowe. Wpisałam już trzy warianty, za każdym razem jest informacja, że hasło nie spełnia wymagań, ale bez listy tych wymagań. Siedzę w biurze, budynek B, i nie mogę wejść nawet do pulpitu.
Proszę o reset albo o podanie zasad, bo o 9:00 mam zamknięcie miesiąca z księgowością.
Anna""",
        "2026-10-20 08:14",
    ),
    z(
        "konto zablokowane",
        """zablokowalo mi konto. wpisywalem haslo z capsem i teraz jest komunikat: skontaktuj sie z administratorem, konto zablokowane. da sie to zdjac na juz? za 20 minut mam spotkanie z klientem i nie wejde nawet do teamsow. login p.wojcik
pisze z telefonu z recepcji, bez polskich znakow, klawiatura mi sie nie przelaczyla""",
        "2026-10-16 09:06",
    ),
    z(
        "Po urlopie nie wchodzę do laptopa",
        """Wracam dziś po dwóch tygodniach urlopu i hasło, które miałam zapisane w kopercie, nie przechodzi. Podejrzewam, że wygasło, kiedy mnie nie było. Laptop służbowy, jestem na 3. piętrze przy recepcji, mogę podejść do Was z dowodem, jeśli tak trzeba.""",
        "2026-09-28 11:40",
    ),
    z(
        "Prośba o reset hasła do konta",
        """Poproszę o zresetowanie hasła do konta domenowego t.lis. Od południa nie mogę się zalogować, komunikat mówi wprost, że nazwa użytkownika lub hasło jest niepoprawne. Nie chcę próbować dalej, żeby tego nie zablokować. Jestem dziś na home office, telefon służbowy działa, można dzwonić.""",
        "2026-08-11 14:22",
    ),
    z(
        "Hasło odrzuca, a wczoraj działało",
        """Wczoraj wieczorem normalnie wyłączyłam komputer. Dziś rano to samo hasło nie wchodzi. Caps Lock sprawdzony, w haśle nie ma cyfr, które dałoby się pomylić z literami, i na klawiaturze numerycznej nic nie świeci. Po dwóch próbach przestałam klikać. Komputer to stacjonarny w pokoju sprzedaży.""",
        "2026-07-03 08:47",
    ),
    z(
        "Po weekendzie nie wejdę do systemu",
        """Po weekendzie nie wejdę do systemu. Komunikat: nazwa użytkownika lub hasło jest niepoprawne. Obok mnie Kasia z HR loguje się na swoim koncie bez problemu, więc raczej nie padła cała domena. Konto a.nowicki. Stoję przy biurku, jeśli ktoś może podejść.""",
        "2026-06-15 08:09",
    ),
    z(
        "Authenticator zniknął po wymianie telefonu",
        """W zeszłym tygodniu dostałam nowy telefon służbowy i oddałam stary. Na nowym nie ma aplikacji z kodami. Hasło do Windowsa działa, problem zaczyna się przy poczcie i przy VPN: system prosi o zatwierdzenie w aplikacji, której nie mam. Da się to przepiąć dziś? Bez poczty nie ogarnę ofert.""",
        "2026-10-19 08:31",
    ),
    z(
        "Nie dochodzi SMS z kodem",
        """Loguję się do portalu pracowniczego, hasło przyjmuje, a potem prosi o kod SMS. Wiadomość nie przychodzi. Prośbę wysłałem trzy razy, czekam łącznie jakieś dwadzieścia minut. Numer się nie zmieniał. Bez tego kodu nie zatwierdzę wniosków zakupowych, a dział zakupów czeka na dwie akceptacje.""",
        "2026-09-02 13:18",
    ),
    z(
        "Kod z aplikacji się nie zgadza",
        """Wpisuję kod z Authenticatora do logowania VPN i za każdym razem jest informacja, że kod jest nieprawidłowy, choć zdążam w czasie. Godzina na telefonie wygląda normalnie. Hasła nie zmieniałam. Na komputerze w biurze, bez VPN, jestem zalogowana. Chodzi tylko o tę drugą weryfikację, a dziś pracuję z domu.""",
        "2026-07-21 09:55",
    ),
    z(
        "Outlook nie wysyła maili",
        """Od rana maile wychodzące zostają w skrzynce nadawczej. Przychodzące widzę. Przy próbie wysłania jest błąd 0x800CCC0E, chyba coś z serwerem. Pilne są dwie wiadomości do klienta z wyceną. Mogę je wysłać z telefonu, ale wolałbym nie, bo załączniki są na dysku. Konto j.pawlak.""",
        "2026-10-15 10:12",
    ),
    z(
        "Skrzynka pełna, nie mogę odebrać poczty",
        """Outlook pisze, że skrzynka jest pełna i nie pobierze nowych wiadomości. Kasowałam już duże załączniki i opróżniłam elementy usunięte, a dalej jest ponad limit. Potrzebuję albo zwiększenia skrzynki, albo wskazówki, co jeszcze ją zapycha, bo czekam na umowę od kancelarii.""",
        "2026-09-14 08:22",
    ),
    z(
        "Klient mówi, że nie dostał odpowiedzi",
        """Wysłałem wczoraj ofertę na adres, z którego klient do mnie napisał. U mnie w elementach wysłanych jest, załącznik ma 2 MB. Klient twierdzi, że nic nie doszło, sprawdził też spam. Do innych osób z firmy maile dzisiaj wychodzą, bo koleżanka dostała ode mnie test. Da się sprawdzić, czy to nie utknęło po naszej stronie?""",
        "2026-08-24 11:05",
    ),
    z(
        "Firmowe maile wpadają mi do spamu",
        """Część maili od działu kadr i z naszego newslettera ląduje w spamie, nie w skrzynce odbiorczej. Nie wyglądają podejrzanie, nadawca jest z domeny meridian.example. Da się to jakoś odhaczyć, żebym nie przegapiała grafiku? Nie klikałam w nic dziwnego, chcę tylko wyjątek w filtrze.""",
        "2026-07-13 09:41",
    ),
    z(
        "Zniknęła skrzynka współdzielona księgowości",
        """Do piątku widziałem w Outlooku skrzynkę faktury@meridian.example. Dziś jej nie ma na liście folderów. Na ten adres nadal przychodzą maile, bo księgowa na swoim komputerze je widzi. Mi zostało tylko własne konto. Nie proszę o nowe uprawnienia, wcześniej tę skrzynkę miałem, po prostu zniknęła z Outlooka po restarcie.""",
        "2026-06-22 15:16",
    ),
    z(
        "Załącznik 30 MB nie chce wyjść",
        """Próbuję wysłać klientowi paczkę zdjęć realizacji, około 30 MB, jeden plik zip. Outlook od razu pisze, że załącznik przekracza dozwolony rozmiar. Da się to puścić inaczej, jakimś linkiem firmowym, czy macie limit i tyle? Na zewnętrzny transfer wolałabym nie wrzucać zdjęć z budowy.""",
        "2026-06-08 12:33",
    ),
    z(
        "vpn z domu nie laczy",
        """hej, od 7:30 probuje odpalic vpn i wyrzuca ze serwer nie odpowiada. hasla nawet nie pyta, pada wczesniej na laczeniu. net w domu dziala, film na telefonie idzie. jestem na home office caly dzien, bez vpn nie wejde na dysk z ofertami. laptop ten sam co zawsze.""",
        "2026-10-13 08:05",
    ),
    z(
        "VPN rozłącza co kilka minut",
        """Połączenie VPN wstaje, wchodzę na dysk i po trzech–czterech minutach zrywa. Łączę ponownie i znowu to samo. Na Teamsach, które idą bez VPN, rozmowa trwa, więc domowy internet raczej nie pada całkowicie. Pracuję dziś z domu, pliki mam na dysku P i przy każdym zerwaniu Excel krzyczy, że utracił połączenie.""",
        "2026-09-09 10:44",
    ),
    z(
        "VPN krzyczy o certyfikacie",
        """Przy uruchamianiu klienta VPN jest komunikat, że certyfikat jest nieważny albo nie można sprawdzić wystawcy. Nic nie klikałem mimo to, bo nie wiem, czy to bezpieczne. W zeszłym miesiącu łączyło się bez tego okna. Jestem w biurze, ale i tak potrzebuję VPN do środowiska testowego.""",
        "2026-08-05 09:12",
    ),
    z(
        "Po aktualizacji Windowsa VPN w ogóle nie wstaje",
        """W piątek wieczorem komputer sam się zaktualizował. Dziś rano ikona VPN jest, ale po kliknięciu Połącz nic się nie dzieje, pasek kręci się minutę i wraca do stanu rozłączony. Inne osoby na spotkaniu porannym mówiły, że im VPN działa, więc to chyba ten laptop po aktualizacji. Home office.""",
        "2026-06-29 08:58",
    ),
    z(
        "W sali Kopernik nie ma sieci",
        """Siedzimy w sali Kopernik z klientem i firmowe Wi-Fi Meridian jest na liście, łączy się i po chwili rozłącza. Na kablu przy stole konferencyjnym też nie ma sieci, lampka w laptopie od gniazdka nie miga. Na 2. piętrze przy biurkach u mnie działa. Da się coś zrobić w trakcie spotkania? Zostaje nam hotspot z telefonu.""",
        "2026-10-08 11:27",
    ),
    z(
        "nie widze wifi w biurze",
        """przyszlam do biura i laptop nie widzi sieci Meridian. kolezanka z biurka obok ma to samo, jej telefon tez nie lapie Meridian, a w domu oba lapia nasze domowe wifi. siedze na 2 pietrze przy oknie. restart nic nie dal. da sie to zglosic jako awarie sieci? bo pol pietra chyba stoi.""",
        "2026-09-03 08:36",
    ),
    z(
        "Kabel w biurze jest, internetu nie ma",
        """Podłączyłem się kablem przy biurku 214. Windows pokazuje sieć niezidentyfikowaną i brak dostępu do internetu. Wi-Fi na tym samym laptopie łapie Meridian i na Wi-Fi strony się otwierają. Wygląda na gniazdko albo switch przy naszym rzędzie, bo sąsiad z 215 ma to samo na kablu.""",
        "2026-07-28 14:05",
    ),
    z(
        "Hasło do sieci dla gościa",
        """O 13:00 mam w sali konferencyjnej audytora, który prosi o Wi-Fi tylko do poczty. Nie chcę mu dawać hasła do sieci Meridian. Czy jest jeszcze sieć gościnna i kto wydaje do niej hasło na jeden dzień?""",
        "2026-06-18 09:20",
    ),
    z(
        "drukarka przy kuchni znowu offline",
        """ta hp przy kuchni na 2 pietrze znowu swieci sie na offline. z mojego kompa i z kompa Asii to samo. kartki sa, kabel z tylu wpiety. wczoraj drukowala. jak ktos bedzie w okolicy to niech ja kopnie, bo musze wydrukowac listy przewozowe, a nie bede latal na 1 pietro.""",
        "2026-10-14 09:48",
    ),
    z(
        "Zacięcie, którego nie umiem wyciągnąć",
        """Drukarka w pokoju kadr, ta mniejsza przy oknie, zatrzymała się w połowie i pisze o zacięciu. Otworzyłam klapę, kartki nie widzę, a jak zamykam, błąd wraca. Nie chcę szarpać na siłę. Są tam dokumenty z danymi pracowników, więc wolę, żeby wyciągnął to ktoś od Was, a nie żebym zostawiła to w połowie.""",
        "2026-09-16 10:02",
    ),
    z(
        "Drukuje puste strony",
        """Od południa zlecenia schodzą z kolejki, drukarka pisze, że drukuje, a wychodzą białe kartki. Toner podobno był wymieniany w zeszłym tygodniu, na obudowie jest karteczka z datą 10.08. Drukarka stoi przy sekretariacie, ta duża. Skanowania jeszcze nie sprawdzałam, potrzebuję najpierw druku umów.""",
        "2026-08-17 13:44",
    ),
    z(
        "Wszystko leci na złą drukarkę",
        """Po wymianie laptopa domyślną drukarką został wydruk do PDF-a i co chwilę tam wraca. HP przy sprzedaży jest na liście, tylko nie jest domyślna. Da się to przypiąć na stałe, tak jak miałem na starym komputerze? Samo drukowanie na tej HP działa, jak ją ręcznie wybiorę.""",
        "2026-07-16 15:38",
    ),
    z(
        "Skaner nie widzi komputera",
        """Skaner przy sekretariacie, ten z podajnikiem, nie wysyła skanu na mój komputer. Wybieram siebie z książki adresowej na panelu i po chwili jest komunikat, że nie można się połączyć. Drukowanie z laptopa na tej samej maszynie działa. Potrzebuję dziś zeskanować podpisane protokoły, około 20 stron.""",
        "2026-06-10 11:51",
    ),
    z(
        "Laptop nie wstaje, tylko czarny ekran",
        """Po otwarciu klapy ekran jest czarny, wentylator kręci się chwilę i cichnie. Lampka zasilania miga na bursztynowo. Podłączyłem zasilacz, który świeci, i trzymałem przycisk zasilania ze dwadzieścia sekund. Nic. W piątek wieczorem normalnie go hibernowałem, w weekend leżał w szufladzie. Jestem w biurze, mogę go podrzucić.""",
        "2026-10-12 08:17",
    ),
    z(
        "Laptop nie ładuje baterii",
        """Podłączony oryginalny zasilacz, dioda na wtyczce się świeci, a bateria stoi na 7 procent i procent nie rośnie. Jak wyjmę wtyczkę, laptop gaśnie od razu. Na spotkaniu poza biurkiem nie da się na nim pracować. Obudowa przy gnieździe jest lekko ciepła. Da się wymienić zasilanie, czy mam oddać cały sprzęt?""",
        "2026-09-07 16:08",
    ),
    z(
        "Niebieski ekran przy włączaniu",
        """Przy starcie Windows dochodzi do logo i wyskakuje niebieski ekran z kodem WHEA_UNCORRECTABLE_ERROR. Po restarcie to samo. Nie zdążę wpisać hasła, więc to raczej nie jest kwestia konta. Laptop służbowy, numer na naklejce inwentarzowej MG-2044. Stoi u mnie na biurku.""",
        "2026-08-03 10:28",
    ),
    z(
        "kilka klawiszy nie dziala",
        """w laptopie nie dzialaja klawisze c, v i spacja dziala co drugi raz. mysz i ekran ok. da sie na tym pisac, ale kopiuje myszka i to szalenstwo. nikt go nie ruszal, po prostu od dzis. moze klawiatura do wymiany. jestem w biurze po lunchu, biurko 118.""",
        "2026-06-25 09:14",
    ),
    z(
        "Laptop sam się wyłącza, obudowa parzy",
        """Przy Teamsie po kilkunastu minutach obudowa przy zawiasach jest tak gorąca, że nie da się trzymać, i komputer gaśnie bez komunikatu. Po ostygnięciu wstaje. Wentylator wyje, jakby o coś ocierał. Nie jest po prostu wolny: on się fizycznie wyłącza. Da się to zgłosić jako sprzęt do wymiany, zanim stracę notatki ze spotkania?""",
        "2026-07-20 15:02",
    ),
    z(
        "Stacja dokująca nie widzi monitorów",
        """Po wpięciu laptopa w stację przy biurku oba monitory zostają czarne, a lampka stacji miga. Laptop bez stacji pokazuje obraz normalnie. Kable nie były ruszane. Wczoraj ta sama stacja działała z tym laptopem. Bez drugiego ekranu nie ogarnę arkusza, który mam rozpisany na dwa okna.""",
        "2026-10-07 08:52",
    ),
    z(
        "mysz usb przestala dzialac",
        """mysz logitech przestala swiecic. wpinam ja u siebie i u Tomka, na obu komputerach nic. klawiatura przy tym samym kablu u mnie dziala, wiec to nie port. da sie wymienic mysz? bez niej excel to katorga, touchpad mam wylaczony i nie chce go wlaczać na stale.""",
        "2026-08-26 11:16",
    ),
    z(
        "Drugi monitor zostaje czarny",
        """Laptop wykrywa drugi monitor w ustawieniach ekranu, mogę nawet przesunąć okno poza pierwszy ekran, ale sam monitor ma czarny obraz i miga kontrolką. Kabel przepiąłem, ten sam objaw. Monitor to Dell przy biurku 118, wczoraj działał. Pierwszy ekran, ten w laptopie, jest w porządku.""",
        "2026-07-09 09:33",
    ),
    z(
        "Słuchawki firmowe nie grają",
        """Pożyczyłam słuchawki od Tomka i w moim laptopie grają. Moje firmowe, te z pałąkiem, nie grają ani u mnie, ani u niego. Głośniki laptopa bez słuchawek działają. Wygląda na tę parę, nie na port. Da się je wymienić przed statusem w czwartek?""",
        "2026-06-04 14:47",
    ),
    z(
        "Excel wywala się na jednym pliku",
        """Plik marża_q3.xlsx otwiera się i po kilku sekundach Excel się zamyka, bez pytania o zapis. Inne skoroszyty, także większe, działają. Plik leży na pulpicie, nie na dysku sieciowym. Kopię ma też koleżanka i u niej ten sam plik też ubija Excela. Wygląda na sam plik albo na dodatek, nie na komputer. Licencja Office nie marudzi.""",
        "2026-10-06 10:21",
    ),
    z(
        "Word otwiera dokumenty jako tylko do odczytu",
        """Od dziś Word każdy dokument z pulpitu otwiera jako tylko do odczytu, także nowe pliki, które przed chwilą sama utworzyłam. Nie leżą na dysku sieciowym. Excel na tym samym komputerze zapisuje normalnie. Nie włączałam żadnej ochrony dokumentu. Potrzebuję poprawić umowę na 15:00.""",
        "2026-08-31 12:06",
    ),
    z(
        "OneDrive pokazuje ciągły konflikt kopii",
        """OneDrive od wczoraj tworzy przy jednym pliku kolejne kopie z dopiskiem konflikt. Synchronizacja kręci się bez końca, a na pasku jest szukanie zmian. Plik to harmonogram, leży w firmowym OneDrive, nie na dysku sieciowym. Inne foldery podobno są zsynchronizowane. Boję się coś skasować, żeby nie nadpisać wersji, którą rano edytowała Olga.""",
        "2026-07-22 08:44",
    ),
    z(
        "Office pisze, że produkt bez licencji",
        """Po zalogowaniu do Worda i Excela jest żółty pasek, że produkt nie ma licencji, i za chwilę przechodzi w tryb tylko do odczytu. Na konto firmowe jestem zalogowana, to samo konto co w Outlooku, a Outlook działa. Wczoraj Office jeszcze pozwalał edytować. Mam dziś poprawki w ofercie, które muszę odesłać przed 14:00.""",
        "2026-06-12 11:08",
    ),
    z(
        "Potrzebuję programu do paczek zip",
        """Cześć, kierownik kazał mi ogarnąć paczkę zip od dostawcy, a na laptopie jest tylko to, co w Windowsie, i wbudowany eksplorator przy haśle na archiwum pokazuje błąd. Proszę o instalację 7-Zip albo czegoś firmowego, co otwiera takie paczki. Zgłoszenie akceptuje kierownik sprzedaży.""",
        "2026-10-02 09:25",
    ),
    z(
        "Aktualizacja Windows stanęła na 48 procent",
        """Rano kliknęłam aktualizuj i uruchom ponownie, bo system nie dawał spokoju. Od dwóch godzin jest napis, że praca z aktualizacjami stoi na 48 procent i żebym nie wyłączała komputera. Laptop jest gorący, ale pasek nie drgnie. Nie wyłączam go z prądu. Mam na nim otwartą prezentację, która chyba już przepadła. Jestem w biurze, biurko przy drukarce kadr.""",
        "2026-08-19 16:27",
    ),
    z(
        "Prośba o instalację czytnika PDF",
        """Na komputerze w magazynie nie otwierają się PDF-y z zamówieniami, przeglądarka je ściąga i tyle. Proszę o doinstalowanie firmowego czytnika PDF. Komputer jest wspólny, login magazyn. Kierownik magazynu akceptuje instalację. Nie instaluję tego sama, tak jak prosiliście przy ostatnim sprzęcie.""",
        "2026-06-23 10:40",
    ),
    z(
        "Prośba o dostęp do folderu projektu Atrium",
        """Dzień dobry, od wczoraj jestem dopisana do projektu Atrium, ale folder Atrium na dysku P otwiera się komunikatem o braku dostępu. Na dysk P wchodzę, widzę inne projekty, tylko ten folder jest niedostępny. Kierowniczka projektu, Ewa Baran, prosiła, żebym napisała zgłoszenie. Loguję się normalnie, hasło działa.""",
        "2026-10-09 09:18",
    ),
    z(
        "Nie mam modułu CRM, choć konto działa",
        """Wchodzę do CRM swoim loginem, pulpit się otwiera, ale nie widzę modułu Oferty, który mają pozostali handlowcy. Przycisku po prostu nie ma, nie ma też błędu. Kierownik sprzedaży potwierdza, że powinienem to mieć od przeniesienia do zespołu w zeszłym tygodniu. Hasło i kod z telefonu przechodzą.""",
        "2026-09-10 14:15",
    ),
    z(
        "Dysk księgowości, odmowa dostępu",
        """Potrzebuję na dziś wglądu do folderu Windykacja na dysku S, bo przejęłam zaległe sprawy. Wchodzę na dysk S, widzę folder, a po dwukliku jest odmowa dostępu. Kierowniczka księgowości, Barbara Kozłowska, mailowo się zgadza, mogę przekazać tę wiadomość. To nie jest awaria dysku, u Barbary folder się otwiera.""",
        "2026-07-30 08:27",
    ),
    z(
        "Dostęp do raportu sprzedaży",
        """Proszę o dostęp do obszaru roboczego Sprzedaż w raporcie, którego używa zespół. Link od kolegi otwiera stronę z informacją, że nie mam uprawnień do wyświetlenia. Konto firmowe to samo, którym loguję się do poczty. Wystarczy odczyt, nic nie publikuję.""",
        "2026-06-03 11:22",
    ),
    z(
        "SAP nie zapisuje faktury, błąd przy księgowaniu",
        """Loguję się do SAP normalnie. Przy księgowaniu faktury, transakcja FB60, dokument dochodzi do symulacji i przy zapisie dostaję krótki błąd, że saldo nie zgadza się z pozycjami, na dokumencie, który w Excelu bilansuje się co do grosza. Ten sam typ faktury wczoraj przeszedł. Wygląda na błąd systemu, nie na brak transakcji, bo FB60 mam i wchodzę w nią bez komunikatu o uprawnieniach.""",
        "2026-10-05 09:55",
    ),
    z(
        "Wniosek urlopowy w kadrach kończy się błędem",
        """W systemie kadr, nie na stronie intranetu, tylko w aplikacji z pulpitu, składam wniosek urlopowy na 27–30 października. Po wysłaniu jest okno: nieoczekiwany błąd serwera aplikacji, kod KH-441. Wniosek nie pojawia się na liście. Kolega z zespołu złożył swój dziś rano i mu przeszło, więc raczej nie leży cały moduł, ale u mnie ten wniosek nie wchodzi za drugim i trzecim razem.""",
        "2026-08-13 12:48",
    ),
    z(
        "CRM nie otwiera karty klienta",
        """Po wyszukaniu klienta Huta Szkła Kolor CRM pokazuje go na liście, a po wejściu w kartę jest pusta strona i kręcące się kółko, które nie znika. Inne karty, na przykład mniejsze firmy, otwierają się. Nie ma napisu o braku uprawnień. Próbowałam w przeglądarce i w aplikacji, to samo. Potrzebuję tej karty na rozmowę jutro o 9:00.""",
        "2026-06-30 15:21",
    ),
    z(
        "nie slychac mnie na teamsach",
        """na spotkaniu z klientem nikt mnie nie slyszy. pisza na czacie ze mam wyciszony mikrofon, a ja nie mam. suwak w teamsach jest na full, w windowsie tez widze ze mikrofon lapie, bo pasek sie rusza przy mowie. sluchawki dzialaja, bo slysze innych. kamera tez jest. tylko moj glos nie dochodzi. spotkanie trwa, jak ktos moze to niech napisze co kliknac.""",
        "2026-10-01 08:40",
    ),
    z(
        "Teams nie uruchamia się",
        """Po kliknięciu ikony Teams okno mignie i znika. Na pasku zadań nie zostaje. Outlook i reszta pakietu działają, jestem zalogowana. Restart komputera nic nie zmienił. Mam za 40 minut status z zarządem i wejdę z telefonu, ale na telefonie nie mam prezentacji. Da się to podnieść?""",
        "2026-08-20 09:07",
    ),
    z(
        "Teams nie pokazuje powiadomień",
        """Teams działa, ale od wczoraj nie przychodzą mi powiadomienia o wiadomościach na kanałach. Widzę je dopiero, jak sama wejdę w kanał. Dzwonek w ustawieniach jest włączony, w Windowsie też. Przez to przegapiłam pytanie klienta. Da się sprawdzić, czemu Teams nie pokazuje powiadomień? Dźwięk na spotkaniach działa.""",
        "2026-07-02 13:11",
    ),
    z(
        "Kliknęłam link i podałam hasło",
        """Dostałam maila jakoby z IT, że konto zostanie zablokowane, jak nie potwierdzę hasła w ciągu 30 minut. Adres był podobny do naszego, ale kończył się na meridian-support.example, nie na meridian.example. Kliknęłam i wpisałam hasło do komputera, zanim dotarło do mnie, że Wy tak nie piszecie. Maila już nie mam, skasowałam w panice. Co mam zrobić najpierw?""",
        "2026-10-19 08:03",
    ),
    z(
        "Znalazłam obcy pendrive w sali",
        """Na stole w sali Kopernik leżał pendrive bez opisu, po spotkaniu z firmą zewnętrzną. Nikt się nie przyznaje. Nie wpinałam go. Leży u mnie w zamkniętej szufladzie biurka 142. Chyba nie powinnam go oddawać na recepcję ani sprawdzać, co jest w środku. Proszę o odbiór.""",
        "2026-09-01 11:36",
    ),
    z(
        "Zostawiłem laptopa w pociągu",
        """Wysiadłem na Centralnej i laptop został na półce. Jest zablokowany hasłem, na dysku mam maile i folder z umowami. Dzwoniłem do kolejarzy, jeszcze go nie mają. Trzeba go chyba zdalnie zablokować, jeśli się da, i unieważnić dostępy. Numer inwentarzowy MG-2218. Jestem pod telefonem.""",
        "2026-07-27 16:46",
    ),
    z(
        "Antywirus złapał załącznik i nie wiem, czy go ruszać",
        """Otwierałam zestawienie od kontrahenta, plik w mailu, i antywirus od razu wrzucił go do kwarantanny z opisem, że zachowanie jest podejrzane. Pliku już nie widzę w pobranych. Nie klikałam przywróć. Nadawca wyglądał znajomo, ale na komunikacie było widać podwójne rozszerzenie. Macie sprawdzić ten komputer?""",
        "2026-06-09 10:18",
    ),
    z(
        "Zniknął folder z dysku projektu",
        """Wczoraj wieczorem na dysku P, w projekcie Atrium, w rysunkach, był folder z września. Dziś rano go nie ma, ani u mnie, ani u osoby obok. Nie wyskakiwał brak dostępu, po prostu nie ma tej pozycji na liście. Szukałem w koszu, pusty. Da się to wziąć z kopii? Bez tych rysunków stoimy z branżą elektryczną.""",
        "2026-09-24 14:55",
    ),
    z(
        "Nie mapuje się dysk S",
        """Po zalogowaniu nie mam dysku S, który wczoraj był. W oknie Ten komputer są tylko dysk C i dysk P. Ręczne połączenie z udziałem księgowości, tym ze skrótu na pulpicie, kończy się błędem, że nie odnaleziono ścieżki sieciowej. VPN jest włączony, na stronę intranetu wchodzę. Wygląda to na sam udział, nie na brak sieci.""",
        "2026-08-06 08:33",
    ),
    z(
        "Przywróćcie proszę wczorajszy plik kosztorysu",
        """Nadpisałam kosztorys na dysku księgowości, plik atrium w wersji 7, złymi stawkami i zapisałam. Poprzednia wersja była z wczoraj, około 16:00, robiła ją Magdalena. Nie mam lokalnej kopii. Czy z backupu da się wyjąć tę wczorajszą wersję obok, nie nadpisując tego, co jest teraz? Przydałyby się obie, żeby porównać.""",
        "2026-06-16 13:27",
    ),
    z(
        "komputer strasznie muli od rana",
        """od wlaczenia wszystko wstaje po kilka minut. pulpit jest, ale klikniecie w menu start to czekanie. wentylator chodzi glosno, ale komputer sie nie wylacza i nie jest goracy jak blacha, po prostu pelza. menedzer zadan pokazuje dysk na 100 procent i jakis proces antymalware. nie instalowalem nic nowego. da sie to przyspieszyc? na spotkaniu za godzine bede musial cos pokazac.""",
        "2026-09-22 08:11",
    ),
    z(
        "Po zalogowaniu da się pracować dopiero po kwadransie",
        """Sam login hasłem przechodzi od razu. Potem z dziesięć minut ikony na pasku dochodzą po jednej i do tego czasu Excel otwiera się biały. Powtarza się codziennie od ponad tygodnia, nie tylko dziś. Laptop ma dwa lata, nie wyłącza się i nie pokazuje niebieskiego ekranu. Na spotkaniach, jak już wszystko wstanie, da się pracować. Wygląda na start systemu, nie na uszkodzenie.""",
        "2026-07-23 11:44",
    ),
    z(
        "Przeglądarka zżera pamięć i zamula resztę",
        """Jak mam otwarte kilkanaście kart w przeglądarce, po godzinie komputer przestaje nadążać z klikaniem. Menedżer zadań pokazuje przeglądarkę powyżej 3 GB. Jak karty pozamykam, da się pracować. Nie jest tak od razu po włączeniu, tylko po dłuższym siedzeniu w intranetie i w CRM w przeglądarce. CRM sam w sobie otwiera się normalnie, to nie wygląda na awarię systemu.""",
        "2026-06-02 15:09",
    ),
    z(
        "Nowy pracownik od środy, prośba o konto i laptop",
        """W środę 14.10 zaczyna u nas Igor Lewicki, specjalista ds. ofert, zespół sprzedaży. Potrzebuje konta, poczty, laptopa i podstawowych dostępów handlowca: CRM, dysk P oraz Teams. Nie zakładałam mu nic sama. Będzie siedział w pokoju 210. Jeśli laptop trzeba przygotować dzień wcześniej, jesteśmy w biurze we wtorek.""",
        "2026-10-12 07:48",
    ),
    z(
        "Praktykantka od września, stanowisko na dwa miesiące",
        """Od 1 września będzie u nas praktykantka, Zuzanna Olczyk, dział marketingu. Umowa na dwa miesiące. Potrzebuje konta, poczty i dostępu do folderu marketingu na dysku P, bez SAP i bez księgowości. Sprzęt może być ten starszy po zwrocie, jeśli macie coś na stanie, nie musi być nowy. Opiekunem jestem ja.""",
        "2026-08-25 09:02",
    ),
    z(
        "Ostatni dzień pracy, wyłączyć dostępy",
        """Dziś ostatni dzień umowy Marka Lisa z działu ofert. To nie jest Tomasz Lis, tylko inna osoba. Proszę o zablokowanie konta po 17:00, przekierowanie poczty m.lis na mnie do końca miesiąca i informację, kiedy odebrać laptopa. Laptop jest u niego, odda go dziś na recepcję. Dostępów do dysków nie zostawiamy.""",
        "2026-09-25 14:36",
    ),
    z(
        "Zwrot sprzętu po zakończonej umowie",
        """W środę skończyła się umowa z grafikiem zewnętrznym. Sprzęt wrócił: laptop MG-1988, zasilacz, mysz i słuchawki, leży w kartonie u mnie w pokoju 206. Konto podobno już zablokowano w zeszłym tygodniu, więc nie proszę o blokadę, tylko o odbiór sprzętu i zdjęcie go z mojego stanu. Formalnie był przypisany do mnie jako do opiekuna.""",
        "2026-06-26 10:55",
    ),
    z(
        "Pęknięta szybka w telefonie służbowym",
        """Telefon służbowy upadł na posadzkę w kuchni i szybka pękła w pajęczynę. Dotyk w górnej części sam klika. Rozmowy działają, karta jest w środku, nie zgubiłam go. Da się wymienić szybę albo dać zastępczy aparat na czas naprawy? Numer zostaje ten sam, klienci go mają. Model mogę podać, jak ktoś przyjdzie, jest na pudełku.""",
        "2026-09-18 12:18",
    ),
    z(
        "Portal pracowniczy zwraca błąd 500",
        """Od 9:00 strona portal.meridian.example nie otwiera strony głównej. Jest biała plansza i błąd 500. Dotyczy też osób obok, sprawdzałem u dwóch. Outlook w tym czasie działa, VPN nie jest potrzebny, jesteśmy w biurze. Chciałem tylko pobrać formularz delegacji, ale nie wstaje nawet menu. Wygląda na awarię portalu, nie na moje konto, bo błąd jest ten sam bez logowania.""",
        "2026-08-10 09:29",
    ),
]
