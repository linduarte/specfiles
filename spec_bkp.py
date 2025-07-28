"""
Este script realiza backups de arquivos e diretórios especificados
para um diretório de backup definido.

Uso:
1. Defina os caminhos a serem salvos em PATHS_TO_BACKUP.
2. Especifique o diretório de destino em BACKUP_DIRECTORY.
3. Execute o script.

O script cria o diretório de backup se ele não existir e copia os arquivos/diretórios,
atualizando arquivos já existentes no backup.
"""

import shutil
from pathlib import Path

def backup_files(paths, backup_dir):
    """
    Faz backup dos arquivos/diretórios especificados para o diretório de backup.

    Args:
        paths (list): Lista de caminhos a serem salvos.
        backup_dir (str): Diretório de destino do backup.
    """
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(parents=True, exist_ok=True)

    for path in paths:
        path = Path(path)
        print(f"Fazendo backup de: {path}")
        if not path.exists():
            print(f"Caminho {path} não existe, pulando.")
            continue

        base_name = path.name
        destination_path = backup_dir / base_name

        if path.is_file():
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, destination_path)
            print(f"Arquivo salvo/atualizado: {destination_path}")
        elif path.is_dir():
            for item in path.rglob('*'):
                rel_path = item.relative_to(path)
                dest_item = destination_path / rel_path
                if item.is_dir():
                    dest_item.mkdir(parents=True, exist_ok=True)
                else:
                    dest_item.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest_item)
                    print(f"Arquivo salvo/atualizado: {dest_item}")
        else:
            print(f"{path} não é arquivo nem diretório, pulando.")

if __name__ == "__main__":
    # Caminhos a serem salvos
    PATHS_TO_BACKUP = [
        r"C:\Program Files (x86)\gnupg",
        r"C:\Users\admin\.sops",
        r"C:\Users\admin\.bashrc",
        r"C:\Users\admin\.gitconfig",
        r"C:\Users\admin\.gitconfig-pers",
        r"C:\Users\admin\.gitconfig-work",
        r"C:\Users\admin\.config"
    ]

    # ...existing code...
    # Diretório de destino do backup
    BACKUP_DIRECTORY = r"C:\Users\Admin\OneDrive\Documentos\spec_files_bkp"
    
    # Chamada da função para executar o backup
    backup_files(PATHS_TO_BACKUP, BACKUP_DIRECTORY)
