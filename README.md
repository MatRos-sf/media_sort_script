# media_sort_script
## Information 
[PL]
Stworzyłem prosty skrypt, który ułatwia mi organizację z mediami (aktualnie z plikami .mp4 i .jpg) na swoim komputerze. 

## Steps
Działanie:
* W pliku głównym znajdują się twie zmienne z ścieżkami DIR_MAIN oraz DIR_MEDIA: DIR_MAIN - ścieżka gdzie ma być tworzony nowy folder , DIR_MEDIA - ścieżka gdzie znajdują się media 
* Po uruchomieniu skryptu program pyta o nową nazwę katalogu podajemy np. zakopane_2022. Dzięki temu wszystkie pliki które są w DIR_MEDIA zostaną zmienione na np. zakopane_2022_1.jpg (nazwaKatalogu_rok_numer.rozszerzenie [ jeżeli rok został nie podany zostanie podany domyślny aktualny] )
* Następnie skrypt tworzy katalog o podanej nazwie w którym znajdują się dwa foldery video i photo oraz przerzuca wszystkie media z DIR_MEDIA do owego katalogu rozdzielając pliki na filmy i zdjęcia 
