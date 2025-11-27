
# **ZADANIE: Rozszerzenie workflowu Weekly Scraper o nowe miasta**

## **Cel zadania**

Celem zadania jest: 

1. zrozumienie mechanizmu **matrix strategy** w GitHub Actions, dostępnego z https://github.com/marcin119a/ci_cd_demo/blob/main/.github/workflows/scraper.yml
2. rozszerzenie istniejącego pipeline’u **Weekly Scraper**,
3. dodanie nowych miast do procesu scrapowania danych,
4. uruchomienie workflowu i weryfikacja automatycznego zapisu wyników.

Zadanie symuluje pracę z prawdziwym **Data Engineering Pipelin’em**.

---

# **Punkt wyjścia – dany workflow**

Dysponujesz takim workflowem:

```yaml
name: Weekly Scraper

on:
  workflow_dispatch:

jobs:
  run-scraper:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        include:
          - city: lodz
            pages: 8
          - city: krakow
            pages: 10
```

Workflow:

* uruchamia scraper dla miast z matrix strategy,
* generuje pliki CSV,
* zapisuje je jako artifacts,
* a następnie w jobie `commit-changes` commit’uje nowe dane do repozytorium.

---

# **Twoje zadanie**

## **1. Dodaj trzy nowe miasta do workflowu**

Rozszerz sekcję:

```yaml
matrix:
  include:
    - city: lodz
      pages: 8
    - city: krakow
      pages: 10
```

O **następujące miasta:**

* `wroclaw`
* `gdansk`
* `sopot`

Każde miasto musi mieć określoną liczbę stron do scrapowania:

Przykład:

```yaml
- city: wroclaw
  pages: 12

- city: gdansk
  pages: 10

- city: sopot
  pages: 6
```

Oczekiwany efekt:
Workflow uruchomi scraper **pięć razy** — po jednym dla każdego miasta.

---

## **2. Upewnij się, że scraper obsługuje nowe miasta**

Po wykonaniu zadania workflow powinien wygenerować następujące pliki:

```
data/ogloszenia_lodz.csv
data/ogloszenia_krakow.csv
data/ogloszenia_wroclaw.csv
data/ogloszenia_gdansk.csv
data/ogloszenia_sopot.csv
```

---

## **3. Uruchom workflow ręcznie**

Wejdź w:

**GitHub → Actions → Weekly Scraper → Run workflow**

Oczekiwane zachowania:

* powstanie 5 jobów równoległych (matrix strategy),
* każdy job wygeneruje artefakt `data-miasto`,
* job `commit-changes` pobierze pliki i wrzuci je do repo.

---

## **4. Zweryfikuj wynik w repozytorium**

Po zakończeniu działania workflowu:

* powinny pojawić się nowe pliki CSV w katalogu `data/`
* powinien zostać wykonany commit typu:

```
Update scraped data for all cities [YYYY-MM-DD HH:MM:SS]
```

#  BONUS (opcjonalne punkty)

1. Dodaj **walidację**, np. sprawdzenie liczby wierszy w CSV.
2. Scal wszystkie pliki w jeden `all_offers.csv`.
3. Zapisuj dane również w osobnym branchu `data-history`.

---

Jeśli chcesz — mogę na tej bazie przygotować:

* **slajdy do prezentacji**,
* **diagram architektury tego pipeline’u**,
* **wersję tego zadania „dla początkujących” lub „dla zaawansowanych”**.
