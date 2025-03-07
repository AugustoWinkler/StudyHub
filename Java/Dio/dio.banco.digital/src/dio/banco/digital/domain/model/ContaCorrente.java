package dio.banco.digital.domain.model;

public class ContaCorrente extends Conta {

	public ContaCorrente(String nome) {
		super(nome);
	}

	@Override
	public void imprimir() {
		System.out.println("===== INFO CONTA CORRENTE =====");
		super.imprimir();
	}

}
