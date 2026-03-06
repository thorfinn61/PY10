def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def apply(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply


def memory_vault():
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print("\nTesting enchantment factory...")
    enchantment1 = enchantment_factory("Flaming")
    enchantment2 = enchantment_factory("Frozen")
    print(f"{enchantment1('Sword')}")
    print(f"{enchantment2('Shield')}")
    # print("\nTesting spell accumulator...")

    # mana = spell_accumulator(100)
    # print(f"Accumulated 1: {mana(50)}")  # 100 + 50 = 150
    # print(f"Accumulated 2: {mana(20)}")  # 150 + 20 = 170

    # print("\nTesting memory vault...")
    # vault = memory_vault()
    # if vault:
    #     store, recall = vault["store"], vault["recall"]
    #     store("Excalibur", "Legendary Sword")
    #     print(f"Recall Excalibur: {recall('Excalibur')}")
    #     print(f"Recall Unknown: {recall('Mjolnir')}")


if __name__ == "__main__":
    main()
