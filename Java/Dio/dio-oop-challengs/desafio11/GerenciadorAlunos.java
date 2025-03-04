package dioambiente.desafio11;

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class GerenciadorAlunos {
	Set<Aluno> alunos = new HashSet<>();

	public void adicionarAluno(String nome, long matricula, double media) {
		Aluno aluno = new Aluno(nome, matricula, media);
		alunos.add(aluno);
	}

	public void removerAluno(long matricula) {
		alunos.removeIf(t -> t.getMatricula() == matricula);
	}

	public Set<Aluno> exibirPorNome() {
		Set<Aluno> alunosPorNome = new TreeSet<>(alunos);
		return alunosPorNome;
	}

	public Set<Aluno> exibirPorNota() {
		Set<Aluno> alunosPorMedia = new TreeSet<>(new ComparatorPorNota());
		alunosPorMedia.addAll(alunos);
		return alunosPorMedia;
	}

	public Set<Aluno> exibirAlunos() {
		return alunos;
	}
}
