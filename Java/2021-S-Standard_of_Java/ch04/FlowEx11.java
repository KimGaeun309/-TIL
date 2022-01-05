package ch04;
import java.util.*;
public class FlowEx11 {

	public static void main(String[] args) {
		System.out.print("´ç½ÅÀÇ ÁÖ¹Î¹øÈ£¸¦ ÀÔ·ÂÇÏ¼¼¿ä.(011231-1111222)>");
		
		Scanner scanner = new Scanner(System.in);
		String regNo = scanner.nextLine();
		char gender = regNo.charAt(7); // ÀÔ·Â¹ŞÀº ¹øÈ£ÀÇ 8¹øÂ° ¹®ÀÚ¸¦ gender¿¡ ÀúÀå
		
		switch(gender) {
		case '1': case '3':
			switch(gender) {
			case '1':
				System.out.println("´ç½ÅÀº 2000³â ÀÌÀü¿¡ Ãâ»ıÇÑ ³²ÀÚÀÔ´Ï´Ù.");
				break;
			case '3':
				System.out.println("´ç½ÅÀº 2000³â ÀÌÈÄ¿¡ Ãâ»ıÇÑ ³²ÀÚÀÔ´Ï´Ù.");
				break;
			}
			break;
		case '2': case '4':
			switch(gender) {
			case '2':
				System.out.println("´ç½ÅÀº 2000³â ÀÌÀü¿¡ Ãâ»ıÇÑ ¿©ÀÚÀÔ´Ï´Ù.");
				break;
			case'4':
				System.out.println("´ç½ÅÀº 2000³â ÀÌÈÄ¿¡ ­„»ıÇÑ ¿©ÀÚÀÔ´Ï´Ù.");
				break;
			}
			break;
		default:
			System.out.println("À¯È¿ÇÏÁö ¾ÊÀº ÁÖ¹Îµî·Ï¹øÈ£ÀÔ´Ï´Ù.");
		}
	} // mainÀÇ ³¡

}
