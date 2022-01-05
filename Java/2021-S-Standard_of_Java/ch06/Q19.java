package ch06;

public class Q19 {
	static int[] shuffle(int[] arr) {
		for(int i=0; i < arr.length; i++) {
			int r = (int)(Math.random() * arr.length);
			int tmp;
			tmp = arr[i];
			arr[i] = arr[r];
			arr[r] = tmp;
		}
		return arr;
	}
	
	public static void main(String[] args) {
		int[] original = {1, 2, 3, 4, 5, 6, 7, 8, 9};
		System.out.println(java.util.Arrays.toString(original));
		
		int[] result = shuffle(original);
		System.out.println(java.util.Arrays.toString(result));
	}

}
