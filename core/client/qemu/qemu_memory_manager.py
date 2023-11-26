import subprocess

from ..abstract_memory_manager import AbstractMemoryManager
from ...config.memory_config import ROMDisk
from ...config.vm_config import AbstractVmConfig


class QEMUMemoryManager(AbstractMemoryManager):
    def create_disk(self, disk: ROMDisk, vm_config: AbstractVmConfig | None = None):
        super().create_disk(disk, vm_config)

        print([
            'qemu-img',
            'create',
            '-f {}'.format(disk.type),
            self.get_disk_path(disk, vm_config),
            disk.capacity
        ])

        subprocess.run([
            'qemu-img',
            'create',
            '-f',
            disk.type,
            self.get_disk_path(disk, vm_config),
            disk.capacity
        ])
