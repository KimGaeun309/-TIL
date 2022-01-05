package Section_01;

// Java 상속 실습 - Character 클래스 사용

public class CharacterEx1 {
	
	// class extends
	
	
	
	public static void main(String[] args) {
		Character player = new Character("gamepari", 100, 12); // Player 라는 객체가 생성되어 값이 초기화됨
		Character enemy = new Character("Orc", 80, 5);
		
		while (player.isLive() && enemy.isLive()) {
			player.attack(enemy);
			if (!enemy.isLive()) break; // 적이 죽었으니 반복문 빠져나오기		
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