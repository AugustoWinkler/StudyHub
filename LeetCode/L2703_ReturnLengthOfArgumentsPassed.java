package leetcode.metods;

public class L2703_ReturnLengthOfArgumentsPassed {

	public int scoreOfString(String s) {
		int sum = 0;
		for (int i = 1; i < s.length(); i++) {
			int temp = (int) s.charAt(i) - (int) s.charAt(i - 1);
			if (temp < 0) {
				temp = -temp;
			}
			sum += temp;
		}
		return sum;
	}

}
