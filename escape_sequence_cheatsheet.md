# cheatsheet escape sequence

## Color
|:----------|:----------------------------------------------------------|
| param     | result                                                    |
| 0         | reset all attributes to their defaults                    |
| 1         | set bold |
| 2         | set half-bright (simulated with color on a color display) |
| 4         | set underscore (simulated with color on a color display) (the colors used to simulate dim or underline are set using ESC ] ...) |
| 5         | set blink                                                 |
| 7         | set reverse video                                         |
| 10        | reset selected mapping, display control flag, and
         toggle meta flag (ECMA-48 says "primary font"). |
| 11        | select null mapping, set display control flag, reset
         toggle meta flag (ECMA-48 says "first alternate font"). |
| 12        | select null mapping, set display control flag, set
         toggle meta flag (ECMA-48 says "second alternate
         font").  The toggle meta flag causes the high bit of a
         byte to be toggled before the mapping table translation
         is done. |
| 21        | set underline; before Linux 4.17, this value set normal
         intensity (as is done in many other terminals) |
| 22        | set normal intensity                                      |
| 24        | underline off                                             |
| 25        | blink off                                                 |
| 27        | reverse video off                                         |
| 30        | set black foreground                                      |
| 31        | set red foreground                                        |
| 32        | set green foreground                                      |
| 33        | set brown foreground                                      |
| 34        | set blue foreground                                       |
| 35        | set magenta foreground                                    |
| 36        | set cyan foreground                                       |
| 37        | set white foreground                                      |
| 38        | 256/24-bit foreground color follows, shoehorned into 16
              basic colors (before Linux 3.16: set underscore on, set
              default foreground color)                                 |
| 39        | set default foreground color (before Linux 3.16: set underscore off, set default foreground color) |
| 40        | set black background                                      |
| 41        | set red background                                        |
| 42        | set green background                                      |
| 43        | set brown background                                      |
| 44        | set blue background                                       |
| 45        | set magenta background                                    |
| 46        | set cyan background                                       |
| 47        | set white background                                      |
| 48        | 256/24-bit background color follows, shoehorned into 8 basic colors |
| 49        | set default background color                              |
| 90..97    | set foreground to bright versions of 30..37               |
| 100.107   | set background, same as 40..47 (bright not supported)     |

Commands 38 and 48 require further arguments:

| ;5;x      | 256 color: values 0..15 are IBGR (black, red, green, ..., white), 16..231 a 6x6x6 color cube, 232..255 a grayscale ramp |
| ;2;r;g;b  | 24-bit color, r/g/b components are in the range 0..255    |

## Cursor

- Positionnez le curseur:
    ```\033[L;CH```
    Ou
    ```\033[L;Cf```
    place le curseur sur la ligne L et la colonne C.

- Déplacez le curseur vers le haut de N lignes:
    ```\033[NA```

- Déplacez le curseur vers le bas de N lignes:
    ```\033[NB```

- Déplacez le curseur vers l'avant de N colonnes:
    ```\033[NC```

- Déplacer le curseur vers l'arrière de N colonnes:
    ```\033[ND```

- Videz l'écran:
    `\033[1J` : Effacer du début de l'écran au curseur.
    `\033[2J` : Effacer tout l'écran.
    `\033[3J` : Effacer tout l'écran ainsi que le buffer de l'historique (depuis Linux 3.0).

- Effacer la ligne:
    `\033[K`  : Effacer la fin de la ligne
    `\033[1K` : Effacer le début de la ligne
    `\033[2K` : Effacer toute la ligne
    Utile après un retour chariot `\r` si le nouveau message est plus court que l'ancien.

- Enregistrer la position du curseur:
    ```\033[s```

- Restaurer la position du curseur:
    ```\033[u```

Les deux derniers peuvent ne pas fonctionner dans l'émulateur de terminal. Apparemment, seulement **xterm** et **nxterm** utilise ces deux séquences.