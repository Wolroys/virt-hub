import asyncio
import os
import qemu.qmp
import subprocess

from ..abstract_client import AbstractClient
from core.config.vm_config import QEMUVmConfig
from .qemu_memory_manager import QEMUMemoryManager


class QEMUClient(AbstractClient):
    def __init__(self):
        self.memory_manager = QEMUMemoryManager()

    def connect(self, config: QEMUVmConfig):
        return None

    def run(self, config: QEMUVmConfig):
        command = ['qemu-system-x86_64',
                   '-qmp',
                   'unix:{sock_file},server=on,wait=off'.format(
                       sock_file=os.path.join(self.__socket_dir(), config.get_qmp_sock()))]

        if config.memory_config.rom:
            for i, disk in enumerate(config.memory_config.rom.get_disks()):
                if not self.memory_manager.is_disk_exists(disk, config):
                    self.memory_manager.create_disk(disk, config)

                command += ['-drive',
                            'file={},{},{}'.format(self.memory_manager.get_disk_path(disk, config), 'media=disk',
                                                   'index={}'.format(i))]

        print(' '.join(command))

        subprocess.Popen(command)

    async def quit(self, config: QEMUVmConfig):
        socket_path = os.path.join(self.__socket_dir(), config.get_qmp_sock())

        if not os.path.exists(socket_path):
            raise BaseException

        qmp = qemu.qmp.QMPClient(config.name)
        await qmp.connect(socket_path)

        await qmp.execute('quite')

        await qmp.disconnect()

    def __socket_dir(self):
        return '/tmp'
