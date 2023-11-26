import json

from .config import parser
from .client import client_factory


class Core:
    def __init__(self, config_path: str):
        self.client_factory = client_factory.ClientFactory()
        self.config_path = config_path

        configs = parser.Parser(config_path).parse()

        self.configs_by_id = {config.get_id(): config for config in configs.vm_configs}

    def run(self, vm_id: str):
        config = self.configs_by_id.get(vm_id)
        client = self.client_factory.build(config)
        client.run(config)

    def run_all(self):
        for config in self.configs_by_id.values():
            self.run(config.get_id())

    async def quit(self, vm_id: str):
        config = self.configs_by_id.get(vm_id)
        client = self.client_factory.build(config)
        await client.quit(config)

    def quit_all(self):
        for config in self.configs_by_id.values():
            self.quit(config.get_id())
