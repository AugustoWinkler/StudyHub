package dio.banco.digital.domain.model;

public class ContaPoupanca extends Conta {

	public ContaPoupanca(String nome) {
		super(nome);
	}

	@Override
	public void imprimir() {
		System.out.println("===== INFO CONTA POUPANÇA =====");
		super.imprimir();
	}

}
