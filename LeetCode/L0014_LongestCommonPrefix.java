package leetcode.metods;

public class L0014_LongestCommonPrefix {

	public static String longestCommonPrefix(String[] strs) {
		if (strs == null || strs.length == 0) {
			return "";
		}

		String commonPrefix = strs[0];

		for (int i = 0; i < strs.length; i++) {
			while (strs[i].indexOf(commonPrefix) != 0) {
				commonPrefix = commonPrefix.substring(0, commonPrefix.length() - 1);
				if (commonPrefix.isEmpty()) {
					return "";
				}
			}
		}
		return commonPrefix;
	}

}
