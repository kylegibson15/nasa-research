from abc import ABC
from typing import Generic, TypeVar

TResponse = TypeVar('TResponse')
TEntity = TypeVar('TEntity')
TModel = TypeVar('TModel')

class Mapper(ABC, Generic[TResponse, TEntity, TModel]):
    @staticmethod
    def response_to_entity(response: TResponse) -> TEntity:
        raise NotImplementedError("Subclasses must implement this method")
    
    @staticmethod
    def entity_to_model(entity: TEntity) -> TModel:
        raise NotImplementedError("Subclasses must implement this method")
    
    @staticmethod
    def model_to_entity(model: TModel) -> TEntity:
        raise NotImplementedError("Subclasses must implement this method")
    