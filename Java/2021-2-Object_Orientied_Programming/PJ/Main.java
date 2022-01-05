package java_homework;

/* [주석 1 : 과제 설명]

객체지향프로그래밍 평가과제 (배점 25점)
학과 : 컴퓨터.전자시스템공학과
학번 : 202000376
이름 : 김가은

과제 주제 : 코로나 확진자의 이름과 주민번호를 입력하면 방문 기록을 통해 접촉자 명단을 출력하는 프로그램

*/

import javax.swing.JOptionPane;

class Person {
	public String name;
	public Integer regidentNumber;
	public double temperature;
	public int family;
	Person() {
		this.name = "";
		this.regidentNumber = 0;
		this.temperature = 36;
		this.family = 0;
	}
}

interface Condition {
	void temperatureHighOrLow();
}

interface Situation {
	void aloneOrNot();
}

//// [주석 2] 클래스 상속, [주석 11] 다중 인터페이스 
class Customer extends Person implements Condition, Situation {
	private String visited[] = new String[20];
	private int idx = 0;
	
	@Override //// [주석 6] 오버라이딩 
	public void temperatureHighOrLow() { 
		if (this.temperature > 37.5) 
			System.out.println("열이 납니다.");
		else
			System.out.println("열이 나지 않습니다.");
		
	}
	
	@Override
	public void aloneOrNot() {
		if (this.family == 0)
			System.out.println("혼자 삽니다.");
		else
			System.out.println(this.family + " 명의 가족이 있습니다.");
	}
	
	//// [주석 3] 생성자
	Customer(String name, int regidentNumber, double temperature, int family) {
		this.name = name;
		//// [주석 9] Wrapper 객체의 박싱 
		this.regidentNumber = regidentNumber; 
		this.temperature = temperature;
		this.family = family;
	}
	
	
	
	//// [주석 5] 오버로딩
	Customer() {
			super(); // 부모 클래스의 생성자 호출
		}

	
	void Visit(String store) {
		//// [주석 10] 예외처리
		try {		
			visited[idx] = store;
			idx++;
		}
		catch (ArrayIndexOutOfBoundsException e) {
			System.out.println(this.name + " 님이 방문 가능 횟수를 초과하였습니다.");
		}
	}
	
}

//// [주석 7] 추상 클래스
abstract class Store {
	public String name;
	public String visitLog[] = new String[100];
	public int idx = 0;
	public int returnIdx(String n) {
		
		for(int i=0; i < idx; i++) {
			if (visitLog[i].equals(n))
				return i+1;
		}
		return -1; // 존재X
	}
	public String[] returnCustomer(int id) {
		String list[] = new String[idx - id];
		for(int j=id; j<idx; j++) {
			list[j - id] = visitLog[j];
		}
		return list;
	}
	
	

	public abstract void printCustomerNumber(int id);
	public abstract void Visit(String n); 
}

class CoffeeShop extends Store {
	public boolean mask = false;	
	public static int coffee_count = 0; // 커피숍 방문객 수 체크 (모든 가게 통합)
	//// [주석 4] static 메소드
	public static int getCount() {
		return coffee_count;
	}
	
	CoffeeShop(String name) {
		this.name = name;
	}
	
	@Override
	public void Visit(String n) {
		try {
			visitLog[idx] = n;
			idx++;
			coffee_count++;
		}
		catch (ArrayIndexOutOfBoundsException e) {
			System.out.println( this.name + " 에 방문 가능한 인원를 초과하였습니다.");
		}
	}
	
	
	@Override
	public void printCustomerNumber(int id) {
		System.out.println("\n=============================================");
		System.out.println(this.name + " 커피숍에서 확진자가 발생하였습니다.");
		System.out.println(" 중요도 : *****(커피숍에서는 마스크를 벗습니다)");
		System.out.println(" 접촉자 : " + (idx - id) + " 명");
		System.out.println(" 오늘 하루 전체 커피숍 방문자 수는 " + coffee_count + " 명");
		System.out.println("=============================================");
	}
	
}

class SuperMarket extends Store {
	public boolean mask = true;
	public static int super_count; // 커피숍 방문객 수 체크 (모든 가게 통합)
	//// [주석 4] static 메소드
	public static int getCount() {
		return super_count;
	}
	
