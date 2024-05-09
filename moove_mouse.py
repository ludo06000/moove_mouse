import pyautogui
import random
import time


def move_mouse_randomly(duration :int) -> None :
    try :
        while True :
            x = random.randint(600, 700)
            y = random.randint(200, 600)
            hour = time.localtime()
            pyautogui.moveTo(x, y, 0.5)
            mouse_position = pyautogui.position()
            print(f'La position de la souris est : {mouse_position}')
            print(f'Mouvement à {hour.tm_hour}:{hour.tm_min}:{hour.tm_sec}')
            time.sleep(duration)
    except KeyboardInterrupt:
        print('\n')


if __name__ == "__main__" :
    print('Press Ctrl-C to quit.')
    duration = int(input("Veuillez entréer le temps de pause : (defaut 90)") or 90)

    try:
        move_mouse_randomly(duration=duration)
    except pyautogui.FailSafeException:
        print('Échec de la fonction "FailSafe" de PyAutoGUI. La souris est proche du coin supérieur gauche de l\'écran.')
    except Exception as e:
        print(f'Une erreur s\'est produite : {e}')

