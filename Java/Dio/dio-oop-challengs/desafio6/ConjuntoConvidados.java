package dioambiente.desafio6;

import java.util.HashSet;
import java.util.Set;

public class ConjuntoConvidados {
	private Set<Convidado> convidadosSet;

	public ConjuntoConvidados() {
		this.convidadosSet = new HashSet<>();
	}

	public void adicionarConvidado(String nome, int convite) {
		convidadosSet.add(new Convidado(nome, convite));
	}

	public void removerConvidado(String codigoConvite) {
		convidadosSet.removeIf(t -> Integer.toString(t.getConvite()).equals(codigoConvite));
	}

	public int contarConvidados() {
		return this.convidadosSet.size();
	}

	public void exibirConvidados() {
		System.out.println(convidadosSet.toString());
	}

	public static void main(String[] args) {
			ConjuntoConvidados convidados =  new ConjuntoConvidados();
			
			convidados.adicionarConvidado("José", 2);
			convidados.adicionarConvidado("Maria", 3);
			convidados.adicionarConvidado("Mariana", 3);
			convidados.adicionarConvidado("Pedro", 4);
			System.out.println(convidados.contarConvidados());
			convidados.exibirConvidados();
			

	}

}
