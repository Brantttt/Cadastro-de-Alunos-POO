import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "alunos.db"

def get_connection():
    """Retorna uma conexão SQLite pronta para uso."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # permite acessar colunas por nome (opcional, mas útil)
    return conn
