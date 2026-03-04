def spell_combiner(spell1: callable, spell2: callable) -> callable:
def power_amplifier(base_spell: callable, multiplier: int) -> callable:
def conditional_caster(condition: callable, spell: callable) -> callable
def spell_sequence(spells: list[callable]) -> callable