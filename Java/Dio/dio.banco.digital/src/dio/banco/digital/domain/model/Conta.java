package dio.banco.digital.domain.model;

import dio.banco.digital.domain.repository.ContaRepository;

abstract class Conta implements ContaRepository {

	private static int AGENCIA_PADRAO = 1;
	private static int NUMERO_CONTA = 1;

	protected int agencia;
	protected int numero;
	protected double saldo;
	protected Cliente cliente;

	public Conta(String nome) {
		this.agencia = AGENCIA_PADRAO++;
		this.numero = NUMERO_CONTA++;
		this.saldo = 0;
		this.cliente = new Cliente(nome);
	}

	@Override
	public void saque(int valor) {
		if (this.saldo < valor) {
			return;
		} else {
			this.saldo -= valor;
		}
	}

	@Override
	public void deposito(int valor) {
		this.saldo += valor;
	}

	@Override
	public void transferir(int valor, ContaRepository contaDestino) {
		if (this.saldo < valor) {
			return;
		} else {
			this.saldo -= valor;
		}
		contaDestino.deposito(valor);
	}

	public void imprimir() {
		System.out.println(String.format("Agencia: %d", this.agencia));
		System.out.println(String.format("Conta: %d", this.numero));
		System.out.println(String.format("Saldo: %.2f", this.saldo));
		System.out.println(String.format("Proprietário %s: ", this.cliente.getNome()));
	}

	public Cliente getCliente() {
		return cliente;
	}

}
