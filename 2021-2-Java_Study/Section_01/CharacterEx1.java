package Section_01;

// Java ��� �ǽ� - Character Ŭ���� ���

public class CharacterEx1 {
	
	// class extends
	
	
	
	public static void main(String[] args) {
		Character player = new Character("gamepari", 100, 12); // Player ��� ��ü�� �����Ǿ� ���� �ʱ�ȭ��
		Character enemy = new Character("Orc", 80, 5);
		
		while (player.isLive() && enemy.isLive()) {
			player.attack(enemy);
			if (!enemy.isLive()) break; // ���� �׾����� �ݺ��� ����������		
			enemy.attack(player);
		}
		
		if (player.isLive()) {
			System.out.println("player win");
		}
		else {
			System.out.println("enemy win");
		}
		
	}
	
}