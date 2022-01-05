package weekD;

// Runnable 인터페이스를 상속받아 1초 단위로 시간을 출력하는 스레드

/*
class TimerRunnable implements Runnable {
	int n = 0;
	
	@Override
	public void run() {
		while(true) {
			System.out.println(n);
			n++;
			try {
				Thread.sleep(1000);
			}
			catch(InterruptedException e) {return;}
		}
	}
}

public class TimeRunnable {

	public static void main(String[] args) {
		Thread th = new Thread(new TimerRunnable()); // 생성자의 매개변수에 Runnable 타겟의 객체.
		th.start();
	}

}
*/