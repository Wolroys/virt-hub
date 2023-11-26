from ..config.vm_config import AbstractVmConfig


class AbstractClient:
    async def connect(self, config: AbstractVmConfig):
        raise NotImplementedError

    async def create(self, config: AbstractVmConfig):
        raise NotImplementedError

    def pause(self):
        raise NotImplementedError

    def resume(self):
        raise NotImplementedError

    def run(self, config: AbstractVmConfig):
        raise NotImplementedError

    async def quit(self, config: AbstractVmConfig):
        raise NotImplementedError
