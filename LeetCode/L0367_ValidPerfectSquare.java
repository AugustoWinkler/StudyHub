package leetcode.metods;

public class L0367_ValidPerfectSquare {

	public boolean isPerfectSquare(int num) {
		int entry = num;
		int result = 0;
		int impar = 1;
		while (num > 0) {
			if (((num -= impar) - (impar += 2)) < 0) {
				result++;
				break;
			}
			result++;
		}
		if ((result * result) == entry)
			return true;
		return false;
	}
}
