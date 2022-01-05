package Section_01;

//Java 상속 실습 - PlayerCharacter 클래스, EnemyCharacter 클래스 사용 (Character 클래스의 자식 클래스인)

public class CharacterEx2 {

	// class extends
	
	public static void main(String[] args) {
		PlayerCharacter player = new PlayerCharacter("gamepari", 70, 12); // Player 라는 객체가 생성되어 값이 초기화됨
		EnemyCharacter enemy = new EnemyCharacter("Orc", 80, 5);
		
		while (player.isLive() && enemy.isLive()) {
			player.attack(enemy);
			if (!enemy.isLive()) break; // 적이 죽었으니 반복문 빠져나오기		
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

