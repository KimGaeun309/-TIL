package Week5;

public class Ex05_05 {
	
	static void replaceSpace(char a[]) {
		for (int i=0; i<a.length; i++)
			if  (a[i] == ' ')
				a[i] = '_';
	}
	
	static void printCharArray(char a[]) {
		for (int i=0; i<a.length; i++)
			System.out.print(a[i]);
		System.out.println();
	}
	public static void main(String[] args) {
		char c[] = {'T', 'h', 'i', 's', ' ', 'i', 's', ' ',  'a', ' ', 'p', 'e', 'n', 'c', 'i', 'l', '.'};
		printCharArray(c);
		replaceSpace(c);
		printCharArray(c);
		
	}

}
