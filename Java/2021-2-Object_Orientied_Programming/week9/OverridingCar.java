package week9;

class Car {
	public void accelate() {
		System.out.println("�Ϲ� ���� ���");
	}
	public static void stop() {
		System.out.println("�Ϲ� �극��ũ ���");
	}
}

class RacingCar extends Car {
	@Override
	public void accelate() {
		System.out.println("���̽�ī ���� ���� ���");
	}
	public static void stop() {
		System.out.println("���̽�ī ���� �극��ũ ���");
	}
}

public class OverridingCar {
	public static void main(String[] args) {
		Car myCar = new RacingCar();
		// �Ϲ� �޼���
		myCar.accelate();
		// Ŭ���� �޼���
		myCar.stop();
	}
}
