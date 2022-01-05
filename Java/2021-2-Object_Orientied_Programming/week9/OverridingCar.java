package week9;

class Car {
	public void accelate() {
		System.out.println("일반 엔진 사용");
	}
	public static void stop() {
		System.out.println("일반 브레이크 사용");
	}
}

class RacingCar extends Car {
	@Override
	public void accelate() {
		System.out.println("레이싱카 전용 엔진 사용");
	}
	public static void stop() {
		System.out.println("레이싱카 전용 브레이크 사용");
	}
}

public class OverridingCar {
	public static void main(String[] args) {
		Car myCar = new RacingCar();
		// 일반 메서드
		myCar.accelate();
		// 클래스 메서드
		myCar.stop();
	}
}
