package dio.banco.digital.domain.model;

import java.util.ArrayList;
import java.util.List;

public class Banco {

	private List<Conta> contas = new ArrayList<>();

	public void criarContaCorrente(String nome) {
		ContaCorrente novaConta = new ContaCorrente(nome);
		contas.add(novaConta);
	}

	public void criarContaPoupanca(String nome) {
		ContaPoupanca novaConta = new ContaPoupanca(nome);
		contas.add(novaConta);
	}

	public ContaCorrente getContaCorrentePorNome(String nome) {
		return (ContaCorrente) contas.stream()
				.filter(c -> c instanceof ContaCorrente && c.getCliente().getNome().equalsIgnoreCase(nome)).findFirst()
				.orElse(null);
	}

	public ContaPoupanca getContaPoupancaPorNome(String nome) {
		return (ContaPoupanca) contas.stream()
				.filter(c -> c instanceof ContaPoupanca && c.getCliente().getNome().equalsIgnoreCase(nome)).findFirst()
				.orElse(null);
	}
	
}
