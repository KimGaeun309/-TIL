package weekD;

/* ������ ����� ��� 1. Thread Ŭ������ ���

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

/* ������ ����� ��� 2. Runnable �������̽��� ����

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