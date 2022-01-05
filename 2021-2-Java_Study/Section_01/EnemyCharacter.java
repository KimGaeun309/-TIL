package Section_01;

//Java ��� �ǽ�

public class EnemyCharacter extends Character {

	public EnemyCharacter(String name, int hp, int atk) {
		super(name, hp, atk);
	}
	
	@Override // �߰������� ��� ���Ѵٴ� ǥ��. (��� ����� ����.)
	public void attack(Character enemy) {
		
		if (hp <= 20) {
			System.out.println("Orc is ANGRY....>O< !!!!");
			this.atk += 15;
		}
		
		super.attack(enemy);
		
		// PlayerCharacter�� ����ȯ�� Heal() ���!
		PlayerCharacter player = (PlayerCharacter)enemy;
		
		if (player.hp <= 30) {
			player.heal();
		}
	}
}
