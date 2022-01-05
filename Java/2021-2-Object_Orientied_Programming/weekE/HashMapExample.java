package WeekE;
import java.util.HashMap;
import java.util.Map;

class Student1 {
	public int sno;
	public String name;
	
	public Student1(int sno, String name) {
		this.sno = sno;
		this.name =name;
	}
	public boolean equals(Object obj) {
		if(obj instanceof Student1) {
			Student1 student = (Student1)obj;
			return (sno == student.sno) && (name.equals(student.name));
		} else {
			return false;
		}
	}
	public int hashCode() {
		return sno + name.hashCode();
	}
}

public class HashMapExample {

	public static void main(String[] args) {
		Map<Student1, Integer> map = new HashMap<Student1, Integer>();
		
		map.put(new Student1(1, "È«±æµ¿"), 95);
		map.put(new Student1(1, "È«±æµ¿"), 95);
		
		System.out.println("ÃÑ Entry ¼ö: " + map.size());
	}

}
