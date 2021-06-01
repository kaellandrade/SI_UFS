-- ALUNO: Micael Andrade Dos Santos 
-- TURMA: BF T01
-- MAT:  201900051051

-- Esquema universidade
SET search_path TO universidade;
-- 1.1
-- Esquema universidade
SELECT mat_professor,
	max(nota) As maior_nota,
	min(nota) As menor_nota,
	avg(nota) as media
FROM leciona le
	JOIN cursa cur ON(le.id_turma = cur.id_turma)
GROUP BY (mat_professor);
-- 1.2
SELECT nome,
	avg(nota)
FROM turma
	JOIN cursa cur USING(id_turma)
	JOIN disciplina di USING(cod_disc)
GROUP BY(nome, pre_req)
HAVING avg(nota) IS NOT NULL;
-- 1.3
SELECT nome,
	pre_req,
	count(turma)
FROM turma
	JOIN disciplina USING(cod_disc)
GROUP BY(cod_disc, pre_req, nome);
-- 1.4
SELECT de.nome,
	avg(nota)
FROM turma
	JOIN cursa USING(id_turma)
	JOIN disciplina di USING(cod_disc)
	JOIN departamento de on(di.depto_responsavel = de.cod_depto)
GROUP BY(de.cod_depto, de.nome);
-- 1.5
SET search_path TO universidade;
SELECT departamento,
	max(salario),
	min(salario)
FROM cargo ca
	JOIN professor pro ON(pro.cargo = ca.id_cargo)
GROUP BY(departamento);
-- 1.6
SELECT mat_professor,
	departamento,
	count(*)
FROM cursa
	JOIN leciona le USING(id_turma)
	JOIN professor pro USING(mat_professor)
GROUP BY(mat_professor, departamento)
HAVING count(*) < 7;
-- 1.7
SELECT primeiro_nome,
	sobrenome,
	avg(nota)
FROM cursa
	JOIN turma USING(id_turma)
	JOIN estudante USING(mat_estudante)
	JOIN usuario USING(cpf)
	JOIN disciplina USING(cod_disc)
GROUP BY(cpf, primeiro_nome, sobrenome, depto_responsavel)
HAVING(depto_responsavel = 'DCOMP');
-- Esquema Hostpital
SET search_path TO hospital;
-- 2.1
SELECT especialidade,
	sum(salario)
FROM medico
GROUP BY(especialidade)
HAVING(sum(salario) > 20000);
-- 2.2
SELECT especialidade,
	sum(salario)
FROM medico
	JOIN medico_docente USING(idregistro)
GROUP BY(especialidade, salario)
HAVING(sum(salario) > 15000);
-- 2.3
SELECT especialidade,
	count(*) as Total
FROM medico
GROUP BY(especialidade);
-- 2.4
SELECT especialidade,
	max(salario) as sal
FROM medico
GROUP BY(especialidade);

-- URI
-- A
SELECT products.id,
	products.name
FROM products
	JOIN categories ON (products.id_categories = categories.id)
WHERE categories.name LIKE 'super%';

-- B 
SELECT li.name,
	round(li.omega * 1.618, 3) AS fator_n
FROM dimensions di
	JOIN life_registry li ON(di.id = li.dimensions_id)
where (li.name LIKE 'Richard%')
	AND (
		di.name = 'C875'
		OR di.name = 'C774'
	);
-- C
SELECT cpf,
	enome,
	dnome
FROM empregados emp
	JOIN departamentos USING(dnumero)
	LEFT JOIN trabalha AS tra ON(emp.cpf = tra.cpf_emp)
	LEFT JOIN projetos USING(pnumero)
where projetos.pnumero IS NULL
ORDER BY cpf ASC;