def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x:  "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]

    total_power = sum(map(lambda x: x['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "misc"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"}
    ]
    sorted_arts = artifact_sorter(artifacts)

    art1 = sorted_arts[0]
    art2 = sorted_arts[1]
    print(f"{art1['name']} ({art1['power']} power) comes before "
          f"{art2['name']} ({art2['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)

    print(" ".join(transformed))
