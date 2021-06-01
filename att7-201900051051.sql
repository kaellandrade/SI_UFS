-- ALUNO: Micael Andrade Dos Santos 
-- TURMA: BF T01
-- MAT:  201900051051
-- Esquema universidade
SET search_path TO universidade;
-- 1.1
-- 1.1
WITH estudantes_p200 AS (
	select *
	from estudante
		JOIN plano pla USING(mat_estudante)
	WHERE mat_professor = 'P200'
)
SELECT *
from estudantes_p200
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
select mat_professor
from nao_orientam
	left join departamento ON(nao_orientam.mat_professor = chefe)
where chefe is NULL;
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

select mat_professor,
	prof_media,
	departamento_media
FROM (
		select mat_professor,
			depto_responsavel,
			avg(nota) AS prof_media
		from cursa
			join turma using(id_turma)
			join leciona using(id_turma)
			join disciplina using(cod_disc)
		group by(mat_professor, depto_responsavel)
	) as media_prof
	JOIN (
		select depto_responsavel,
			avg(nota) AS departamento_media
		from cursa
			join turma using(id_turma)
			join disciplina using(cod_disc)
		group by depto_responsavel
	) AS media_dep using(depto_responsavel);