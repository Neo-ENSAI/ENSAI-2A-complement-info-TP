from abc import ABC, abstractmethod

from .pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(ABC):
    """
    """

    def _init_(self, power : int, name : str, description):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(
        self, attacking_pokemon: AbstractPokemon, defending_pokemon : AbstractPokemon
    ) -> int:
        pass

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
