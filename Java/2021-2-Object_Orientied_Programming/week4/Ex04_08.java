package Week4;

class Television2 {
	int channel;
	int volume;
	boolean onOff;
	void print() {
		System.out.println("ä���� " + channel + "�̰� ������ " + volume + "�Դϴ�.");
	}
	int getChannel() {
		return channel;
	}
	void setChannel(int ch) {
		channel = ch;
	}
}

public class Ex04_08 {

	public static void main(String[] args) {
		Television2 myTv = new Television2();
		myTv.setChannel(11);
		int ch =  myTv.getChannel();
		System.out.println("���� ä���� " + ch + "�Դϴ�.");

	}

}
