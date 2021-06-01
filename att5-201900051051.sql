-- ALUNO: Micael Andrade Dos Santos 
-- TURMA: BF T01
-- MAT:  201900051051
-- Esquema universidade
SET search_path TO universidade;
-- 1.1 Precisava usar o distinct
SELECT nome
FROM disciplina AS di
	INNER JOIN turma AS tu USING (cod_disc);
-- 1.2
SELECT primeiro_nome,
	sobrenome,
	nome
FROM estudante es
	JOIN cursa cur ON(es.mat_estudante = cur.mat_estudante)
	JOIN turma USING(id_turma)
	JOIN disciplina USING(cod_disc)
	JOIN usuario USING (cpf);
-- 1.3
SELECT usrprof.primeiro_nome,
	usrprof.sobrenome,
	usrestud.primeiro_nome,
	usrestud.sobrenome
FROM plano
	JOIN estudante es USING(mat_estudante)
	JOIN professor pro USING(mat_professor)
	JOIN usuario usrprof ON (pro.cpf = usrprof.cpf)
	JOIN usuario usrestud ON (es.cpf = usrestud.cpf);
-- 1.4
SELECT usrprof.primeiro_nome,
	usrprof.sobrenome,
	nome,
	usraluno.primeiro_nome,
	usraluno.sobrenome
FROM turma
	JOIN leciona le USING(id_turma)
	JOIN professor pro USING(mat_professor)
	JOIN usuario usrprof USING(cpf)
	JOIN disciplina USING(cod_disc)
	JOIN cursa USING(id_turma)
	JOIN estudante aluno USING(mat_estudante)
	JOIN usuario usraluno ON(aluno.cpf = usraluno.cpf);
-- 1.5
SELECT d2.nome AS disciplina,
	d1.nome AS pre_requisito
FROM disciplina d1
	RIGHT JOIN disciplina d2 ON(d1.cod_disc = d2.pre_req);
--1.6
SELECT usrpro.primeiro_nome,
	usrpro.sobrenome,
	usrchef.primeiro_nome,
	usrchef.sobrenome
FROM professor pro
	JOIN departamento dep ON(pro.departamento = dep.cod_depto)
	JOIN usuario usrpro USING(cpf)
	JOIN professor chef ON(dep.chefe = chef.mat_professor)
	JOIN usuario usrchef ON(chef.cpf = usrchef.cpf);
-- 1.7 REVISAR
SELECT nome,
	turma,
	primeiro_nome,
	sobrenome
FROM disciplina
	JOIN turma USING(cod_disc)
	JOIN leciona USING(id_turma)
	JOIN professor USING(mat_professor)
	JOIN usuario USING(cpf)
WHERE pre_req IS NULL;
--1.8 REVISAR COM FULL JOIN
SELECT usraluno.primeiro_nome,
	usraluno.sobrenome,
	usrprof.primeiro_nome,
	usrprof.sobrenome
FROM estudante alu
	LEFT JOIN plano USING(mat_estudante)
	LEFT JOIN professor pro USING(mat_professor)
	LEFT JOIN usuario usrprof ON(usrprof.cpf = pro.cpf)
	LEFT JOIN usuario usraluno ON(usraluno.cpf = alu.cpf);
-- 1.9
SELECT DISTINCT usrpro.primeiro_nome,
	usrpro.sobrenome,
	usres.primeiro_nome,
	usres.sobrenome
FROM professor
	LEFT JOIN plano AS planopro USING(mat_professor)
	LEFT JOIN plano AS planoes ON(planopro.mat_estudante = planoes.mat_estudante)
	LEFT JOIN usuario AS usrpro ON(professor.cpf = usrpro.cpf)
	LEFT JOIN estudante AS es ON (es.mat_estudante = planoes.mat_estudante)
	LEFT JOIN usuario AS usres ON (es.cpf = usres.cpf);
-- 1.10
SELECT primeiro_nome,
	sobrenome
FROM professor
	JOIN usuario userprof USING(cpf)
UNION
SELECT primeiro_nome,
	sobrenome
FROM estudante
	JOIN usuario estu USING(cpf);
-- 1.11
SELECT primeiro_nome,
	sobrenome
FROM professor
	LEFT JOIN leciona USING(mat_professor)
	JOIN usuario USING(cpf)
WHERE id_turma IS NULL;
-- 1.12
SELECT nome
from turma
	join cursa USING(id_turma)
	RIGHT join disciplina USING(cod_disc)
WHERE id_turma IS NULL;
-- 1.13
SELECT DISTINCT pro.mat_professor
FROM professor pro
	LEFT JOIN departamento de ON(de.chefe = pro.mat_professor)
	LEFT JOIN plano pla ON(pla.mat_professor = pro.mat_professor)
WHERE (de.chefe IS NOT NULL)
	OR (pla.id_projeto IS NOT NULL);
--1.14
SELECT DISTINCT mat_professor
FROM plano pla
	JOIN departamento dep ON(dep.chefe = pla.mat_professor);
-- 1.15
SELECT DISTINCT mat_professor
FROM plano pla
	LEFT JOIN departamento dep ON(dep.chefe = pla.mat_professor)
WHERE dep.chefe IS NULL;
-- Esquema hospital
SET search_path TO hospital;
-- 2.1
SELECT *
FROM usuario
WHERE usuario.sobrenome LIKE '%sa%';
-- 2.2
SELECT COUNT(sobrenome) AS comeca_com_s
FROM usuario
WHERE usuario.sobrenome LIKE 'S%';
-- 2.3
SELECT primeironome,
	cpf
FROM paciente
	JOIN usuario USING(cpf);
-- 2.4
SELECT SUM(salario) AS soma_sal_med_ativos
from medico
	JOIN usuario USING(cpf)
	JOIN perfil USING(idperfil)
WHERE ativo = 'S';
-- 2.5
SELECT usrpaciente.primeironome AS paciente,
	usrpaciente.cpf AS paciente_cpf,
	usracomp.primeironome AS acompanhante,
	usracomp.cpf AS acompanhante_cpf
FROM paciente pa
	JOIN acompanhante acomp ON (pa.cpfacomp = acomp.cpf)
	JOIN usuario usrpaciente ON(pa.cpf = usrpaciente.cpf)
	JOIN usuario usracomp ON (acomp.cpf = usracomp.cpf);
-- 2.6
SELECT DISTINCT primeironome,
	cpf
FROM paciente
	JOIN consulta USING(numprontuario)
	JOIN usuario USING(cpf);
-- 2.7
select DISTINCT primeironome as paciente,
	cpf,
	numprontuario,
	nome as nome_medciamento
FROM paciente
	join prescricao pre using (numprontuario)
	join usuario using(cpf)
	join medicamento using(idmedicamento);