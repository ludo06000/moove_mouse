# MOOSE MOOVE

Ce script en Python utilise les modules PyAutoGUI, random et time pour simuler des mouvements aléatoires de la souris sur l'écran de l'ordinateur.

## INSTRUCTION

```python
poetry install
```

```python
poetry run python moove_mouse.py
```

## Fonctionnement du code
Le script effectue les actions suivantes :

1. Affiche un message indiquant à l'utilisateur de presser Ctrl-C pour quitter le programme.
2. Génère des coordonnées aléatoires pour déplacer la souris dans une boucle infinie.
3. Utilise PyAutoGUI pour déplacer la souris vers les coordonnées générées avec une durée de déplacement de 0.5 seconde.
4. Fait une pause de 60 secondes entre chaque déplacement de souris.
5. Capture l'exception KeyboardInterrupt lorsque l'utilisateur presse Ctrl-C pour quitter proprement le programme.