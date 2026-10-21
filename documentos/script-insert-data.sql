INSERT INTO usuarios (nome, email, senha)
VALUES
('Ana Silva', 'ana@gmail.com', '123456'),
('Joao Santos', 'joao@gmail.com', '789101'),
('Maria Oliveira', 'maria@gmail.com', '213141'),
('Pedro Souza', 'pedro@gmail.com', '516171'),
('Lucas Costa', 'lucas@gmail.com', '819202');
INSERT INTO filmes
(usuario_id, titulo, ano_lancamento, genero, nota, capa_url)
VALUES
(1, 'O Poderoso Chefinho', '2017-03-31', 'Animacao', 7.0, 'O Poderoso Chefinho.pdf'),
(1, 'A Bela e a Fera', '1991-11-22', 'Fantasia', 8.0, 'A Bela e a Fera.pdf'),

(2, 'Matilda', '1996-08-02', 'Comedia', 7.0, 'Matilda.pdf'),
(2, 'Avatar (2009)', '2009-12-18', 'Ficcao Cientifica', 7.8, 'Avatar (2009).pdf'),

(3, 'Interestelar', '2014-11-06', 'Ficcao Cientifica', 9.0, 'Interestelar.pdf'),
(3, 'Titanic', '1997-12-19', 'Romance', 8.0, 'Titanic.pdf'),

(4, 'Corra!', '2017-05-18', 'Terror', 8.2, 'Corra!.pdf'),
(4, 'Shrek', '2001-05-18', 'Animacao', 8.0, 'Shrek.pdf'),

(5, 'Vingadores: Ultimato', '2019-04-25', 'Acao', 8.4, 'Vingadores Ultimato.pdf'),
(5, 'Toy Story', '1995-12-22', 'Animacao', 8.5, 'Toy Story.pdf');
