# Więzień labiryntu – ucieczka z dynamicznie zmieniającego się labiryntu za pomocą sieci neuronowej z wykorzystaniem nauczania przez wzmacnianie



Opis
Aplikacja oparta na algorytmie uczenia przez wzmacnianie, której celem jest nauczenie agenta (sztucznej inteligencji) przechodzenia przez labirynt. Agent używa algorytmu Q-learning do podejmowania decyzji na podstawie nagród i kar, które zdobywa, poruszając się po labiryncie. Aplikacja umożliwia generowanie i wyświetlanie dynamicznie zmieniających się labiryntów w graficznej aplikacji opartej na bibliotece Tkinter. Labirynty są ładowane z plików CSV i prezentowane na planszy. Agent jest trenowany w serii epizodów, a jego działania są monitorowane.

Funkcje
Ładowanie labiryntu z pliku CSV.
Dynamiczna wizualizacja agenta i labiryntu w czasie rzeczywistym.
Algorytm Q-learning dla agenta, który samodzielnie uczy się rozwiązywać labirynt.
Monitorowanie trasy agenta i zapisywanie postępów w postaci tabeli Q.
Zmienność labiryntów w trakcie działania aplikacji (losowe generowanie nowych labiryntów).
Możliwość dostosowywania parametrów uczenia agenta: epsilon, learning rate, discount factor.
Instalacja
Aby uruchomić aplikację na swoim systemie, wykonaj następujące kroki:

Klonowanie repozytorium

Skopiuj repozytorium na swoje lokalne urządzenie:

```bash

git clone https://github.com/TwojeKonto/NazwaRepozytorium.git
```
Instalacja wymaganych bibliotek

Aplikacja wymaga kilku bibliotek Pythona. Aby je zainstalować, uruchom poniższe polecenie w terminalu:

```bash

pip install -r requirements.txt
```
Jeśli plik requirements.txt nie istnieje, zainstaluj ręcznie wymagane biblioteki:

```bash

pip install tkinter csv time random
```
Pliki z labiryntem

Aplikacja ładuje pliki labiryntów w formacie CSV. Upewnij się, że w katalogu głównym projektu znajdują się pliki takie jak Maze1.csv, Maze2.csv, itd., które zawierają dane o strukturze labiryntu (poziomy, ściany, otwarte ściany).

Uruchomienie aplikacji

Aby uruchomić aplikację, uruchom główny plik Pythona:

```bash

python main.py
```
W oknie aplikacji zobaczysz labirynt i agenta poruszającego się po nim. Agenta trenuje Q-learning, a po osiągnięciu celu otrzymuje nagrodę.

Testowanie
Testowanie agenta

Po uruchomieniu aplikacji agent będzie próbował przejść przez labirynt, ucząc się na podstawie nagród i kar za wykonane ruchy. Aby sprawdzić skuteczność agenta, można monitorować wynik w postaci sumy nagród za każdy epizod.

Zmiana labiryntu

Labirynty zmieniają się automatycznie w trakcie działania aplikacji. Po wykonaniu kilku epizodów agent będzie testował kolejne labirynty, które są ładowane losowo z plików CSV.

Monitorowanie postępu

W trakcie działania aplikacji monitorowane są takie parametry jak czas, etap, liczba wykonanych ruchów oraz suma nagród w każdym epizodzie. Możesz je śledzić na ekranie.

Zmiana parametrów agenta

Możesz dostosować parametry agenta (epsilon, learning rate, discount factor) w kodzie, aby sprawdzić ich wpływ na uczenie się i wyniki agenta w różnych epizodach.
