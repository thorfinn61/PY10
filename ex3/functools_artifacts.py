from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    op_func = operations.get(operation)
    return reduce(op_func, spells)


def base_enchantment(power, element, target):
    return f"Enchanting {target} with {element} power {power}!"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="Fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="Ice"),
        "lightning_enchant": partial(
            base_enchantment, power=50, element="Lightning"
        )
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher():
    @singledispatch
    def dispatcher(spell):
        return f"Unknown spell type: {spell}"

    @dispatcher.register(int)
    def _(damage):
        return f"Casting Damage Spell: {damage} HP"

    @dispatcher.register(str)
    def _(enchantment):
        return f"Applying Enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_cast):
        return f"Multi-casting {len(multi_cast)} spells: {multi_cast}"

    return dispatcher


if __name__ == "__main__":
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
