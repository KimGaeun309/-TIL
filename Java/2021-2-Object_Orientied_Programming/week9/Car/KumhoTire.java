package week9_Car_poly;

public class KumhoTire extends Tire {
	public KumhoTire(String location, int maxRotation) {
		super(location ,maxRotation);
	}
	
	@Override
	public boolean roll() {
		++accumulatedRotation;
		if(accumulatedRotation < maxRotation) {
			System.out.println(location + " kumhoTire 수명: " + (maxRotation - accumulatedRotation) + "회");
			return true;
		} else {
			System.out.println("*** " + location + " KumhoTire 평크 ***");
			return false;
		}
	}
}