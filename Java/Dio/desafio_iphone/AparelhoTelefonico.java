package iPhone;

public class AparelhoTelefonico {
	public void ligar(String numero) {
		System.out.println("Ligando para: ".concat(numero));
	}

	public void pausar() {
		System.out.println("Pausar música...");
	}

	public void selecionarMúsica(String musica) {
		System.out.println("Tocando: " + musica);
	}
}
