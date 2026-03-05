def spell_combiner(spell1: callable, spell2: callable) -> callable:
	return lambda *args: (spell1(*args), spell2(*args))

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
	return lambda *args: base_spell(*args) * multiplier

def conditional_caster(condition: callable, spell: callable) -> callable:
	return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"

def spell_sequence(spells: list[callable]) -> callable:
	return lambda *args: [s(*args) for s in spells]

def main():
	print("\nTesting spell combiner...")
	def fireball(target): return f"Fireball hits {target}"
	def heal(target): return f"Heals {target}"
    
	combined = spell_combiner(fireball, heal)
	res = combined("Dragon")

	print(f"Combined spell result: {res[0]}, {res[1]}")

	print("\nTesting power amplifier...")
	def basic_damage(target): return 10
    
	amplified = power_amplifier(basic_damage, 3)
	print(f"Original: {basic_damage('Goblin')}, Amplified: {amplified('Goblin')}")

if __name__ == "__main__":
	main()