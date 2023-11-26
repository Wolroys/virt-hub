from . vm_config import AbstractVmConfig


class ParserResult:
    def __init__(self, vm_configs: list[AbstractVmConfig]):
        self.vm_configs = vm_configs

    def get_vm_configs(self):
        return self.vm_configs
