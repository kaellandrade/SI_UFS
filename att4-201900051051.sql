-- ALUNO: Micael Andrade Dos Santos 
-- TURMA: BF T01
-- MAT:  201900051051

-- Esquema universidade
-- 1.1 OK!
SELECT cpf
FROM universidade.professor
WHERE departamento = 'DMA';

-- 1.2 OK!
SELECT id_turma
FROM universidade.cursa
WHERE mat_estudante = 'E101';

-- 1.3 OK!
SELECT primeiro_nome, sobrenome, cpf 
FROM universidade.usuario
WHERE telefone IS NOT NULL;

-- 1.4 OK!
SELECT nome, cod_disc
FROM universidade.disciplina
WHERE pre_req IS NOT NULL AND creditos > 2;

-- 1.5 ERRADO!
SELECT AVG(mc)
FROM universidade.estudante;

-- 1.6 ERRADO! DEVERIA USAR DISTINCT
SELECT COUNT(mat_professor) AS total_orientacoes
FROM universidade.plano;


-- 1.7 ERRADO! NÃO DEVERIA USAR ALL(POIS DUPLICA)
SELECT mat_professor FROM universidade.plano
UNION ALL
SELECT chefe FROM universidade.departamento
WHERE chefe IS NOT NULL;


-- 1.8 OK!
SELECT mat_professor FROM universidade.plano
INTERSECT
SELECT chefe FROM universidade.departamento


-- 1.9 OK!
SELECT mat_professor FROM universidade.plano
EXCEPT
SELECT chefe FROM universidade.departamento;


-- Esquema hospital

-- 2.1 OK!
SELECT *
FROM hospital.usuario;

-- 2.2 OK!
SELECT primeironome,
    sobrenome
FROM hospital.usuario;

-- 2.3 OK!
SELECT *
FROM hospital.usuario
WHERE sexo = 'M';

-- 2.4 OK!
SELECT *
FROM hospital.perfil
WHERE ativo = 'S';

-- 2.5 OK!
SELECT DISTINCT cidade
FROM hospital.endereco;

-- 2.6 OK!
SELECT DISTINCT bairro
FROM hospital.endereco
WHERE cidade = 'Aracaju';

-- 2.7 OK!
SELECT primeironome,
    sobrenome
FROM hospital.usuario
ORDER BY primeironome,
    sobrenome ASC;

-- 2.8 OK!
SELECT DISTINCT sobrenome
FROM hospital.usuario
WHERE sexo = 'F'
ORDER BY sobrenome ASC;

-- 2.9  OK!
SELECT MAX(salario) AS maior_sal,
    MIN(salario) AS menor_sal
FROM hospital.medico;

-- 2.10 OK!
SELECT MAX(salario) AS maior_sal_clinico_geral
FROM hospital.medico
WHERE especialidade = 'Clínico Geral';

-- 2.11 OK!
SELECT AVG(salario) AS media_sal_cirurgiao
FROM hospital.medico
WHERE especialidade = 'Cirurgião';

-- 2.12 OK!
SELECT COUNT(sexo) AS qtd_pessoas_masc
FROM hospital.usuario
WHERE sexo = 'M';

-- 2.13 OK!
SELECT *
FROM hospital.usuario
WHERE sexo = 'M' AND extract(year FROM datanasc) >= 1980;

-- URI JUDGE
SELECT name 
FROM customers 
WHERE state='RS';

SELECT name, street 
FROM customers
WHERE city='Porto Alegre';

SELECT id, name 
FROM products
WHERE price < 10 OR price > 100;

SELECT DISTINCT city 
FROM providers;

SELECT max(price), min(price)
FROM products;

SELECT DISTINCT city
FROM customers;

SELECT id, password, MD5(password)
FROM account;