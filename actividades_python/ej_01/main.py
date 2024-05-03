from gpiozero import LED, Button
from signal import pause

# Configuración de los pines
led = LED(26)
button = Button(18)

# Cuando el botón se presiona, se enciende el LED
button.when_pressed = led.on
# Cuando el botón se suelta, se apaga el LED
button.when_released = led.off

pause()
