package leetcode.metods;

public class L2011_FinalValueOfVariableAfterPerfomingOperations {

	public int finalValueAfterOperations(String[] operations) {
		int x = 0;
		for (String operator : operations) {
			if (operator.equals("--X") || operator.equals("X--")) {
				x--;
			} else {
				x++;
			}
		}
		return x;
	}

}