	SuperMarket(String name) {
		this.name = name;
	}
	
	@Override
	public void Visit(String n) {
		if (idx >= 100) {
			System.out.println("방문 가능 고객 수를 초과하였습니다.");
			
		}
		else {
			visitLog[idx] = n;
			idx++;
			super_count++;
		}
	}
	
	@Override
	public void printCustomerNumber(int id) {
		System.out.println("\n=============================================");
		System.out.println(this.name + " 슈퍼마켓에서 확진자가 발생하였습니다.");
		System.out.println(" 중요도 : **   (슈퍼마켓에서는 마스크를 벗지 않습니다)");
		System.out.println(" 접촉자 : " + (idx - id) + " 명");
		System.out.println(" 오늘 하루 전체  슈퍼마켓 방문자 수는 " + super_count + " 명");
		System.out.println("=============================================");
	}
}



public class Main {
	
	//// [주석 12] 다중스레드 (Thread 클래스)
	static class PrintAttatched extends Thread {
		public void run() {
			for (int i=0; i<store.length; i++) {
				int id = store[i].returnIdx(s);
				if (id != -1) {
					store[i].printCustomerNumber(id);
					String cus_list[] = store[i].returnCustomer(id);
					
					for (int j=0; j<cus_list.length; j++) {
						 for (int k=0; k<customer.length; k++) {
							 if (customer[k].name.equals(cus_list[j])) {
								 System.out.println(customer[k].name + "(" + customer[k].regidentNumber + ") 은 확진자와 접촉하였습니다.");
								 customer[k].temperatureHighOrLow();
								 customer[k].aloneOrNot();
								 System.out.println("--------------------------------------------");
							 }
						 }
					}
				}
			}
		}
	}
	
	////[주석 13] 다중스레드 (Runnable 인터페이스)
	static class PrintLine implements Runnable {
		public void run() {
			for (int i=0; i<store.length; i++) {
				if (store[i].name == null)
					break;
				System.out.println(store[i].name + " 방문자 목록");
				for (int j=0; j<store[i].visitLog.length; j++) {
					if (store[i].visitLog[j] == null)
						break;
					System.out.println(store[i].visitLog[j]); 
				}
			}
			
		}
	}
	
	public static Customer customer[] = new Customer[5];
	
	public static Store store[] = new Store[2];
	
	public static String s;
	
	public static void main(String[] args) {
		
		customer[0] = new Customer("홍길동", 12345, 36.5, 0);
		customer[1] = new Customer("김철수", 23456, 37.7, 3);
		customer[2] = new Customer("박영희", 34567, 36.8, 0);
		customer[3] = new Customer();
		customer[4] = new Customer("전우치", 56789, 38, 2);
		
		customer[3].name =  "심청";
		customer[3].regidentNumber = 45678;
		customer[3].temperature = 36.6;
		customer[3].family = 1;
		
		
		//// [주석 8] 다형성
		store[0] = new SuperMarket("eMart");
		store[1] = new CoffeeShop("starbucks");
		
		customer[0].Visit(store[0].name); // eMart에 홍길동이 방문
		store[0].Visit(customer[0].name);
		
		customer[0].Visit(store[1].name); // starbucks에 홍길동이 방문
		store[1].Visit(customer[0].name);
		
		customer[1].Visit(store[1].name); // starbucks에 김철수가 방문
		store[1].Visit(customer[1].name);
		
		customer[2].Visit(store[1].name); // starbucks에 박영희가 방문
		store[1].Visit(customer[2].name);
		
		customer[3].Visit(store[0].name); // eMart에 심청이 방문
		store[0].Visit(customer[3].name);
		
		customer[1].Visit(store[0].name); // eMart에 김철수가 방문
		store[0].Visit(customer[1].name);
		
		customer[4].Visit(store[0].name); // eMart에 전우치가 방문
		store[0].Visit(customer[4].name);
		
		Thread r = new Thread(new PrintLine());
		
		r.start();
		
		s = JOptionPane.showInputDialog("확진자의 이름을 입력해주세요.");
		
		Thread t = new PrintAttatched();
		
		t.start();
		

	}
	
}

