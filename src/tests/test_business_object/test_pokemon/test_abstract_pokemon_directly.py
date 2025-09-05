from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic

class MockAbstractPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        return 0

class TestAbstractPokemonDirectly:
    def test_level_up_increases_level_by_1_on_all_pokemon(self):
        squirtle = MockAbstractPokemon(level=5)

        squirtle.level_up()

        assert squirtle.level == 6