package dioambiente.desafio6;

import java.util.Objects;

public class Convidado {
	private String nome;
	private int convite;

	public Convidado(String nome, int convite) {
		this.nome = nome;
		this.convite = convite;
	}

	@Override
	public String toString() {
		return "Convidado [nome=" + nome + ", convite=" + convite + "]";
	}
	
	
	

	@Override
	public int hashCode() {
		return Objects.hash(convite);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Convidado other = (Convidado) obj;
		return convite == other.convite;
	}

	public String getNome() {
		return nome;
	}

	public int getConvite() {
		return convite;
	}

}
