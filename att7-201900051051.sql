-- ALUNO: Micael Andrade Dos Santos 
-- TURMA: BF T01
-- MAT:  201900051051
-- Esquema universidade
SET search_path TO universidade;
-- 1.1
WITH estudantes_p200 AS (
	SELECT *
	FROM estudante
		JOIN plano pla USING(mat_estudante)
	WHERE mat_professor = 'P200'
)
SELECT estudantes_p200.mat_estudante
FROM estudantes_p200
	JOIN cursa cur ON(
		estudantes_p200.mat_estudante = cur.mat_estudante
	)
	JOIN leciona le USING(id_turma)
WHERE le.mat_professor = 'P500';
-- 1.2
SELECT mat_professor
FROM professor
WHERE mat_professor NOT IN (
		SELECT mat_professor
		FROM plano
	)
	OR mat_professor IN (
		SELECT chefe AS mat_professor
		FROM departamento
	);
-- 1.3
SELECT mat_professor
FROM professor
WHERE mat_professor IN (
		SELECT mat_professor
		FROM plano
	)
	AND mat_professor IN (
		SELECT chefe AS mat_professor
		FROM departamento
	);
-- 1.4
WITH nao_orientam AS (
	SELECT mat_professor
	FROM professor
	WHERE mat_professor NOT IN (
			SELECT mat_professor
			FROM plano
		)
)
SELECT mat_professor
FROM nao_orientam
	LEFT JOIN departamento ON(nao_orientam.mat_professor = chefe)
WHERE chefe is NULL;
-- 1.5
WITH media_todos_dept AS (
	SELECT p.departamento AS depto,
		avg(salario) AS media_salario
	FROM professor p
		JOIN cargo c ON(p.cargo = c.id_cargo)
	GROUP BY p.departamento
)
SELECT min(media_salario) AS menor_media_de_todos_dpt
FROM media_todos_dept;
-- 1.6
SELECT mat_professor,
	prof_media,
	departamento_media
FROM (
		SELECT mat_professor,
			depto_responsavel,
			avg(nota) AS prof_media
		FROM cursa
			JOIN turma USING(id_turma)
			JOIN leciona USING(id_turma)
			JOIN disciplina USING(cod_disc)
		GROUP BY(mat_professor, depto_responsavel)
	) as media_prof
	JOIN (
		SELECT depto_responsavel,
			avg(nota) AS departamento_media
		FROM cursa
			JOIN turma USING(id_turma)
			JOIN disciplina USING(cod_disc)
		GROUP BY depto_responsavel
	) AS media_dep USING(depto_responsavel);
--1.7
SELECT ur.primeiro_nome,
	ur.sobrenome
FROM professor pro2
	JOIN cargo car2 ON (car2.id_cargo = pro2.cargo)
	JOIN usuario ur USING(cpf)
WHERE car2.salario = (
		SELECT min(salario)
		FROM professor pro
			JOIN cargo car ON(car.id_cargo = pro.cargo)
	);
-- 1.8
SELECT primeiro_nome,
	sobrenome
FROM (
		SELECT *
		FROM cursa
		WHERE nota IN (
				SELECT min(nota)
				FROM cursa
			)
	) as al_menor
	JOIN estudante USING(mat_estudante)
	JOIN usuario USING(cpf);
-- 1.9
SELECT primeiro_nome,
	sobrenome,
	maior_5,
	menor_5
FROM (
		SELECT mat_estudante,
			count(cod_disc) as maior_5
		FROM (
				SELECT *
				FROM cursa
				WHERE nota >= 5
			) AS maior_5
			JOIN turma USING(id_turma)
		GROUP BY (mat_estudante)
	) as notas_maiores_5
	JOIN (
		SELECT mat_estudante,
			count(cod_disc) AS menor_5
		FROM (
				SELECT *
				FROM cursa
				WHERE nota < 5
			) AS maior_5
			JOIN turma USING(id_turma)
		GROUP BY (mat_estudante)
	) AS notas_menores_5 USING(mat_estudante)
	JOIN estudante USING(mat_estudante)
	JOIN usuario USING(cpf);
-- 1.10
SELECT *
FROM (
		(
			SELECT cod_disc,
				depto_responsavel,
				avg(nota) AS media_disc
			FROM cursa
				JOIN turma USING(id_turma)
				JOIN disciplina USING(cod_disc)
			GROUP BY(cod_disc, cod_disc, depto_responsavel)
		) AS notas_dis
		JOIN (
			SELECT depto_responsavel,
				avg(nota) AS media_depto
			FROM cursa
				JOIN turma USING(id_turma)
				JOIN disciplina USING(cod_disc)
			GROUP BY(depto_responsavel)
		) AS notas_depto USING(depto_responsavel)
	) AS media_final
WHERE (media_disc < media_depto);
-- Esquema hospital
SET search_path TO hospital;
-- 2.1
SELECT numcrm,
	primeironome,
	especialidade,
	salario
FROM medico
	JOIN usuario USING(cpf)
WHERE medico.salario >= SOME (
		SELECT avg(salario)
		FROM medico
		GROUP BY(especialidade)
	)
ORDER BY (salario) ASC;
-- 2.2
SELECT primeironome,
	numprontuario
FROM paciente
	JOIN usuario us USING(cpf)
	JOIN consulta co USING(numprontuario)
	JOIN medico ON(co.idregistromedico = medico.idregistro)
WHERE especialidade IN(
		SELECT DISTINCT especialidade
		FROM medico
		WHERE medico.especialidade = 'Clínico Geral'
	);
-- 2.3
SELECT primeironome cpf,
	numprontuario
FROM usuario
	JOIN (
		SELECT *
		FROM paciente
			JOIN consulta co USING(numprontuario)
		WHERE (
				EXTRACT(
					YEAR
					FROM co.dataconsulta
				),
				EXTRACT(
					MONTH
					FROM co.dataconsulta
				)
			) = (2018, 6)
	) AS junho_consul USING(cpf);
-- 2.4
SELECT idexame,
	nome
FROM (
		SELECT *
		FROM solicitacao_exame
		WHERE datarealizacao IS NOT NULL
	) AS realizados
	JOIN exame USING(idexame);
-- 2.5
SELECT idexame,
	nome
FROM (
		SELECT *
		FROM solicitacao_exame
		WHERE datarealizacao IS NOT NULL
	) AS realizados
	JOIN exame USING(idexame)
	JOIN laudo USING(idexame)
WHERE statuslaudo = 'Entregue';
-- 2.6
with soma_especialidades AS (
	SELECT especialidade,
		sum(salario) AS soma_es
	FROM medico
		JOIN medico_docente USING(idregistro)
	GROUP BY(especialidade)
)
SELECT *
FROM soma_especialidades
WHERE soma_es > 15000;
-- 2.7
SELECT primeironome,
	numcrm,
	especialidade,
	(salario + (salario * 0.05)) AS sal_com_bonus
FROM (
		SELECT idregistro,
			cpf,
			numcrm,
			salario,
			especialidade,
			count(*) AS num_consultas
		FROM medico me
			JOIN consulta con ON(con.idregistromedico = me.idregistro)
		GROUP BY(idregistro, cpf, numcrm, salario, especialidade)
		having count(*) > 9
	) AS medicos_bonus
	JOIN usuario USING(cpf);
