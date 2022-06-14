from time import sleep
from desmume.emulator import DeSmuME
from desmume.controls import keymask, Keys
from threading import Thread

emu = DeSmuME()
emu.open("C:\\Users\\swank\\PokemonAI\\Black2ROM.nds")
window = emu.create_sdl_window()
emu.volume_set(0)

# Create a function that, when executed, will "spin" and handle our input.
def input_handler():
    # This will infinitely loop on the child thread. You can change this code if you like.
    while True:
        emu.input.keypad_add_key(keymask(Keys.KEY_A))
        sleep(1) 
        emu.input.keypad_rm_key(keymask(Keys.KEY_A))
        emu.input.keypad_add_key(keymask(Keys.KEY_B))
        sleep(1) 
        emu.input.keypad_rm_key(keymask(Keys.KEY_B))
        emu.input.keypad_add_key(keymask(Keys.KEY_UP))
        sleep(1) 
        emu.input.keypad_rm_key(keymask(Keys.KEY_UP))
        emu.input.keypad_add_key(keymask(Keys.KEY_LEFT))
        sleep(1) 
        emu.input.keypad_rm_key(keymask(Keys.KEY_LEFT))
        emu.input.keypad_add_key(keymask(Keys.KEY_DOWN))
        sleep(1) 
        emu.input.keypad_rm_key(keymask(Keys.KEY_DOWN))
        emu.input.keypad_add_key(keymask(Keys.KEY_RIGHT))
        sleep(1) 
        emu.input.keypad_rm_key(keymask(Keys.KEY_RIGHT))

# Spawn a thread that just calls our input handler. This makes the emulator and input sender run concurrently.
Thread(target=input_handler, args=()).start()

while not window.has_quit(): 
    window.process_input()
    emu.cycle()
    window.draw()