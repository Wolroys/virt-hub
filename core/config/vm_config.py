from .memory_config import MemoryConfig


class AbstractVmConfig:
    def __init__(self, vm_id: str, vm_name: str):
        self.id = vm_id
        self.name = vm_name

    def get_id(self) -> str:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_vm_type(self) -> str:
        raise NotImplementedError

    def get_get_memory_config(self) -> MemoryConfig:
        raise NotImplementedError


class QEMUVmConfig(AbstractVmConfig):
    vm_type = 'VM_TYPE_QEMU'

    def __init__(self, data: dict):
        super().__init__(data.get('id'), data.get('name'))
        self.memory_config = MemoryConfig(data.get('memory') or None)

    def get_vm_type(self) -> str:
        return QEMUVmConfig.vm_type

    def get_qmp_sock(self) -> str:
        return self.get_id() + '.sock'

    def get_memory_config(self) -> MemoryConfig:
        return self.memory_config
