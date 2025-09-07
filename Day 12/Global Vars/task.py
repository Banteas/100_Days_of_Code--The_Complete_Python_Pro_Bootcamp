# Modifying Global Scope

enemies = 1


def increase_enemies(enemy,adding_num):
    print(f"enemies inside function: {enemies}")
    return enemy + adding_num


enemies = increase_enemies(enemies,15)
print(f"enemies outside function: {enemies}")


