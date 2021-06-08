-- ALUNO: Micael Andrade Dos Santos 
-- TURMA: BF T01
-- MAT:  201900051051
-- Esquema universidade
-- TODO: FORMATAR 
SET search_path TO universidade;
-- 1.1
-- 1.1
WITH estudantes_p200 AS (
	select *
	from estudante
		JOIN plano pla USING(mat_estudante)
	WHERE mat_professor = 'P200'
)
SELECT estudantes_p200.mat_estudante
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
--1.7
select ur.primeiro_nome,
	ur.sobrenome
from professor pro2
	join cargo car2 ON (car2.id_cargo = pro2.cargo)
	join usuario ur using(cpf)
where car2.salario = (
		select min(salario)
		from professor pro
			join cargo car ON(car.id_cargo = pro.cargo)
	);
-- 1.8
select primeiro_nome,
	sobrenome
FROM (
		select *
		from cursa
		where nota in (
				select min(nota)
				from cursa
			)
	) as al_menor
	JOIN estudante using(mat_estudante)
	join usuario using(cpf);
-- 1.9
select primeiro_nome,
	sobrenome,
	maior_5,
	menor_5
FROM (
		select mat_estudante,
			count(cod_disc) as maior_5
		from (
				select *
				from cursa
				where nota >= 5
			) as maior_5
			join turma using(id_turma)
		group by (mat_estudante)
	) as notas_maiores_5
	join (
		select mat_estudante,
			count(cod_disc) as menor_5
		from (
				select *
				from cursa
				where nota < 5
			) as maior_5
			join turma using(id_turma)
		group by (mat_estudante)
	) as notas_menores_5 using(mat_estudante)
	join estudante using(mat_estudante)
	join usuario using(cpf);
-- 1.10
-- semelhante a 1.6, fazer consulta co-relacionadas
-- não precisa SOME some nem ALL
-- Esquema hospital
SET search_path TO hospital;
-- 2.1
SET search_path TO hospital;
select numcrm,
	primeironome,
	especialidade,
	salario
from medico
	join usuario using(cpf)
where medico.salario >= SOME (
		select avg(salario)
		from medico
		group by(especialidade)
	)
order by (salario) ASC;
-- 2.2
select primeironome,
	numprontuario
from paciente
	join usuario us using(cpf)
	join consulta co using(numprontuario)
	join medico ON(co.idregistromedico = medico.idregistro)
where especialidade IN(
		select DISTINCT especialidade
		from medico
		where medico.especialidade = 'Clínico Geral'
	);
-- 2.3
select primeironome cpf,
	numprontuario
from usuario
	join (
		select *
		from paciente
			join consulta co using(numprontuario)
		where (
				EXTRACT(
					YEAR
					FROM co.dataconsulta
				),
				EXTRACT(
					MONTH
					FROM co.dataconsulta
				)
			) = (2018, 6)
	) as junho_consul using(cpf);
-- 2.4
select idexame,
	nome
from (
		select *
		from solicitacao_exame
		where datarealizacao is not null
	) as realizados
	join exame using(idexame);
-- 2.5
where datarealizacao is not null
) as realizados
join exame using(idexame)
join laudo using(idexame)
where statuslaudo = 'Entregue';
-- 2.6
with soma_especialidades as (
	select especialidade,
		sum(salario) as soma_es
	from medico
		join medico_docente using(idregistro)
	group by(especialidade)
)
select *
from soma_especialidades
where soma_es > 15000;
-- 2.7
select primeironome,
	numcrm,
	especialidade,
	(salario + (salario * 0.05)) AS sal_com_bonus
from (
		select idregistro,
			cpf,
			numcrm,
			salario,
			especialidade,
			count(*) AS num_consultas
		from medico me
			join consulta con ON(con.idregistromedico = me.idregistro)
		group by(idregistro, cpf, numcrm, salario, especialidade)
		having count(*) > 9
	) as medicos_bonus
	join usuario using(cpf);