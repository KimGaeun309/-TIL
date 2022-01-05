package weekD;

// flag를 이용한 종료

public class FlagThread extends Thread {
	private int n = 0;
	private boolean flag = false;
	public void finish() {flag = true;}
	
	@Override
	public void run() {
		while(true) {
			System.out.println(n); // 화면에 카운트 값 출력
			n++;
			try {
				sleep(1000);
				if(flag == true)
					return; // 스레드 종료
			}
			catch(InterruptedException e) {
				return;
			}
		}
	}
	
	public static void main(String[] args) {
		FlagThread th = new FlagThread();
		th.start();
		
		th.finish(); // FlagThread 강제 종료
	}

}
