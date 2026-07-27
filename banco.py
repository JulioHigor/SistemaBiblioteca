import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL
)
""")

conexao.commit()

def cadastrar_livro(titulo, autor, ano):
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)",
        (titulo, autor, ano)
    )
    conexao.commit()
    
def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    return livros

def buscar_livro(busca):
    cursor.execute(
        """
        SELECT * FROM livros 
        WHERE titulo Like ? 
        """,
        ('%' + busca + '%',)
    )
    
    livros = cursor.fetchall()
    return livros

def remover_livro(id):
    cursor.execute(
        """
        DELETE FROM livros
        WHERE id = ?
        """, 
        (id,)
    )
    conexao.commit()
    
def editar_livro(id, titulo, autor, ano):
    cursor.execute(
        """
        UPDATE livros
        SET titulo = ?, autor = ?, ano = ?
        WHERE id = ?
        """,
        (titulo, autor, ano, id)
    )
    conexao.commit()
        