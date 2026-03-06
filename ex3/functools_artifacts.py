from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any, Dict


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: Dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    op_func: Callable | None = operations.get(operation)
    if op_func is None:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(op_func, spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {element} power {power}!"


def partial_enchanter(base_func: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": partial(base_func, power=50, element="Fire"),
        "ice_enchant": partial(base_func, power=50, element="Ice"),
        "lightning_enchant": partial(
            base_func, power=50, element="Lightning"
        )
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return f"Unknown spell type: {spell}"

    @dispatcher.register(int)
    def _(damage: int) -> str:
        return f"Casting Damage Spell: {damage} HP"

    @dispatcher.register(str)
    def _(enchantment: str) -> str:
        return f"Applying Enchantment: {enchantment}"

    @dispatcher.register(list)
    def _(multi_cast: list) -> str:
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

    # print("\nTesting partial enchanter...")
    # enchanters = partial_enchanter(base_enchantment)

    # print(enchanters["fire_enchant"](target="Sword"))
    # print(enchanters["ice_enchant"](target="Shield"))

    # print("\nTesting spell dispatcher...")
    # dispatch = spell_dispatcher()
    # print(dispatch(100))
    # print(dispatch("Invisibility"))
    # print(dispatch(["Fire", "Ice"]))
    # print(dispatch(45.5))
