import os

from core.config.memory_config import ROMDisk
from core.config.vm_config import AbstractVmConfig


class AbstractMemoryManager:
    def is_disk_exists(self, disk: ROMDisk, vm_config: AbstractVmConfig | None = None) -> bool:
        return os.path.exists(self.get_disk_path(disk, vm_config))

    def create_disk(self, disk: ROMDisk, vm_config: AbstractVmConfig | None = None):
        if not self.is_disk_exists(disk, vm_config):
            print(os.path.dirname(self.get_disk_path(disk, vm_config)))
            os.makedirs(os.path.dirname(self.get_disk_path(disk, vm_config)))

    def get_disk_path(self, disk: ROMDisk, vm_config: AbstractVmConfig | None = None) -> str:
        if not vm_config and not disk.has_custom_path():
            raise BaseException

        if disk.has_custom_path():
            return disk.custom_path

        return os.path.join(os.path.expanduser('~/.virthub'), vm_config.get_id(), 'disks',
                            '{}.{}'.format(disk.name, disk.type))

    def __get_disks_dir(self) -> str:
        return os.path.expanduser('~/.virthub')
