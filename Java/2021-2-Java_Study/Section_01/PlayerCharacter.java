package Section_01;

//Java »ó¼Ó ½Ç½À

public class PlayerCharacter extends Character {
	
	public PlayerCharacter(String name, int hp, int atk) {
		super(name, hp, atk);
	}
	
	public void heal() {
		hp += 20;
		System.out.println(name + " HEAL!!!!");
		System.out.println(name + " HP : " + hp);
	}

}
