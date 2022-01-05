package ch06;
/*
class Tv {
	String color;
	boolean power;
	int channel;
	
	void power() = {power = !power; };
	void channelUp() = {++channel;}
	void channelDown() = {--channel;)
}
*/
public class TvTest3 {

	public static void main(String[] args) {
		Tv t1 = new Tv();
		Tv t2 = new Tv();
		System.out.println("t1의 channel값은 " + t1.channel + "입니다.");
		System.out.println("t2의 channel값은 " + t2.channel + "입니다.");
		
		t2 = t1; // t1이 저장하고 있는 값(주소)를 t2에 저장. t2는 t1이 참조하고 있던 인스턴스를 같이 참조하게 된다.
		t1.channel = 7;
		System.out.println("t1의 channel값을 7로 변경했습니다.");
		
		System.out.println("t1의 channel값은 " + t1.channel + "입니다.");
		System.out.println("t2의 channel값은 " + t2.channel + "입니다.");
	}

}
