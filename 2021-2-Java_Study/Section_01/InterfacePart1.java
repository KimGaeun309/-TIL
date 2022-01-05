package Section_01;

//interface part 1
// Animal 클래스

public class InterfacePart1 {
	
	public static void main(String[] args) {
		
		Animal dog = new Dog("baduk");
		Animal cat = new Cat("nyaong");
		Animal wolf = new Wolf("waoooo");
		
		dog.Cry();
		cat.Cry();
		wolf.Cry();
		
		System.out.println("------------------");
		
		// 인터페이스
		Pet pet1 = new Cat("nyaong");
		Pet pet2 = new Dog("baduk");
		
		pet1.FoodCall();
		pet2.FoodCall();
		
		System.out.println("------------------");
		
		// 형변환
		((Cat)pet1).Cry();
	}

}
