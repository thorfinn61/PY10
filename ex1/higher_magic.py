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

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    res = combined("Dragon")

    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("\nTesting power amplifier...")

    def basic_damage(target):
        return 10

    amplified = power_amplifier(basic_damage, 3)
    print(f"Original: {basic_damage('Goblin')}, "
          f"Amplified: {amplified('Goblin')}")

    # print("\nTesting conditional caster...")

    # def is_valid_target(target):
    #     return len(target) > 3

    # cast_on_target = conditional_caster(is_valid_target, fireball)

    # print(f"Cast on 'Orc': {cast_on_target('Orc')}")
    # print(f"Cast on 'Dragon': {cast_on_target('Dragon')}")

    # print("\nTesting spell sequence...")
    # spells = [fireball, heal, lambda t: f"Buffs {t}"]
    # sequence = spell_sequence(spells)

    # results = sequence("Hero")
    # for r in results:
    #     print(f"Sequence step: {r}")


if __name__ == "__main__":
    main()
