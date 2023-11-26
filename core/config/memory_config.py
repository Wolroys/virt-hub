from typing import Any


class MemoryConfig:
    def __init__(self, data: dict | None):
        self.rom = ROMMemoryConfig(data.get('rom')) if data and data.get('rom') else None


class ROMMemoryConfig:
    def __init__(self, disks: list[dict]):
        self.__disks_by_name: dict[str, ROMDisk] = {disk_config.get('name'): ROMDisk(disk_config) for disk_config in disks}

    def get_disks(self):
        return self.__disks_by_name.values()


class ROMDisk:
    DISK_TYPE_QCOW2 = 'qcow2'
    DISK_TYPE_RAW = 'raw'
    
    def __init__(self, disk_config: dict):
        self.name = disk_config.get('name')
        self.capacity = disk_config.get('capacity')
        self.type = disk_config.get('type') or ROMDisk.DISK_TYPE_QCOW2
        self.custom_path: str | None = disk_config.get('custom_path') or None

    def has_custom_path(self) -> bool:
        return bool(self.custom_path)

    def get_custom_path(self) -> str | None:
        return self.custom_path
