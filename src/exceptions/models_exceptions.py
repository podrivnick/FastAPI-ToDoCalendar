from dataclasses import dataclass

from configs.config_exceptions import MODEL_EXCEPTION, NOT_FOUND_DATA_IN_MODEL_BY_FILTER


@dataclass
class ModelsException(Exception):
    @property
    def message(self):
        return MODEL_EXCEPTION


@dataclass
class NotFoundDataInModelByFilter(ModelsException):
    @property
    def message(self):
        return NOT_FOUND_DATA_IN_MODEL_BY_FILTER

