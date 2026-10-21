"""Domyślne kolejki. Do bazy trafiają tylko przy pierwszym uruchomieniu."""

LABELS: list[dict[str, str]] = [
    {
        "code": "haslo",
        "name": "Reset hasła i blokada konta",
        "description": "Hasło wygasło, jest złe albo konto zablokowano. Nie brak roli przy udanym logowaniu i nie kody MFA.",
    },
    {
        "code": "mfa",
        "name": "Uwierzytelnianie wieloskładnikowe",
        "description": "Authenticator, SMS albo push nie działa, choć hasło zostało przyjęte.",
    },
    {
        "code": "uprawnienia",
        "name": "Uprawnienia do systemów i folderów",
        "description": "Logowanie działa, brakuje roli, folderu, modułu albo transakcji. Nie instalacja programu.",
    },
    {
        "code": "onboarding",
        "name": "Nowe stanowisko",
        "description": "Nowa osoba: konto, laptop i zestaw dostępów na start. Nie pojedyncze prawo stałego pracownika.",
    },
    {
        "code": "offboarding",
        "name": "Odejście i zwrot sprzętu",
        "description": "Koniec umowy, blokada konta odchodzącego, odbiór sprzętu. Zgubiony laptop pracującego to bezpieczeństwo.",
    },
    {
        "code": "drukarka",
        "name": "Drukarki i skanery",
        "description": "Offline, zacięcie, puste strony, zła drukarka, skaner. Odmowa dostępu przy działających innych to uprawnienia.",
    },
    {
        "code": "sprzet",
        "name": "Sprzęt komputerowy",
        "description": "Laptop nie wstaje, czarny ekran, bateria, niebieski ekran, przegrzanie z wyłączeniem, klawiatura wbudowana.",
    },
    {
        "code": "peryferia",
        "name": "Monitory, dokowanie i peryferia",
        "description": "Stacja dokująca, monitor, mysz, słuchawki, kamera niesprawna też poza jedną aplikacją.",
    },
    {
        "code": "instalacja",
        "name": "Instalacja i aktualizacje",
        "description": "Prośba o instalację programu albo utknięta aktualizacja Windows, także gdy instalator pyta o hasło administratora.",
    },
    {
        "code": "wydajnosc",
        "name": "Wydajność i zawieszanie",
        "description": "Komputer działa, ale pełza, bez awarii sprzętu i bez podejrzanego pliku.",
    },
    {
        "code": "telefon",
        "name": "Telefon służbowy",
        "description": "Służbowa komórka: szybka, wymiana, konfiguracja. Zgubiony telefon z danymi to bezpieczeństwo.",
    },
    {
        "code": "vpn",
        "name": "VPN i praca zdalna",
        "description": "Tunel VPN nie wstaje, zrywa się albo błąd certyfikatu. Odrzucenie hasła albo brak push to tożsamość.",
    },
    {
        "code": "wifi",
        "name": "Sieć lokalna i Wi-Fi",
        "description": "Wi-Fi lub kabel w biurze, sala, sieć gościnna. Hasło gościa zostaje tutaj.",
    },
    {
        "code": "poczta",
        "name": "Poczta elektroniczna",
        "description": "Outlook: wysyłka, odbiór, pełna skrzynka, limit załącznika. Phishing to bezpieczeństwo.",
    },
    {
        "code": "office",
        "name": "Pakiet biurowy i Microsoft 365",
        "description": "Word, Excel, PowerPoint, OneDrive, licencja. Sam Outlook to poczta, plik tylko na dysku sieciowym to pliki.",
    },
    {
        "code": "erp",
        "name": "Systemy dziedzinowe",
        "description": "SAP, CRM albo kadry: błąd zapisu lub ekranu przy dostępie, który użytkownik już ma.",
    },
    {
        "code": "teams",
        "name": "Microsoft Teams i spotkania",
        "description": "Teams nie wstaje, cisza mimo sprawnego mikrofonu w Windowsie, brak powiadomień.",
    },
    {
        "code": "intranet",
        "name": "Intranet i aplikacje webowe",
        "description": "Portal nie wstaje, błąd 500, formularz w przeglądarce się nie kończy. Odmowa zapisu to uprawnienia.",
    },
    {
        "code": "pliki",
        "name": "Pliki, dyski sieciowe i kopie",
        "description": "Zniknął plik, nie mapuje się dysk, kopia z backupu, uszkodzony plik na udziale.",
    },
    {
        "code": "bezpieczenstwo",
        "name": "Incydent bezpieczeństwa",
        "description": "Phishing, kliknięty link, obce hasło, pendrive, zgubiony laptop, alarm antywirusa, obce maile z czyjejś skrzynki.",
    },
]

BY_CODE = {item["code"]: item for item in LABELS}


def category_name(code: str | None) -> str:
    if not code:
        return ""
    item = BY_CODE.get(code)
    return item["name"] if item else code
