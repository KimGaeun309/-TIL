package weekA;
import java.util.Scanner;

public class ReadFileFromURL {

	public static void main(String[] args) throws Exception
	{
		System.out.print("Enter a URL");
		String URLString = new Scanner(System.in).next();
		
		try {
			java.net.URL url = new java.net.URL(URLString);
			Scanner input = new Scanner(url.openStream());
			int count = 0;
			while (input.hasNext()) {
				String line = input.nextLine();
				count += line.length();
				System.out.println(line);
			}
			
			System.out.println("The file size is " + count + " characters");
		}
		catch (java.net.MalformedURLException ex) {
			System.out.println("invalid URL");
		}
		catch (java.io.IOException ex) {
			System.out.println("IO Errors");
		}
		
	}

}
