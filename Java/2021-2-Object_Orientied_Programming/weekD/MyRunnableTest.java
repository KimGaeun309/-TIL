package weekD;

// Runnable 인터페이스로 스레드 생성

/* Runnable 인터페이스를 구현하는 방법
run() 메소드를 가지고 있는 클래스를 작성하고, 
이 클래스의 객체를 Thread 클래스의 생성자를 호출할 때 전달한다.
*/

class MyRunnable implements Runnable {
	@Override
	public void run() {
		for(int i=10; i>=0; i--)
			System.out.print(i+" ");
	}
}

public class MyRunnableTest {

	public static void main(String[] args) {
		Thread t = new Thread(new MyRunnable());
		t.start();	           // 이 부분이 다름!
	}

}
