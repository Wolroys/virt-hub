import asyncio
from time import sleep
from os import getcwd
from core.core import Core


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    core = Core(getcwd())

    core.run_all()

    sleep(10)

    asyncio.run(core.quit_all())
