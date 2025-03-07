package dio.banco.digital.domain.repository;

public interface ContaRepository {

	void saque(int valor);

	void deposito(int valor);

	void transferir(int valor, ContaRepository contaDestino);
}
