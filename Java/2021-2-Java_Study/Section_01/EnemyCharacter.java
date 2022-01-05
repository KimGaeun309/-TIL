package Section_01;

//Java 상속 실습

public class EnemyCharacter extends Character {

	public EnemyCharacter(String name, int hp, int atk) {
		super(name, hp, atk);
	}
	
	@Override // 추가적으로 기능 더한다는 표시. (없어도 기능은 같음.)
	public void attack(Character enemy) {
		
		if (hp <= 20) {
			System.out.println("Orc is ANGRY....>O< !!!!");
			this.atk += 15;
		}
		
		super.attack(enemy);
		
		// PlayerCharacter로 형변환해 Heal() 사용!
		PlayerCharacter player = (PlayerCharacter)enemy;
		
		if (player.hp <= 30) {
			player.heal();
		}
	}
}
