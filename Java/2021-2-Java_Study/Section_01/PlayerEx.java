package Section_01;

// Java 클래스 실습

public class PlayerEx {
	
	// class
	
	static class Player {
		
		String name;
		int hp; 
		int atk;
		
		// 생성자
		public Player(String name, int hp, int atk) {
			this.name = name; // this 는 Player 객체
			this.hp = hp;
			this.atk = atk; 
		}
		
		public void attack(Enemy enemy) {
			System.out.println("Enemy attack!");
			enemy.hp -= this.atk;
			System.out.println("Enemy hp : " + enemy.hp);
		}
		
		public boolean isLive() {
			if (hp <= 0) {
				return false;
			}
			else {
				return true;
			}
		}
	}
	
	static class Enemy {
		String name;
		int hp;
		int atk;
		
		public Enemy(String name, int hp, int atk) {
			this.name = name; 
			this.hp = hp;
			this.atk = atk; 
		}
		
		public void attack(Player player) {
			System.out.println("Player attack!");
			player.hp -= this.atk;
			System.out.println("Player hp : " + player.hp);
		}
		
		public boolean isLive() {
			if (hp <= 0) {
				return false;
			}
			else {
				return true;
			}
		}
	}

	public static void main(String[] args) {
		
		Player player = new Player("gamepari", 100, 12); // Player 라는 객체가 생성되어 값이 초기화됨
		Enemy enemy = new Enemy("Orc", 80, 5);
		
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
