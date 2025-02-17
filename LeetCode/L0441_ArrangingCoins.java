package leetcode.metods;

public class L0441_ArrangingCoins {

	public int arrangeCoins(int n) {
		int i = 1;
		while (n > 0) {
			n -= i;
			if (n < 0) {
				return i - 1;
			} else {
				i++;
			}
		}
		return i - 1;
	}
}
