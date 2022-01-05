package Section_01;

//Java ��� �ǽ� - PlayerCharacter Ŭ����, EnemyCharacter Ŭ���� ��� (Character Ŭ������ �ڽ� Ŭ������)

public class CharacterEx2 {

	// class extends
	
	public static void main(String[] args) {
		PlayerCharacter player = new PlayerCharacter("gamepari", 70, 12); // Player ��� ��ü�� �����Ǿ� ���� �ʱ�ȭ��
		EnemyCharacter enemy = new EnemyCharacter("Orc", 80, 5);
		
		while (player.isLive() && enemy.isLive()) {
			player.attack(enemy);
			if (!enemy.isLive()) break; // ���� �׾����� �ݺ��� ����������		
			enemy.attack(player);
			System.out.println("----------------------------------");
		}
		
		if (player.isLive()) {
			System.out.println("player win");
		}
		else {
			System.out.println("enemy win");
		}
		
	}

}

