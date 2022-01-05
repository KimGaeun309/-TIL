package Week6;
import java.util.ArrayList;

class GameCharacter {
	private class GameItem {
		String name;
		int type;
		int price;
		
		int getPrice() { return price; }
		
		@Override
		public String toString() {
			return "GameItem[name = " + name + ", type = " + type + ", price = " + price + "]";
		}
		
	}
	
	private ArrayList<GameItem> list = new ArrayList<>0;
	
	public void add(String name, int type, int price) {
		GameItem item = new GameItem();
		item.type = type;
		item.name = name;
		item.price = price;
		list.add(item);
	}
	
	public void print() {
		int total = 0;
		for (GameItem item : list) {
			System.out.println(item);
			total += item.getPrice();
		}
		System.out.println(total);
	}
}

public class InnerClassEx {

	public static void main(String[] args) {
		GameCharacter charac = new GameCharacter();
		charac.add("Sward", 1, 100);
		charac.add("Gun", 2, 50);
		charac.print();

	}

}
