package Week4;

class Television1 {
	int channel;
	int volume;
	boolean onOff;
	void print() {
		System.out.println("ä���� " + channel + "�̰� ������ " + volume + "�Դϴ�."); 
	}
	int getChannel() {
		return channel;
	}
}

public class Ex04_05 {

	public static void main(String[] args) {
		Television1 myTv = new Television1();
		myTv.channel = 7;
		myTv.volume = 9;
		myTv.onOff = true;
		int ch = myTv.getChannel();
		System.out.println("���� ä���� " + ch + "�Դϴ�.");
	}

}
