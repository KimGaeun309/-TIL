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
		System.out.println("t1�� channel���� " + t1.channel + "�Դϴ�.");
		System.out.println("t2�� channel���� " + t2.channel + "�Դϴ�.");
		
		t2 = t1; // t1�� �����ϰ� �ִ� ��(�ּ�)�� t2�� ����. t2�� t1�� �����ϰ� �ִ� �ν��Ͻ��� ���� �����ϰ� �ȴ�.
		t1.channel = 7;
		System.out.println("t1�� channel���� 7�� �����߽��ϴ�.");
		
		System.out.println("t1�� channel���� " + t1.channel + "�Դϴ�.");
		System.out.println("t2�� channel���� " + t2.channel + "�Դϴ�.");
	}

}
