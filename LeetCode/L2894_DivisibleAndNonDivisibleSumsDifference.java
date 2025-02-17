package leetcode.metods;

public class L2894_DivisibleAndNonDivisibleSumsDifference {

	public int differenceOfSums(int n, int m) {
		int n1 = 0, n2 = 0;

		for (int i = 0; i <= n; i++) {
			if (i % m == 0) {
				n2 += i;
			} else {
				n1 += i;
			}
		}
		return n1 - n2;
	}
}
