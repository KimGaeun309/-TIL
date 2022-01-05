package week9;

class Date {
	private int year;
	private int month;
	private int date;
	
	public Date(int year, int month, int date) {
		this.year = year;
		this.month = month;
		this.date = date;
	}
	
	@Override
	public String toString() {
		return "Date [year=" + year + ", month=" + month + ", date" + date + "]";
	}
}

class Employee {
	private String name;
	private Date birthDate;
	
	public Employee(String name, Date birthDate) {
		this.name = name;
		this.birthDate = birthDate;
	}
	
	@Override
	public String toString() {
		return "Employee [name=" + name + ", birthDate=" + birthDate + "]";
	}
}

public class Has_A {

	public static void main(String[] args) {
		Date birth = new Date(1990, 1, 1);
		
		Employee employee = new Employee("ȫ�浿", birth);
		
		System.out.println(employee);
	}

}
