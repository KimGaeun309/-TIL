package Section_01;

//interface part 1
// Animal Ŭ����

public class InterfacePart1 {
	
	public static void main(String[] args) {
		
		Animal dog = new Dog("baduk");
		Animal cat = new Cat("nyaong");
		Animal wolf = new Wolf("waoooo");
		
		dog.Cry();
		cat.Cry();
		wolf.Cry();
		
		System.out.println("------------------");
		
		// �������̽�
		Pet pet1 = new Cat("nyaong");
		Pet pet2 = new Dog("baduk");
		
		pet1.FoodCall();
		pet2.FoodCall();
		
		System.out.println("------------------");
		
		// ����ȯ
		((Cat)pet1).Cry();
	}

}
