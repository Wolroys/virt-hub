from os import listdir
from os.path import abspath, isfile, join
import json
from typing import Type

from .parser_result import ParserResult
from .vm_config import *


class Parser:
    def __init__(self, config_path: str):
        self.config_path = config_path

    def parse(self) -> ParserResult:
        return ParserResult(self.__parse_vm_configs())

    def __parse_vm_configs(self) -> list[AbstractVmConfig]:
        vm_config_files: list[dict] = []
        abs_path = abspath(join(self.config_path, self.__get_config_dir_name(),
                             self.__get_vm_config_dir_name()))

        for file_name in listdir(abs_path):
            file_path = join(abs_path, file_name)

            if isfile(file_path):
                file = open(file_path)

                vm_config_files.append(json.loads(file.read()))

        return [self.__resolve_config_class(config.get('type'))(config) for config in vm_config_files]

    def __get_config_dir_name(self) -> str:
        return 'config'

    def __get_vm_config_dir_name(self) -> str:
        return 'vm'

    def __resolve_config_class(self, vm_type: str) -> Type[AbstractVmConfig | QEMUVmConfig]:
        if vm_type == QEMUVmConfig.vm_type:
            return QEMUVmConfig
