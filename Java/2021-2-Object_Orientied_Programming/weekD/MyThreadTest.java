package weekD;

// Thread 클래스로 스레드 생성

/* Thread 클래스를 상속하는 방법
 Thread 클래스를 상속받은 후에 run() 메소드를 재정의한다.
 run() 메소드 안에 작업을 기술한다.
*/

class MyThread extends Thread {
	@Override
	public void run() {
		for (int i=10; i>=0; i--) {
			System.out.print(i + " ");
		}
	}
}

public class MyThreadTest {

	public static void main(String[] args) {
		Thread t = new MyThread();
		t.start();
	}

}
