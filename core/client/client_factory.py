from ..config.vm_config import *
from .abstract_client import AbstractClient
from .qemu.qemu_client import QEMUClient


class ClientFactory:
    def build(self, vm_sign: AbstractVmConfig | str) -> AbstractClient:
        if vm_sign == QEMUVmConfig.vm_type or isinstance(vm_sign, QEMUVmConfig):
            return QEMUClient()
