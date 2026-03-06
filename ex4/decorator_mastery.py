import time
import functools


def spell_timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Attempt to extract 'power' from kwargs or args
            # Logic: if > 2 args, assume method (self, name, power) -> index 2
            # else assume function (power, ...) -> index 0
            # This logic mimics original code but might be brittle
            power = kwargs.get('power', args[2] if len(args) > 2 else args[0])
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int):
        return f"Successfully cast {spell_name} with power {power}"


if __name__ == "__main__":
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G2"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
