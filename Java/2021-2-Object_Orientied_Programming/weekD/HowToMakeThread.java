package weekD;

/* 스레드 만드는 방법 1. Thread 클래스를 상속

class PrimeThread extends Thread {
	long minPrime;
	PrimeThread(long minPrime) {
		this.minPrime = minPrime;
	}
	
	public void run() {
		// compute primes larger than minPrime
		...
	}
}

PrimeThread p = new PrimThread(143);
p.start();

*/

/* 스레드 만드는 방법 2. Runnable 인터페이스를 구현

class PrimeRun implements Runnable {
	long minPrime;
	PrimeRun(long minPrime) {
		this.minPrime = minPrime;
	}
	
	public void run() {
		// compute larger than minPrime
		...
	}
}

PrimeRun p = new PrimeRun(143);
new Thread(p).start();

*/