package weekB;


public abstract class Animal {
	public String kind;
	
	public void breathe() {
		System.out.println("¼ûÀ» ½±´Ï´Ù.");
	}
	
	public abstract void sound();
}

class Cat extends Animal {
	public Cat() {
		this.kind = "Æ÷À¯·ù";
	}
	@Override
	public void sound() {
		System.out.println("¾ß¿Ë");
	}
}

class Dog extends Animal {
	public Dog() {
		this.kind = "Æ÷À¯·ù";
	}
	@Override
	public void sound() {
		System.out.println("¸Û¸Û");
	}
}
