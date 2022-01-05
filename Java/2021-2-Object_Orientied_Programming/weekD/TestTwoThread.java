package weekD;

// 두 개의 스레드

class MyTestRunnable implements Runnable {
	String myName;
	public MyTestRunnable(String name) {
		myName = name;
	}
	
	@Override
	public void run() {
		for(int i=10; i>=0; i--)
			System.out.print(myName + i + " ");
	}
}

public class TestTwoThread {

	public static void main(String[] args) {
		Thread t1 = new Thread(new MyTestRunnable("A"));
		Thread t2 = new Thread(new MyTestRunnable("B"));
		t1.start();
		t2.start();
	}

}
