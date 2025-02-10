package iPhone;

public class iPhone {
	private ReprodutorMusical reprodutorMusical;
	private AparelhoTelefonico aparelhoTelefonico;
	private NavegadorInternet navegadorInternet;
	
	public iPhone(){
		this.reprodutorMusical = new ReprodutorMusical();
        this.aparelhoTelefonico = new AparelhoTelefonico();
        this.navegadorInternet = new NavegadorInternet();
	}
}
