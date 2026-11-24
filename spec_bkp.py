"""
Script de backup de arquivos e diretórios.

- Cria o diretório de backup caso não exista.
- Atualiza arquivos já existentes.
- Ignora diretórios .git.
- Continua executando mesmo quando algum arquivo falha.
"""

import shutil
from collections.abc import Sequence
from pathlib import Path

IGNORED_DIRS = {".git"}


def should_ignore(path: Path) -> bool:
    """Retorna True se o caminho deve ser ignorado."""
    return any(part in IGNORED_DIRS for part in path.parts)


def copy_file(source: Path, destination: Path) -> None:
    """Copia um único arquivo."""
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"✓ {destination}")
    except PermissionError as exc:
        print(f"✗ Sem permissão: {source}")
        print(f"  {exc}")
    except OSError as exc:
        print(f"✗ Erro ao copiar: {source}")
        print(f"  {exc}")


def backup_directory(source_dir: Path | str, destination_dir: Path | str) -> None:
    """Copia recursivamente um diretório."""
    source_dir = Path(source_dir)
    destination_dir = Path(destination_dir)

    for item in source_dir.rglob("*"):
        if should_ignore(item):
            continue

        relative_path = item.relative_to(source_dir)
        destination = destination_dir / relative_path

        if item.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue

        copy_file(item, destination)


def backup_files(paths: Sequence[str | Path], backup_root: str | Path) -> None:
    """Executa o backup dos caminhos informados."""
    backup_root = Path(backup_root)
    backup_root.mkdir(parents=True, exist_ok=True)

    for path_str in paths:
        source = Path(path_str)

        print(f"\nBackup: {source}")

        if not source.exists():
            print("Caminho não encontrado.")
            continue

        destination = backup_root / source.name

        if source.is_file():
            copy_file(source, destination)

        elif source.is_dir():
            backup_directory(source, destination)

        else:
            print("Tipo de arquivo não suportado.")


if __name__ == "__main__":
    PATHS_TO_BACKUP = [
        r"C:\Users\Admin\.bashrc",
        r"C:\Users\Admin\.gitconfig",
        r"C:\Users\Admin\.gitconfig-personal",
        r"C:\Users\Admin\.gitconfig-work",
        r"C:\Users\Admin\.config",
        r"C:\Users\Admin\.ssh",
        r"C:\Users\Admin\.ssh\config",
        r"C:\Users\Admin\.ssh\allowed_signers",
        r"C:\Users\Admin\OneDrive\Documentos\PowerShell\Microsoft.PowerShell_profile.ps1",
        r"C:\Users\Admin\AppData\Roaming\jj\config.toml",
        r"C:\Users\Admin\.local\share\chezmoi",
        r"C:\Users\Admin\.secrets",
    ]

    BACKUP_DIRECTORY = r"C:\Users\Admin\OneDrive\Documentos\spec_files_bkp"

    backup_files(PATHS_TO_BACKUP, BACKUP_DIRECTORY)
