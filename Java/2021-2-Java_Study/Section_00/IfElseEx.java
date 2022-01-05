public class IfElseEx {

	public static void main(String[] args) {
		boolean isCar = false;
		boolean isHaveHouse = false;
		boolean isJob = false;
		boolean isGoldSpoon = false;
		int asset = 17000;
		
		int grade = MyGrade(isCar, isHaveHouse, isJob, isGoldSpoon, asset);
		
		System.out.println("your grade is " + grade);
	}
	
	static int MyGrade(boolean isCar, boolean isHaveHouse, boolean isJob, 
			boolean isGoldSpoon, int asset) {

		if (isGoldSpoon) {
			return 1;
		}
		else if (isHaveHouse) {
			return 2;
		}
		else if (isCar) {
			return 3;
		}
		else if (isJob) {
			return 4;
		}
		else {
			if (asset >= 300000000) {
				return 5;
			}
			else if (asset >= 10000000 && asset < 300000000) {
				return 6;
			}
			else if (asset >= 1000000 && asset < 10000000) {
				return 7;
			}
			else if (asset >= 17000 && asset < 1000000) {
				return 8;
			}
			else  {
				return 9;
			}
		}
	}

}
