package weekB;


public abstract class Animal {
	public String kind;
	
	public void breathe() {
		System.out.println("���� ���ϴ�.");
	}
	
	public abstract void sound();
}

class Cat extends Animal {
	public Cat() {
		this.kind = "������";
	}
	@Override
	public void sound() {
		System.out.println("�߿�");
	}
}

class Dog extends Animal {
	public Dog() {
		this.kind = "������";
	}
	@Override
	public void sound() {
		System.out.println("�۸�");
	}
}
