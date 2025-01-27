from pathlib import Path
import shutil
import sys
from typing import Tuple

def parse_arguments() -> Tuple[Path, Path]:
    """
    Парсить аргументи командного рядка. Якщо аргументи не передані, запитує через input.

    Returns:
        Tuple[Path, Path]: Вихідна директорія та директорія призначення.
    """
    if len(sys.argv) > 1:
        source_dir = Path(sys.argv[1])
        destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")
    else:
        # Якщо аргументи не передані, запитуємо у користувача
        source_dir = Path(input("Введіть шлях до вихідної директорії: ").strip())
        destination_dir_input = input("Введіть шлях до директорії призначення (натисніть Enter для використання 'dist'): ").strip()
        destination_dir = Path(destination_dir_input) if destination_dir_input else Path("dist")
    return source_dir, destination_dir

def copy_and_sort_files(src: Path, dest: Path) -> None:
    """
    Рекурсивно копіює файли з вихідної директорії до директорії призначення,
    сортує файли за розширеннями в піддиректорії.

    Args:
        src (Path): Вихідна директорія.
        dest (Path): Директорія призначення.
    """
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest)
            elif item.is_file():
                extension = item.suffix[1:].lower()  # Наприклад, "txt", "jpg"
                target_dir = dest / extension

                target_dir.mkdir(parents=True, exist_ok=True)

                try:
                    shutil.copy2(item, target_dir)
                    print(f"Копіюємо: {item} -> {target_dir}")
                except Exception as e:
                    print(f"Помилка копіювання {item}: {e}")
    except Exception as e:
        print(f"Помилка доступу до {src}: {e}")

def main():
    """
    Головна функція програми. Виконує парсинг аргументів або запитує шляхи директорій,
    перевіряє директорії та викликає функцію для копіювання файлів.
    """
    source_dir, destination_dir = parse_arguments()

    if not source_dir.exists():
        print(f"Вихідна директорія '{source_dir}' не знайдена.")
        sys.exit(1)

    destination_dir.mkdir(parents=True, exist_ok=True)

    copy_and_sort_files(source_dir, destination_dir)
    print("Копіювання завершено.")

if __name__ == "__main__":
    main()